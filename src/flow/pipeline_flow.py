import os
import json
from typing import List, Dict, Any
from pydantic import BaseModel
from crewai.flow.flow import Flow, start, listen
from src.crews.crew_eda.crew import EdaCrew
from src.crews.crew_define_analyses.crew import AnaliseDefinicaoCrew
from src.crews.crew_execute_analyses.crew import ExecucaoAnalisesCrew

class PipelineState(BaseModel):
    dataframe: str = ""
    eda_output: str = ""
    analises: List[Dict[str, Any]] = []
    resultados: str = ""

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
        # Remove blocos markdown, se existirem
        raw_clean = resultado.raw.strip()
        if raw_clean.startswith("```json"):
            raw_clean = raw_clean.replace("```json", "").strip()
        if raw_clean.endswith("```"):
            raw_clean = raw_clean[:-3].strip()
        # Faz o parsing seguro
        try:
            self.state.analises = json.loads(raw_clean)
        except json.JSONDecodeError:
            print("❌ Erro ao decodificar JSON. Conteúdo recebido:")
            print(raw_clean)
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
        self.state.resultados = resultado.raw
        with open("output/resultados.md", "w") as f:
            f.write(self.state.resultados)
        return self.state.resultados


