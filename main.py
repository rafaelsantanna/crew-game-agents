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
sound_designer_agent = agents.sound_designer_agent()
ui_ux_designer_agent = agents.ui_ux_designer_agent()
level_designer_agent = agents.level_designer_agent()
ai_specialist_agent = agents.ai_specialist_agent()
project_manager_agent = agents.project_manager_agent()

# Create Tasks
design_game = tasks.design_task(game_designer_agent, game)
develop_game = tasks.develop_task(game_developer_agent, game)
create_art = tasks.create_art_task(game_artist_agent, game)
create_sound = tasks.create_sound_task(sound_designer_agent, game)
design_ui_ux = tasks.design_ui_ux_task(ui_ux_designer_agent, game)
design_levels = tasks.design_levels_task(level_designer_agent, game)
develop_ai = tasks.develop_ai_task(ai_specialist_agent, game)
manage_project = tasks.manage_project_task(project_manager_agent, game)

# Create Crew responsible for the game development
crew = Crew(
    agents=[
        game_designer_agent,
        game_developer_agent,
        game_artist_agent,
        sound_designer_agent,
        ui_ux_designer_agent,
        level_designer_agent,
        ai_specialist_agent,
        project_manager_agent
    ],
    tasks=[
        design_game,
        develop_game,
        create_art,
        create_sound,
        design_ui_ux,
        design_levels,
        develop_ai,
        manage_project
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
