'''
The following code analyzes the results of the genetic algorithm by plotting the trend of the performance of each
Tetris player generation.
'''

import plotly.plotly as py
import plotly.graph_objs as go

# load the text file containing the data to be analyzed
f = open("fitness_values.txt", 'r')
lines = f.readlines()
data = []
for i in range(0, 6):
    data.append(lines[i].split(", "))

# load the data into useable data structures
data = [[-float(j) for j in i] for i in data]
avg = [sum(i)/len(i) for i in data]
max = [max(i) for i in data]

x0 = []
for i in range(1, 7):
    x0 += [i] * len(data[0])
y0 = []
for i in range(0, 6):
    y0 += data[i]

# create traces
trace0 = go.Scatter(
    x = x0,
    y = y0,
    mode = 'markers',
    name = 'Fitness'
)
trace1 = go.Scatter(
    x = range(1, 7),
    y = avg,
    mode = 'lines+markers',
    name = 'Average Fitness'
)
trace2 = go.Scatter(
    x = range(1, 7),
    y = max,
    mode = 'lines+markers',
    name = 'Maximum Fitness'
)
data = [trace0, trace1, trace2]

# set layout
layout = go.Layout(
    title='Growth of Population Fitness',
    xaxis=dict(
        title='Generation',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Fitness',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='Fitness Growth')