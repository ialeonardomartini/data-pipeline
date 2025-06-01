from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from typing import List
from crewai.agents.agent_builder.base_agent import BaseAgent

@CrewBase
class EbookIntroCrew:
    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def copywriter(self) -> Agent:
        return Agent(config=self.agents_config['copywriter'], verbose=True)

    @task
    def create_copy_intro(self) -> Task:
        return Task(config=self.tasks_config['create_copy_intro'])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )

@CrewBase
class EbookEdaCrew:
    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def copywriter(self) -> Agent:
        return Agent(config=self.agents_config['copywriter'], verbose=True)

    @task
    def create_copy_intro(self) -> Task:
        return Task(config=self.tasks_config['create_copy_eda'])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )

@CrewBase
class EbookInsightsCrew:
    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def copywriter(self) -> Agent:
        return Agent(config=self.agents_config['copywriter'], verbose=True)

    @task
    def create_copy_intro(self) -> Task:
        return Task(config=self.tasks_config['create_copy_insights'])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )

@CrewBase    
class EbookConclusaoCrew:
    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def copywriter(self) -> Agent:
        return Agent(config=self.agents_config['copywriter'], verbose=True)

    @task
    def create_copy_intro(self) -> Task:
        return Task(config=self.tasks_config['create_copy_conclusao'])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )