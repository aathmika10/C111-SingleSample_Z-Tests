import csv 
import pandas as pd
import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv("grp-3.csv")
data=df["Math_score"].to_list()

fig=ff.create_distplot([data],["maths score"],show_hist=False)
fig.show()

meanOfpopulation=statistics.mean(data)
stdDev=statistics.stdev(data)
print("mean of the population:",meanOfpopulation)
print("standard deviation of the population:",stdDev)

