from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from typing import List
from crewai.agents.agent_builder.base_agent import BaseAgent
import yaml
import os

@CrewBase
class ExecucaoAnalisesCrew:
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
    def executor_analitico(self) -> Agent:
        return Agent(
            role=self.agents_config['executor_analitico']['role'],
            goal=self.agents_config['executor_analitico']['goal'],
            backstory=self.agents_config['executor_analitico']['backstory'],
            verbose=True
        )

    @task
    def executar_analises(self) -> Task:
        return Task(
            description=self.tasks_config['executar_analises']['description'],
            expected_output=self.tasks_config['executar_analises']['expected_output'],
            agent=self.executor_analitico()
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.executor_analitico()],
            tasks=[self.executar_analises()],
            process=Process.sequential,
            verbose=True
        )
