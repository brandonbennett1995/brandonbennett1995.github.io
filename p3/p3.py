# %% [markdown]
# # QUESTIONS
#
# 1. Write an SQL query to create a new dataframe about baseball players who attended BYU-Idaho.
# The new table should contain five columns:
#
#    1. `playerID`
#    2. `schoolID`
#    3. `salary`
#    4. `yearID`
#    5. `teamID` *associated with each salary*
#
#    Order the table by salary (highest to lowest) and print out the table in your report.
#
# 2. This three-part question requires you to calculate batting average (number of hits divided by the number of at-bats)
#
#     - Write an SQL query that provides playerID, yearID, and batting average for players with at least 1 at bat that year. Sort the table from highest batting average to lowest, and then by playerid alphabetically. Show the top 5 results in your report.
#     - Use the same query as above, but only include players with at least 10 at bats that year. Print the top 5 results.
#     - Now calculate the batting average for players over their entire careers (all years combined). Only include players with at least 100 at bats, and print the top 5 results.
#

import sqlite3

import numpy as np

# %%
import pandas as pd
import plotly.express as px

# careful to list your path to the file or save it in the same place as your .qmd or .py file
sqlite_file = "lahmansbaseballdb.sqlite"
con = sqlite3.connect(sqlite_file)

q = "SELECT * FROM allstarfull LIMIT 5"
results = pd.read_sql_query(q, con)

results

# %%
# Getting the master table data
q = """--sql
    SELECT * 
    FROM sqlite_master 
    WHERE type='table'
    """
table = pd.read_sql_query(q, con)
table.filter(["name"])

# %%
q = """--sql
    SELECT * FROM schools
    WHERE name_full = "Brigham Young University-Idaho"
    """

schools = pd.read_sql_query(q, con)
byui = schools.get("schoolID")[0]
# f"{byui}"
schools

# %%
q = """--sql
    SELECT people.nameGiven AS `Given Name`, 
           people.playerID AS `Player ID`, 
           collegeplaying.schoolID AS `School ID`,
           salaries.teamID AS `Team ID`,
           salaries.yearID AS `Year`,
           salaries.salary AS `Salary`
    FROM people
    JOIN collegeplaying ON people.playerID = collegeplaying.playerID
    JOIN salaries ON people.playerID = salaries.playerID
    WHERE schoolID = 'idbyuid'
    ORDER BY salary DESC
    """

player_info = pd.read_sql_query(q, con)
player_info = player_info.replace("idbyuid", "Brigham Young University-Idaho")
player_info["Salary"] = player_info["Salary"].map(lambda x: f"$ {x:,.0f}")
player_info = player_info.drop_duplicates()
player_info.reset_index(drop=True)

# %% [markdown]
# - Write an SQL query that provides `playerID`, `yearID`, and `batting_average` for players with at least 1 at bat that year.
# - Sort the table from highest batting average to lowest, and then by playerid alphabetically.
# - Show the top 5 results in your report.

# %%
q = """--sql
    SELECT playerID, yearID, H, AB
    FROM batting
    WHERE AB > 0
    """

batting_avgs = pd.read_sql_query(q, con)
batters = (
    batting_avgs.groupby("playerID")
    .agg(ab=("AB", "sum"), h=("H", "sum"))
    .assign(ba=lambda x: x.h / x.ab)
)
batters.sort_values("ba", ascending=False).head().reset_index()

# %%
q = """--sql
    SELECT playerID, yearID, H, AB
    FROM batting
    WHERE AB >= 100
    """

high_batting_avgs = pd.read_sql_query(q, con)
high_batters = (
    high_batting_avgs.groupby("playerID")
    .agg(ab=("AB", "sum"), h=("H", "sum"))
    .assign(ba=lambda x: x.h / x.ab)
)
high_batters.sort_values("ba", ascending=False).head().reset_index()

# %% [markdown]
# - Pick any two baseball teams and compare them using a metric of your choice (average salary, home runs, number of wins, etc).
# - Write an SQL query to get the data you need, then make a graph using Plotly Express to visualize the comparison. What do you learn?

# %%
q = """--sql
    SELECT * FROM teams
    """

mlb_players = pd.read_sql_query(q, con)
mlb_players

# %%
q = """--sql
    SELECT salaries.yearID AS `Year`, 
           salaries.teamID AS `Team ID`,
           teams.name AS `Team Name`,
           salaries.playerID AS `Player ID`, 
           people.nameGiven AS `Player Name`,
           fielding.POS as `Position`,
           salaries.salary AS `Salary`
    FROM salaries
    JOIN fielding
        USING (yearID, teamID, playerID)
    INNER JOIN people on salaries.playerID=people.playerID
    INNER JOIN teams on salaries.teamID=teams.teamID
    """

teams_players_pos = pd.read_sql_query(q, con)
teams_players_pos

# %% [markdown]
# I have picked Boston Red Socks and New York Yankees

# %%
q = """--sql
    SELECT salaries.yearID AS `Year`,
           salaries.teamID AS `Team`,
           salaries.playerID AS `Player ID`,
           people.nameGiven AS `Player Name`,
           fielding.POS as `Position`,
           salaries.salary AS `Salary`
    FROM salaries
    JOIN fielding
        USING (yearID, teamID, playerID)
    INNER JOIN people on salaries.playerID=people.playerID
    WHERE salaries.teamID IN ('BOS', 'NYA')
    """

mlb_players = pd.read_sql_query(q, con)
mlb_players["Team"] = mlb_players["Team"].replace(
    ["BOS", "NYA"], ["Boston Red Sox", "New York Yankees"]
)
mlb_players

# %%
avg_player_salary = (
    mlb_players.groupby(["Year", "Team"]).agg(avg_salary=("Salary", np.mean))
).reset_index()
avg_player_salary["avg_salary"] = avg_player_salary["avg_salary"].map(
    lambda x: float(f"{x:.2f}")
)
avg_player_salary

# %%
fig = px.bar(
    avg_player_salary,
    x="Year",
    y="avg_salary",
    color="Team",
    title="Player Salary | 1985-2016",
    barmode="group",
    color_discrete_map={"Boston Red Sox": "#BD3039", "New York Yankees": "#003087"},
)

fig.update_xaxes(insiderange=[1984.5, 2016.5])

fig.update_yaxes(title="Average Salary", tickprefix="$")

fig.update_layout(
    legend=dict(
        title="",
        orientation="h",
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.005,
    )
)

fig.show()

# %%
avg_player_salary_by_pos = (
    mlb_players.groupby(["Team", "Position"]).agg(avg_salary=("Salary", np.mean))
).reset_index()

avg_player_salary_by_pos["avg_salary"] = avg_player_salary_by_pos["avg_salary"].map(
    lambda x: float(f"{x:.2f}")
)
avg_player_salary_by_pos

# %%
fig = px.bar(
    avg_player_salary_by_pos,
    x="Position",
    y="avg_salary",
    color="Team",
    title="Player Salary by Position",
    text_auto="$.2s",
    barmode="group",
    color_discrete_map={"Boston Red Sox": "#BD3039", "New York Yankees": "#003087"},
)

fig.update_yaxes(title="Average Salary", tickprefix="$")

fig.update_layout(
    legend=dict(
        title="",
        orientation="h",
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.75,
    )
)

fig.show()
