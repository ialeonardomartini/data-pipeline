from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from typing import List
from crewai.agents.agent_builder.base_agent import BaseAgent
import yaml
import os

@CrewBase
class AnaliseDefinicaoCrew:
    agents: List[BaseAgent]
    tasks: List[Task]

    def __init__(self):
        # Carrega configurações dos agentes
        with open(os.path.join(os.path.dirname(__file__), "config/agents.yaml")) as f:
            self.agents_config = yaml.safe_load(f)
        
        # Carrega configurações das tasks
        with open(os.path.join(os.path.dirname(__file__), "config/tasks.yaml")) as f:
            self.tasks_config = yaml.safe_load(f)

    @agent
    def analise_estrategista(self) -> Agent:
        return Agent(
            role=self.agents_config['analise_estrategista']['role'],
            goal=self.agents_config['analise_estrategista']['goal'],
            backstory=self.agents_config['analise_estrategista']['backstory'],
            verbose=True
        )

    @task
    def definir_analises(self) -> Task:
        return Task(
            description=self.tasks_config['definir_analises']['description'],
            expected_output=self.tasks_config['definir_analises']['expected_output'],
            agent=self.analise_estrategista()
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.analise_estrategista()],
            tasks=[self.definir_analises()],
            process=Process.sequential,
            verbose=True
        )
