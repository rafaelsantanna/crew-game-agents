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

    def create_sound_task(self, agent, game):
        return Task(
            description=dedent(f"""You are creating sound for a game, these are the instructions:
                Instructions
                ------------
                {game}

                Create immersive soundscapes and sound effects, ensuring they enhance the gameplay experience.

                Your Final answer must be a collection of sound effects and background music.
            """),
            agent=agent,
            expected_output="The final output should be a collection of sound effects and background music."
        )

    def design_ui_ux_task(self, agent, game):
        return Task(
            description=dedent(f"""You are designing the UI/UX for a game, these are the instructions:
                Instructions
                ------------
                {game}

                Design intuitive and engaging user interfaces, ensuring a seamless player experience.

                Your Final answer must be a detailed UI/UX design document.
            """),
            agent=agent,
            expected_output="The final output should be a detailed UI/UX design document."
        )

    def design_levels_task(self, agent, game):
        return Task(
            description=dedent(f"""You are designing levels for a game, these are the instructions:
                Instructions
                ------------
                {game}

                Design and balance game levels to provide a challenging and enjoyable experience for players.

                Your Final answer must be a detailed level design document.
            """),
            agent=agent,
            expected_output="The final output should be a detailed level design document."
        )

    def develop_ai_task(self, agent, game):
        return Task(
            description=dedent(f"""You are developing AI for a game, these are the instructions:
                Instructions
                ------------
                {game}

                Develop intelligent behaviors for non-player characters (NPCs) to enhance the gameplay experience.

                Your Final answer must be the complete AI code.
            """),
            agent=agent,
            expected_output="The final output should be the complete AI code."
        )

    def manage_project_task(self, agent, game):
        return Task(
            description=dedent(f"""You are managing the project for a game, these are the instructions:
                Instructions
                ------------
                {game}

                Coordinate tasks and ensure the project stays on schedule, providing updates and resolving issues as they arise.

                Your Final answer must be a project management report.
            """),
            agent=agent,
            expected_output="The final output should be a project management report."
        )
