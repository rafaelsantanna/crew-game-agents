from textwrap import dedent
from crewai import Task

class GameTasks():
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
