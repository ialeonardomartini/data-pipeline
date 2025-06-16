from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from typing import List
from crewai.agents.agent_builder.base_agent import BaseAgent
import yaml
import os

@CrewBase
class EbookIntroCrew:
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
    def copywriter(self) -> Agent:
        return Agent(
            role=self.agents_config['copywriter']['role'],
            goal=self.agents_config['copywriter']['goal'],
            backstory=self.agents_config['copywriter']['backstory'],
            verbose=True
        )

    @task
    def create_copy_intro(self) -> Task:
        return Task(
            description=self.tasks_config['create_copy_intro']['description'],
            expected_output=self.tasks_config['create_copy_intro']['expected_output'],
            agent=self.copywriter()
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.copywriter()],
            tasks=[self.create_copy_intro()],
            process=Process.sequential,
            verbose=True
        )

@CrewBase
class EbookEdaCrew:
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
    def copywriter(self) -> Agent:
        return Agent(
            role=self.agents_config['copywriter']['role'],
            goal=self.agents_config['copywriter']['goal'],
            backstory=self.agents_config['copywriter']['backstory'],
            verbose=True
        )

    @task
    def create_copy_intro(self) -> Task:
        return Task(
            description=self.tasks_config['create_copy_eda']['description'],
            expected_output=self.tasks_config['create_copy_eda']['expected_output'],
            agent=self.copywriter()
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.copywriter()],
            tasks=[self.create_copy_intro()],
            process=Process.sequential,
            verbose=True
        )

@CrewBase
class EbookInsightsCrew:
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
    def copywriter(self) -> Agent:
        return Agent(
            role=self.agents_config['copywriter']['role'],
            goal=self.agents_config['copywriter']['goal'],
            backstory=self.agents_config['copywriter']['backstory'],
            verbose=True
        )

    @task
    def create_copy_intro(self) -> Task:
        return Task(
            description=self.tasks_config['create_copy_insights']['description'],
            expected_output=self.tasks_config['create_copy_insights']['expected_output'],
            agent=self.copywriter()
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.copywriter()],
            tasks=[self.create_copy_intro()],
            process=Process.sequential,
            verbose=True
        )

@CrewBase    
class EbookConclusaoCrew:
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
    def copywriter(self) -> Agent:
        return Agent(
            role=self.agents_config['copywriter']['role'],
            goal=self.agents_config['copywriter']['goal'],
            backstory=self.agents_config['copywriter']['backstory'],
            verbose=True
        )

    @task
    def create_copy_intro(self) -> Task:
        return Task(
            description=self.tasks_config['create_copy_conclusao']['description'],
            expected_output=self.tasks_config['create_copy_conclusao']['expected_output'],
            agent=self.copywriter()
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.copywriter()],
            tasks=[self.create_copy_intro()],
            process=Process.sequential,
            verbose=True
        )