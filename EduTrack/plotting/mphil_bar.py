import csv
import plotly.graph_objects as go

with open('StateWise_Enrollment1.csv') as file:
    csvfile = csv.reader(file)
    M = []
    header = next(csvfile)
    next(csvfile)
    state_names = []
    for row in csvfile:
        M.append(row[:-1])
        state_names.append(row[1])

# state_names = [item for item in state_names if item != '']

male_phd = list(map(lambda r: int(r[5]) if r[5] != '' else 0, M))
female_phd = list(map(lambda r: int(r[6]) if r[6] != '' else 0, M))

male_phd = male_phd[:-1]
female_phd = female_phd[:-1]
state_names = state_names[:-1]

# Create traces with different order for stacking
trace1 = go.Bar(x=state_names, y=male_phd, name='Male', marker=dict(color='blue'))
trace2 = go.Bar(x=state_names, y=female_phd, name='Female', marker=dict(color='pink'))

# Create the layout for the plot
layout = go.Layout(barmode='stack', title='Enrollment of male and female in M.Phil')

# Create the figure and add the traces
fig = go.Figure(data=[trace2, trace1], layout=layout)

# Show the plot
fig.show()