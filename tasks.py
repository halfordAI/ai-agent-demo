from textwrap import dedent
from crewai import Task

class CrewTasks():
	def code_task(self, agent, code):
		return Task(description=dedent(f"""You will create a landing page using HTML, CSS, and JavaScript, in a single file. 
			You must write the full implementation code for the instructions. Do not say you can't do it.
			Be sure to save your code when you are finished.
								 
			These are the instructions:

			Instructions
			------------
    		{code}

			Your Final answer must be the result of your save code tool, and nothing else.
			"""),
			agent=agent
		)

	def review_task(self, agent, code):
		return Task(description=dedent(f"""\
			You are helping create a landing page using HTML, these are the instructions:

			Instructions
			------------
			{code}

			Using the code provided, check for errors. Check for logic errors,
			syntax errors, missing imports, variable declarations, mismatched brackets,
			and security vulnerabilities. Do not make suggestions. Only report any errors or issues.

			If you are not provided code, use the tool to get the code.

			Your Final answer must be the full HTML code with embedded CSS and JavaScript, only the HTML file code and nothing else.
			"""),
			agent=agent
		)

	def evaluate_task(self, agent, code):
		return Task(description=dedent(f"""\
			You are helping create a landing page using HTML, these are the instructions:

			Instructions
			------------
			{code}

			You will look over the code to insure that it is complete and
			does the job that it is supposed to do. Do not make suggestions. Only review the code and ensure
			it fulfills the provided instructions.

			If you are not provided code, use the tool to get the code.

			Your Final answer must be the full HTML code with embedded CSS and JavaScript, only the HTML file code and nothing else.
			"""),
			agent=agent
		)

	def get_feedback(self, agent, code):
		return Task(description=dedent(f"""\
			The team has created a landing page using HTML, these are the instructions from the client:

			Instructions
			------------
			{code}

			You will be provided the latest project code to give to the client for input. If you are not provided with the code, then use a tool to get the code. If the tool does not give you code, tell the Senior Software Engineer that the code was not saved, and to redo the task.
			You will use a tool to get the clients input. This will be the clients feedback. Report the client's feedback back to the team.
			You will continue to get feedback from the client until the client says the project is complete.

			If the client requests changes, then ask the Senior Software Engineer to make the changes and be sure to save the updated code.

			Your Final answer must be the full project code and the client's feedback.
			"""),
			agent=agent
		)