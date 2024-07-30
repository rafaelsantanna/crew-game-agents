from dotenv import load_dotenv
load_dotenv()

from crewai import Crew
from tasks import GameTasks
from agents import GameAgents

tasks = GameTasks()
agents = GameAgents()

print("## Welcome to the Game Crew")
print('-------------------------------')
game = input("What is the game you would like to build? What will be the mechanics?\n")

# Create Agents
game_designer_agent = agents.game_designer_agent()
game_developer_agent = agents.game_developer_agent()
game_artist_agent = agents.game_artist_agent()

# Create Tasks
design_game = tasks.design_task(game_designer_agent, game)
develop_game = tasks.develop_task(game_developer_agent, game)
create_art = tasks.create_art_task(game_artist_agent, game)

# Create Crew responsible for the game development
crew = Crew(
    agents=[
        game_designer_agent,
        game_developer_agent,
        game_artist_agent
    ],
    tasks=[
        design_game,
        develop_game,
        create_art
    ],
    verbose=True
)

game_result = crew.kickoff()

# Print results
print("\n\n########################")
print("## Here is the result")
print("########################\n")
print("Final code for the game:")
print(game_result)
