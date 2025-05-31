
from src.flow.pipeline_flow import AnalisePipelineFlow, PipelineState
import os
from dotenv import load_dotenv

load_dotenv()


if __name__ == "__main__":
    with open("dataframe.csv", "r") as f:
        csv_content = f.read()

    flow = AnalisePipelineFlow()
    flow.state.dataframe = csv_content
    result = flow.kickoff()

    print("\n✅ Pipeline finalizado com sucesso!")