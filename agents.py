from textwrap import dedent
from crewai import Agent

class GameAgents():
    def game_designer_agent(self):
        return Agent(
            role='Game Designer',
            goal='Design engaging and challenging levels for the game',
            backstory=dedent("""
                You are a creative game designer with a deep understanding of game
                mechanics and player psychology. Your goal is to design levels that
                are both fun and challenging, keeping players engaged.
            """),
            allow_delegation=True,
            verbose=True,
            llm='gpt-4o-mini'
        )

    def game_developer_agent(self):
        return Agent(
            role='Game Developer',
            goal='Implement game mechanics and ensure smooth gameplay',
            backstory=dedent("""
                You are an experienced game developer with expertise in implementing
                game mechanics, physics, and AI. You work closely with game designers
                to bring their vision to life, ensuring the game is fun and runs smoothly.
            """),
            allow_delegation=True,
            verbose=True,
            llm='gpt-4o-mini'
        )

    def game_artist_agent(self):
        return Agent(
            role='Game Artist',
            goal='Create visually appealing game assets and animations',
            backstory=dedent("""
                You are a talented game artist with a knack for creating visually
                stunning assets and animations. You work closely with designers
                and developers to ensure the game's visual style is consistent and
                appealing.
            """),
            allow_delegation=True,
            verbose=True,
            llm='gpt-4o-mini'
        )
