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
senior_engineer_agent = agents.senior_engineer_agent()
qa_engineer_agent = agents.qa_engineer_agent()
chief_qa_engineer_agent = agents.chief_qa_engineer_agent()
game_designer_agent = agents.game_designer_agent()
game_developer_agent = agents.game_developer_agent()
game_artist_agent = agents.game_artist_agent()

# Create Tasks
design_game = tasks.design_task(game_designer_agent, game)
develop_game = tasks.develop_task(game_developer_agent, game)
create_art = tasks.create_art_task(game_artist_agent, game)
code_game = tasks.code_task(senior_engineer_agent, game)
review_game = tasks.review_task(qa_engineer_agent, game)
approve_game = tasks.evaluate_task(chief_qa_engineer_agent, game)

# Create Crew responsible for the game development
crew = Crew(
    agents=[
        senior_engineer_agent,
        qa_engineer_agent,
        chief_qa_engineer_agent,
        game_designer_agent,
        game_developer_agent,
        game_artist_agent
    ],
    tasks=[
        design_game,
        develop_game,
        create_art,
        code_game,
        review_game,
        approve_game
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
