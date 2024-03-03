from textwrap import dedent
from crewai import Agent
from langchain.tools import tool
from singleton import Singleton

class CrewAgents():
	# Create Tools
	@tool
	def input_tool(prompt: str, code: str = "") -> str:
		"""Collects client feedback about the project from the terminal based on a given feedback request or prompt.
		
		Args:
			prompt (str): The feedback request message to display to the client.
			code (str): The code to be reviewed for the project.
		
		Returns:
			str: The project code with the client's feedback as a string.
		"""
		feedback = ""

		if code == "":
			code = Singleton().get_code()

		refined_output = code
		feedback = input(prompt + "\nIf you are finished, type 'Finished'. Your feedback: ")
		if feedback.lower() != "finished":
			refined_output += "\n\n[Feedback from the client: {}]".format(feedback)
			return refined_output
		else:
			return "No feedback, project is complete."
		
	@tool
	def get_code_tool() -> str:
		"""Provides the latest code for the project.
		
		Args:
			None
		
		Returns:
			str: The project code as a string.
		"""
		
		# Get the code from the Singleton
		return Singleton().get_code()
		
	@tool
	def save_code_tool(code: str) -> bool:
		"""Saves the latest code for the project.
		
		Args:
			code (str): The latest project code to be saved.
		
		Returns:
			bool: A boolean indicating whether the code was saved successfully.
		"""
		
		# Save the code to the Singleton
		Singleton().set_code(code)
		
		return True

	def senior_engineer_agent(self):
		return Agent(
			role='Senior Software Engineer',
			goal='Create software as needed',
			backstory=dedent("""\
				You are a Senior Software Engineer at a leading tech think tank.
				Your expertise in programming in HTML, CSS, and JavaScript. You love writing new code
				but you do not like reviewing code. When asked to review code, you will tell the manager to
				ask the Software Quality Control Engineer to review the code instead. When it comes to the code,
				you are always verbose and always write the full code for the requirements provided. You NEVER use placeholders or
				omit code for brevity. Always remember to save your code when you are finished.
				Do your best to produce perfect code"""),
			allow_delegation=False,
			tools=[self.save_code_tool, self.get_code_tool],
			verbose=True
		)

	def qa_engineer_agent(self):
		return Agent(
			role='Software Quality Control Engineer',
  			goal='Create perfect code, by analyzing the code that is given for errors',
  			backstory=dedent("""\
				You are a software engineer that specializes in checking code
  			for errors. You have an eye for detail and a knack for finding
				hidden bugs.
  			You check for missing imports, variable declarations, mismatched
				brackets and syntax errors.
  			You also check for security vulnerabilities, and logic errors"""),
			allow_delegation=False,
			tools=[self.get_code_tool],
			verbose=True
		)

	def chief_qa_engineer_agent(self):
		return Agent(
			role='Chief Software Quality Control Engineer',
  			goal='Ensure that the code does the job that it is supposed to do',
  			backstory=dedent("""\
				You feel that programmers always do only half the job, so you are
				super dedicated to make high quality code."""),
			allow_delegation=True,
			tools=[self.get_code_tool],
			verbose=True
		)
	
	def feedback_agent(self):
		return Agent(
			role='Chief Client Relationship Manager',
  			goal='Ensure that the client is happy with the code that is produced.',
  			backstory=dedent("""\
				You are responsible for making sure that the client
				is happy with the code that is given. You are the one that will be
				communicating with the client and getting feedback from them.
					  
				Always make sure to provide the code to the client. If you were not provided with the code, then
				ask the manager to provide you with the code."""),
			allow_delegation=True,
			tools=[self.input_tool, self.get_code_tool],
			verbose=True
		)