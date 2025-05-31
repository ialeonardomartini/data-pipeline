from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from typing import List
from crewai.agents.agent_builder.base_agent import BaseAgent

@CrewBase
class EdaCrew:
    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def eda_analyst(self) -> Agent:
        return Agent(config=self.agents_config['eda_analyst'], verbose=True)

    @task
    def realizar_eda(self) -> Task:
        return Task(config=self.tasks_config['realizar_eda'])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
