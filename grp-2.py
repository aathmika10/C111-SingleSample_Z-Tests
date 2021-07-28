import csv 
import pandas as pd
import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv("grp-2.csv")
data=df["Math_score"].to_list()

fig=ff.create_distplot([data],["maths score"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean_of_sample2, mean_of_sample2], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO HAD EXTRA CLASSES"))
fig.show()

meanOfpopulation=statistics.mean(data)
stdDev=statistics.stdev(data)
print("mean of the population:",meanOfpopulation)
print("standard deviation of the population:",stdDev)

