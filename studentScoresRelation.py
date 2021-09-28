import pandas as pd
import plotly_express as px
import numpy as np

def plotFigure(df,col_x,col_y):
    fig = px.scatter(df,x=col_x,y=col_y)
    fig.show()

def findCorrelation(df, col_x, col_y):
    list_x = df[col_x].tolist()
    list_y = df[col_y].tolist()
    correlation = np.corrcoef(list_x, list_y)
    if(round(correlation[0,1])==1): 
        print(f'{col_x} and {col_y} are Directly Proportional')
    elif(round(correlation[0,1])==-1):
        print(f'{col_x} and {col_y} are Inversely Proportional')
    else:
        print(f'{col_x} and {col_y} are Not Related')

def getDataRelation():
    df = pd.read_csv('marks_Attendance.csv')
    col_x = 'Days Present'
    col_y = 'Marks In Percentage'
    findCorrelation(df, col_x, col_y)
    plotFigure(df,col_x,col_y)

getDataRelation()