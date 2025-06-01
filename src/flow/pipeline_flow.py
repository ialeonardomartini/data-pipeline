import os
import json
from typing import List, Dict, Any
from pydantic import BaseModel
from main import safe_json_from_markdown_block
from crewai.flow.flow import Flow, start, listen
from src.crews.crew_eda.crew import EdaCrew
from src.crews.crew_define_analyses.crew import AnaliseDefinicaoCrew
from src.crews.crew_execute_analyses.crew import ExecucaoAnalisesCrew
from src.crews.crew_ebook.crew import (
    EbookIntroCrew,
    EbookEdaCrew,
    EbookInsightsCrew,
    EbookConclusaoCrew,
)

# ✅ Classe de estado unificada
class PipelineState(BaseModel):
    dataframe: str = ""
    eda_output: str = ""
    analises: List[Dict[str, Any]] = []
    resultados: List[Dict[str, Any]] = []
    ebook_intro: str = ""
    ebook_eda: str = ""
    ebook_insights: List[Dict[str, Any]] = []
    ebook_conclusao: str = ""


# ✅ Fase 1: Pipeline de análise
class AnalisePipelineFlow(Flow[PipelineState]):

    @start()
    def fazer_eda(self):
        print("🚀 Iniciando EDA...")
        resultado = EdaCrew().crew().kickoff(inputs={"dataframe": self.state.dataframe})
        print("🔎 Resultado.raw do agente:")
        print(resultado.raw)
        self.state.eda_output = resultado.raw

        os.makedirs("output", exist_ok=True)
        with open("output/eda.md", "w") as f:
            f.write(self.state.eda_output)

        return self.state.eda_output

    @listen(fazer_eda)
    def definir_analises(self, eda_output):
        print("🧠 Definindo análises a serem feitas...")
        resultado = AnaliseDefinicaoCrew().crew().kickoff(inputs={"eda_output": eda_output})
        print("🔎 Resultado.raw do agente:")
        print(resultado.raw)

 #       raw_clean = resultado.raw.strip()
 #       if raw_clean.startswith("```json"):
 #           raw_clean = raw_clean.replace("```json", "").strip()
 #       if raw_clean.endswith("```"):
 #           raw_clean = raw_clean[:-3].strip()

        try:
            self.state.analises = safe_json_from_markdown_block(resultado.raw)
        except json.JSONDecodeError:
            print("❌ Erro ao decodificar JSON \n ❌ Erro ao decodificar JSON \n ❌ Erro ao decodificar JSON")
            self.state.analises = []

        with open("output/analises.json", "w") as f:
            json.dump(self.state.analises, f, indent=2)

        return self.state.analises

    @listen(definir_analises)
    def executar_analises(self, analises):
        print("⚙️ Executando análises propostas...")
        resultado = ExecucaoAnalisesCrew().crew().kickoff(inputs={
            "dataframe": self.state.dataframe,
            "analises": json.dumps(analises, indent=2)
        })
        print("🔎 Resultado.raw do agente:")
        print(resultado.raw)

        raw_clean = resultado.raw.strip()
        if raw_clean.startswith("```json"):
            raw_clean = raw_clean.replace("```json", "").strip()
        if raw_clean.endswith("```"):
            raw_clean = raw_clean[:-3].strip()

        try:
            self.state.resultados = json.loads(raw_clean)
        except json.JSONDecodeError:
            print("❌ Erro ao decodificar JSON:")
            print(raw_clean)
            self.state.resultados = []

        with open("output/resultados.json", "w") as f:
            json.dump(self.state.resultados, f, indent=2)

        return self.state.resultados
    


# ✅ Fase 2: Geração dos textos do e-book
class CreateEbookText(Flow[PipelineState]):

    @start()
    def fazer_ebook_intro(self):
        eda_output = self.state.eda_output
        resultados = self.state.resultados

        print("🧠 Iniciando geração da introdução...")
        print(f"🔎 EDA: {eda_output[:300]}")
        print(f"🔎 RESULTADOS: {resultados[:300]}")

        resultado = EbookIntroCrew().crew().kickoff(inputs={
            "eda": eda_output,
            "resultados": json.dumps(resultados, indent=2)
        })

        print("📘 Intro gerada:")
        print(resultado.raw)

        self.state.ebook_intro = resultado.raw
        os.makedirs("output", exist_ok=True)
        with open("output/ebook_intro.md", "w") as f:
            f.write(self.state.ebook_intro)

        return self.state.ebook_intro

    @listen(fazer_ebook_intro)
    def fazer_ebook_eda(self, eda_output):
        eda_output = self.state.eda_output
        print("📊 Gerando seção de EDA...")
        resultado = EbookEdaCrew().crew().kickoff(inputs={"eda": eda_output})
        self.state.ebook_eda = resultado.raw

        with open("output/ebook_eda.md", "w") as f:
            f.write(self.state.ebook_eda)

        return self.state.ebook_eda

    @listen(fazer_ebook_eda)
    def fazer_ebook_insights(self, resultados):
        resultados = self.state.resultados
        print("🔍 Gerando seção de insights...")
        resultado = EbookInsightsCrew().crew().kickoff(inputs={"resultados": resultados})
        self.state.ebook_insights = resultado.raw


        raw_clean = resultado.raw.strip()
        if raw_clean.startswith("```json"):
            raw_clean = raw_clean.replace("```json", "").strip()
        if raw_clean.endswith("```"):
            raw_clean = raw_clean[:-3].strip()

        try:
            self.state.ebook_insights = json.loads(raw_clean)
        except json.JSONDecodeError:
            print("❌ Erro ao decodificar JSON:")
            print(raw_clean)
            self.state.ebook_insights = []

        with open("output/ebook_insights.json", "w") as f:
            json.dump(self.state.ebook_insights, f, indent=2)

        return self.state.ebook_insights

    @listen(fazer_ebook_insights)
    def fazer_ebook_conclusao(self):
        print("📝 Gerando conclusão...")
        resultado = EbookConclusaoCrew().crew().kickoff()
        self.state.ebook_conclusao = resultado.raw

        with open("output/ebook_conclusao.md", "w") as f:
            f.write(self.state.ebook_conclusao)

        return self.state.ebook_conclusao
