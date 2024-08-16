import pandas as pd
import numpy as np
import plotly.express as px
import csv

# df = pd.read_csv('StateWise_Enrollment1.csv')

# # Display the DataFrame
# print(df)

with open('StateWise_Enrollment1.csv', 'r') as file:
    csv_reader = csv.reader(file)

    # Read and print each row
    l=[]
    i=0
    for row in csv_reader:
        i+=1
        if(i>3 and i<39):
            l.append(row)
states=[]
phd_male=[]
phd_female=[]
phd_total=[]
for row in l:
    states.append(row[1])
    phd_male.append(row[2])
    phd_female.append(row[3])
    phd_total.append(row[4])
print(len(states))

data = {'State': states,
        'Male': phd_male,
        'Female': phd_female,
        }

df = pd.DataFrame(data)

# Melt the DataFrame to reshape it for Plotly Express
df_melted = pd.melt(df, id_vars=['State'], var_name='Category', value_name='Value')

# Create a nested pie chart
fig = px.sunburst(df_melted, path=['State', 'Category'], values='Value',
                  title='Nested Pie Chart: Education Level by Gender and State in Ph.D.')

# Show the chart
fig.show()
