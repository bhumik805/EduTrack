import pandas as pd
import numpy as np
import plotly.express as px
import csv


with open('StateWise_Enrollment2.csv', 'r') as file:
    csv_reader = csv.reader(file)

    l=[]
    i=0
    for row in csv_reader:
        i+=1
        if(i>2 and i<39):
            l.append(row)
states=[]
male=[]
female=[]
phd_total=[]
for row in l:
    states.append(row[1])
    male.append(row[2])
    female.append(row[3])

data = {'State': states,
        'Male': male,
        'Female': female,
        }

df = pd.DataFrame(data)

df_melted = pd.melt(df, id_vars=['State'], var_name='Category', value_name='Value')

fig = px.sunburst(df_melted, path=['State', 'Category'], values='Value',
                  title='Nested Pie Chart: Education Level by Gender and State in Under graduate')

# Show the chart
fig.show()
