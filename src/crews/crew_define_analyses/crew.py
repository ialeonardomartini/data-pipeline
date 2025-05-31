from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from typing import List
from crewai.agents.agent_builder.base_agent import BaseAgent

@CrewBase
class AnaliseDefinicaoCrew:
    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def analise_estrategista(self) -> Agent:
        return Agent(config=self.agents_config['analise_estrategista'], verbose=True)

    @task
    def definir_analises(self) -> Task:
        return Task(config=self.tasks_config['definir_analises'])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
