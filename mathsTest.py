import csv 
import pandas as pd
import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv("mathsTest-1.csv")
data=df["Math_score"].to_list()

#fig=ff.create_distplot([data],["maths score"],show_hist=False)
#fig.show()

meanOfpopulation=statistics.mean(data)
stdDev=statistics.stdev(data)
print("mean of the population:",meanOfpopulation)
print("standard deviation of the population:",stdDev)

def randomMean(counter):
    dataSet=[]
    for i in range (0,counter):
        randIndex=random.randint(0,len(data)-1)
        value=data[randIndex]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return mean

def showFig(meanList):
    df=meanList
    meanOfdf=statistics.mean(df)
    fig=ff.create_distplot([df],["mathScore"],show_hist=False)
    fig.add_trace(go.Scatter(x=[meanOfdf,meanOfdf],y=[0,1],mode="lines",name="mean"))
    fig.show()

def setup():
    meanList=[]
    for i in range(0,1000):
        set_of_means=randomMean(100)
        meanList.append(set_of_means)
    showFig(meanList)
    mean=statistics.mean(meanList)
    stdDev1=statistics.stdev(meanList)
    print("mean of sampling distribution", mean)
    print(" standard deviation of sampling distribution :", stdDev1)

setup()

FirstStart,FirstEnd= meanOfpopulation-stdDev,meanOfpopulation+stdDev
SecondStart,SecondEnd=meanOfpopulation-(2*stdDev),meanOfpopulation+(2*stdDev)
ThirdStart,ThirdEnd= meanOfpopulation-(3*stdDev),meanOfpopulation+(3*stdDev)
listOf1stStdDev=[result for result in data if result>FirstStart and result<FirstEnd]
listOf2ndStdDev=[result for result in data if result>SecondStart and result<SecondEnd]
listOf3rdStdDev=[result for result in data if result>ThirdStart and result<ThirdEnd]

print("{}% of data lies within 1 standard deviation".format(len(listOf1stStdDev)*100.0/len(data)))
print("{}% of data lies within 2 standard deviation".format(len(listOf2ndStdDev)*100.0/len(data)))
print("{}% of data lies within 3 standard deviation".format(len(listOf3rdStdDev)*100.0/len(data)))

df=pd.read_csv("grp-1.csv")
data=df["Math_score"].to_list()

meanOfSample=statistics.mean(data)
stdDev=statistics.stdev(data)
print("mean of the population:",meanOfSample)
print("standard deviation of the population:",stdDev)

fig=ff.create_distplot([data],["maths score"],show_hist=False)
fig.add_trace(go.Scatter(x=[meanOfpopulation, meanOfpopulation], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[meanOfSample, meanOfSample], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO HAD EXTRA CLASSES"))
fig.add_trace(go.Scatter(x=[FirstEnd , FirstEnd], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[SecondEnd, SecondEnd], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.show()

zScore=(meanOfSample-mean)/stdDev
print(zScore)