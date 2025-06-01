from src.flow.pipeline_flow import PipelineState
from src.flow.pipeline_flow import CreateEbookText
import os
from dotenv import load_dotenv

load_dotenv()

def run_ebook(state: PipelineState):
    crew = CreateEbookText(state=state)
    result = crew.kickoff()

    os.makedirs("output", exist_ok=True)
    with open("output/ebook.md", "w") as f:
        for section in ["ebook_intro.md", "ebook_eda.md", "ebook_insights.md", "ebook_conclusao.md"]:
            path = os.path.join("output", section)
            if os.path.exists(path):
                with open(path) as s:
                    f.write(s.read() + "\n\n")

    print("✅ E-book gerado em output/ebook.md")
    return result
