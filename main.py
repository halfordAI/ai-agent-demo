import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Crew
from crewai.process import Process
from langchain_openai import ChatOpenAI

from tasks import CrewTasks
from agents import CrewAgents
from singleton import Singleton

# Uncomment the line below to use the latest GPT-4 turbo model
#os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"

tasks = CrewTasks()
agents = CrewAgents()

# Instantiate the Singleton so it's ready for use and is retained at the "main" level.
Singleton()

# Print welcome message
print("## Welcome to the Landing Page Crew")
print('-------------------------------')
code = input("What is the landing page you would like to build? What will be the topic, look, and style?\n")

# Create Agents
senior_engineer_agent = agents.senior_engineer_agent()
qa_engineer_agent = agents.qa_engineer_agent()
chief_qa_engineer_agent = agents.chief_qa_engineer_agent()
feedback_agent = agents.feedback_agent()

# Create Tasks
code_landing_page = tasks.code_task(senior_engineer_agent, code)
review_landing_page = tasks.review_task(qa_engineer_agent, code)
approve_landing_page = tasks.evaluate_task(chief_qa_engineer_agent, code)
get_feedback = tasks.get_feedback(feedback_agent, code)

# Create Crew responsible for Copy
crew = Crew(
	agents=[
		senior_engineer_agent,
		qa_engineer_agent,
		chief_qa_engineer_agent,
        feedback_agent
	],
	tasks=[
		code_landing_page,
		review_landing_page,
		approve_landing_page,
        get_feedback
	],
	verbose=True,
    process=Process.sequential
)

game = crew.kickoff()

# Print results
print("\n\n########################")
print("## Here is the result")
print("########################\n")
print("final code for the landing page:")
print(game)