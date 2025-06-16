from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from typing import List
from crewai.agents.agent_builder.base_agent import BaseAgent
import yaml
import os

@CrewBase
class EdaCrew:
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
    def eda_analyst(self) -> Agent:
        return Agent(
            role=self.agents_config['eda_analyst']['role'],
            goal=self.agents_config['eda_analyst']['goal'],
            backstory=self.agents_config['eda_analyst']['backstory'],
            verbose=True
        )

    @task
    def realizar_eda(self) -> Task:
        return Task(
            description=self.tasks_config['realizar_eda']['description'],
            expected_output=self.tasks_config['realizar_eda']['expected_output'],
            agent=self.eda_analyst()
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.eda_analyst()],
            tasks=[self.realizar_eda()],
            process=Process.sequential,
            verbose=True
        )
