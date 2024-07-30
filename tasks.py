from textwrap import dedent
from crewai import Task

class GameTasks():
    def code_task(self, agent, game):
        return Task(
            description=dedent(f"""You will create a game using python, these are the instructions:
                Instructions
                ------------
                {game}

                Your Final answer must be the full python code, only the python code and nothing else.
            """),
            agent=agent,
            expected_output="The final output should be the complete python code for the game."
        )

    def review_task(self, agent, game):
        return Task(
            description=dedent(f"""You are helping create a game using python, these are the instructions:
                Instructions
                ------------
                {game}

                Using the code you got, check for errors. Check for logic errors,
                syntax errors, missing imports, variable declarations, mismatched brackets,
                and security vulnerabilities.

                Your Final answer must be the full python code, only the python code and nothing else.
            """),
            agent=agent,
            expected_output="The reviewed code should be free of errors and vulnerabilities."
        )

    def evaluate_task(self, agent, game):
        return Task(
            description=dedent(f"""You are helping create a game using python, these are the instructions:
                Instructions
                ------------
                {game}

                You will look over the code to ensure that it is complete and
                does the job that it is supposed to do.

                Your Final answer must be the full python code, only the python code and nothing else.
            """),
            agent=agent,
            expected_output="The final evaluated code should be complete and functional."
        )

    def design_task(self, agent, game):
        return Task(
            description=dedent(f"""You are designing a game, these are the instructions:
                Instructions
                ------------
                {game}

                Your task is to design engaging and challenging levels, defining the game mechanics, 
                player objectives, and overall game flow.

                Your Final answer must be a detailed game design document.
            """),
            agent=agent,
            expected_output="The final output should be a detailed game design document."
        )

    def develop_task(self, agent, game):
        return Task(
            description=dedent(f"""You are developing a game, these are the instructions:
                Instructions
                ------------
                {game}

                Implement the game mechanics, physics, and AI as defined in the game design document, 
                ensuring smooth and fun gameplay.

                Your Final answer must be the complete implementation code.
            """),
            agent=agent,
            expected_output="The final output should be the complete implementation code."
        )

    def create_art_task(self, agent, game):
        return Task(
            description=dedent(f"""You are creating art for a game, these are the instructions:
                Instructions
                ------------
                {game}

                Create visually appealing game assets and animations, ensuring consistency with the game's visual style.

                Your Final answer must be a collection of game art assets and animations.
            """),
            agent=agent,
            expected_output="The final output should be a collection of game art assets and animations."
        )
