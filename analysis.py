import pandas as pd
import csv
import plotly_express as px
import plotly.graph_objects as pg

print("")
print("Mathly - Student Report Card Analyzer")
print("")
print("Hi. Please select your Id and get to know how you have performed overall and in what level.")
print("")
print("trl_123")
print("trl_987")
print("trl_abc")
print("trl_imb")
print("trl_mda")
print("trl_mno")
print("trl_rst")
print("trl_xsl")
print("trl_xyz")
print("trl_zet")
print("trl_zny")
print("I want to see everyone's performance")
print("")

ID = input("Please enter your Id :-")

df = pd.read_csv("data.csv")

if(ID == "I want to see everyone's performance"):

    

    mean = df.groupby(["student_id", "level"], as_index= False)["attempt"].mean()

    fig = px.scatter(mean, x = "student_id" , y = "level", size = 'attempt', color = 'attempt')
    fig.show()

if(ID == "trl_123"):

    student_df = df.loc[df['student_id'] == 'TRL_123']

    print(student_df.groupby("level")["attempt"].mean())

    fig = pg.Figure(pg.Bar(x = student_df.groupby("level")["attempt"].mean(), y = ['level1', 'level2', 'level3', 'level4'], orientation = 'h'))
    fig.show()

if(ID == "trl_987"):

    student_df = df.loc[df['student_id'] == 'TRL_987']

    print(student_df.groupby("level")["attempt"].mean())

    fig = pg.Figure(pg.Bar(x = student_df.groupby("level")["attempt"].mean(), y = ['level1', 'level2', 'level3', 'level4'], orientation = 'h'))
    fig.show()

if(ID == "trl_abc"):

    student_df = df.loc[df['student_id'] == 'TRL_abc']

    print(student_df.groupby("level")["attempt"].mean())

    fig = pg.Figure(pg.Bar(x = student_df.groupby("level")["attempt"].mean(), y = ['level1', 'level2', 'level3', 'level4'], orientation = 'h'))
    fig.show()

if(ID == "trl_imb"):

    student_df = df.loc[df['student_id'] == 'TRL_imb']

    print(student_df.groupby("level")["attempt"].mean())

    fig = pg.Figure(pg.Bar(x = student_df.groupby("level")["attempt"].mean(), y = ['level1', 'level2', 'level3', 'level4'], orientation = 'h'))
    fig.show()

if(ID == "trl_mda"):

    student_df = df.loc[df['student_id'] == 'TRL_mda']

    print(student_df.groupby("level")["attempt"].mean())

    fig = pg.Figure(pg.Bar(x = student_df.groupby("level")["attempt"].mean(), y = ['level1', 'level2', 'level3', 'level4'], orientation = 'h'))
    fig.show()

if(ID == "trl_mno"):

    student_df = df.loc[df['student_id'] == 'TRL_mno']

    print(student_df.groupby("level")["attempt"].mean())

    fig = pg.Figure(pg.Bar(x = student_df.groupby("level")["attempt"].mean(), y = ['level1', 'level2', 'level3', 'level4'], orientation = 'h'))
    fig.show()

if(ID == "trl_rst"):

    student_df = df.loc[df['student_id'] == 'TRL_rst']

    print(student_df.groupby("level")["attempt"].mean())

    fig = pg.Figure(pg.Bar(x = student_df.groupby("level")["attempt"].mean(), y = ['level1', 'level2', 'level3', 'level4'], orientation = 'h'))
    fig.show()

if(ID == "trl_xsl"):

    student_df = df.loc[df['student_id'] == 'TRL_xsl']

    print(student_df.groupby("level")["attempt"].mean())

    fig = pg.Figure(pg.Bar(x = student_df.groupby("level")["attempt"].mean(), y = ['level1', 'level2', 'level3', 'level4'], orientation = 'h'))
    fig.show()

if(ID == "trl_xyz"):

    student_df = df.loc[df['student_id'] == 'TRL_xyz']

    print(student_df.groupby("level")["attempt"].mean())

    fig = pg.Figure(pg.Bar(x = student_df.groupby("level")["attempt"].mean(), y = ['level1', 'level2', 'level3', 'level4'], orientation = 'h'))
    fig.show()

if(ID == "trl_zet"):

    student_df = df.loc[df['student_id'] == 'TRL_zet']

    print(student_df.groupby("level")["attempt"].mean())

    fig = pg.Figure(pg.Bar(x = student_df.groupby("level")["attempt"].mean(), y = ['level1', 'level2', 'level3', 'level4'], orientation = 'h'))
    fig.show()

if(ID == "trl_zny"):

    student_df = df.loc[df['student_id'] == 'TRL_zny']

    print(student_df.groupby("level")["attempt"].mean())

    fig = pg.Figure(pg.Bar(x = student_df.groupby("level")["attempt"].mean(), y = ['level1', 'level2', 'level3', 'level4'], orientation = 'h'))
    fig.show()

print("")
print("Thanks for using Mathly. Hope you have understood your performance levels.")
print("")