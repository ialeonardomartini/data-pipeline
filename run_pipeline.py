from src.flow.pipeline_flow import AnalisePipelineFlow, PipelineState, CreateEbookText
import os
from dotenv import load_dotenv
import json

load_dotenv()

if __name__ == "__main__":
    with open("dataframe.csv", "r") as f:
        csv_content = f.read()

    # 🚀 Parte 1: Executar pipeline de análise
    flow = AnalisePipelineFlow()
    flow.state.dataframe = csv_content
    result = flow.kickoff()


    # ✅ Recarrega eda e resultados salvos após a execução do flow
    with open("output/eda.md", "r") as f:
        eda_output = f.read()

    with open("output/resultados.json", "r") as f:
        resultados = json.load(f)

    with open("output/analises.json", "r") as f:
        analises = json.load(f)  

    # 🔁 Atualiza state com dados garantidos
    state = PipelineState(
        dataframe=csv_content,
        eda_output=eda_output,
        resultados=resultados,
        analises=analises
    )

    print("\n✅ Parte 1 finalizada com sucesso!")

    # 🧠 Parte 2: Geração dos textos
    ebook_flow = CreateEbookText()
    ebook_flow.state.dataframe = csv_content
    ebook_flow.state.eda_output = eda_output
    ebook_flow.state.resultados = resultados
    print("🔎 Enviando para intro:")
    print(f"EDA: {state.eda_output[:300]}")
    print(f"RESULTADOS: {state.resultados[:300]}")


    result_ebook = ebook_flow.kickoff()

    with open("output/ebook_intro.md", "r") as f:
        ebook_intro = f.read()    
    
    with open("output/ebook_eda.md", "r") as f:
        ebook_eda = f.read()    

    with open("output/ebook_insights.json", "r") as f:
        ebook_insights = json.load(f)    

    with open("output/ebook_conclusao.md", "r") as f:
        ebook_conclusao = f.read()        

    state = PipelineState(
        dataframe=csv_content,
        eda_output=eda_output,
        resultados=resultados,
        analises=analises,
        ebook_intro=ebook_intro,
        ebook_eda=ebook_eda,
        ebook_insights=ebook_insights,
        ebook_conclusao=ebook_conclusao
    )


    print("\n✅ Parte 2 finalizada com sucesso!")
