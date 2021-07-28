import csv 
import pandas as pd
import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv("grp-1.csv")
data=df["Math_score"].to_list()


mean=statistics.mean(data)
stdDev=statistics.stdev(data)
print("mean of the population:",mean)
print("standard deviation of the population:",stdDev)


fig=ff.create_distplot([data],["maths score"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
#fig.add_trace(go.Scatter(x=[mean_of_sample2, mean_of_sample2], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO HAD EXTRA CLASSES"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.show()

