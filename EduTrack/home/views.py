from django.shortcuts import render
from django.template.context_processors import csrf
from .models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import csv
import plotly.graph_objects as go
import plotly.express as px
import plotly
import os
import pandas as pd

def home(request):
    return render(request,"home/home.html",{})

def login(request):
    return render(request,'home/login.html',{})

def validate(request):
    if(request.method=='POST'):
        username = request.POST.get('username','')
        password = request.POST.get('pass','')
        if(username is not None and password is not None):
            # flag1 = False
            # flag2 = False
            try:
                u = User.objects.get(username = username)
            except:
                messages.error(request,"Invalid Username")
                return render(request,'home/login.html') 

            if(u.password == password):
                request.session['username'] = username
                # request.session['password'] = password
                uname={
                    "username":username
                }      
                return render(request,'home/visualize.html', uname)
            else:
                messages.error(request,"Invalid Password")
                return render(request,'home/login.html')    
        else:
            messages.success(request,'Credentials cannot be empty')
            return render(request,'home/login.html')
    
    elif(request.method == "GET"):
        if(request.session.get('username',False)):
            username = request.session.get('username',False)
            uname={
                    "username":username
            }     
            return render(request,'home/login.html', uname)    
    
    else:
        return render(request,'home/login.html')

def register(request):
    return render(request,"home/registration.html",{})


def add_user(request):
    if(request.method=='POST'):
        username = request.POST.get('username','')
        password = request.POST.get('password','')
    u = User()
    u.username = username
    u.password = password
    u.save()
    return render(request,"home/login.html",{})


def plot(request,p1,p2):

    if(request.session.get('username',False)):
        username = request.session.get('username',False)
        uname={
                    "username":username
            }

        if p1=='phd' or p1=='mphil' or p1=='pg':
            fi='StateWise_Enrollment1.csv'
        else: 
            fi='StateWise_Enrollment2.csv'

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_file_path = os.path.join(base_dir, 'assets', fi)

        if p1=='phd' or p1=='ug':
            c1,c2=2,3
        if p1=='mphil' or p1=='pgdi':
            c1,c2=5,6
        if p1=='pg' or p1=='di':
            c1,c2=8,9


        with open(csv_file_path) as file:
            csvfile = csv.reader(file)
            M = []
            header = next(csvfile)
            next(csvfile)
            state_names = []
            for row in csvfile:
                M.append(row[:-1])
                state_names.append(row[1])
        
        male = list(map(lambda r: int(r[c1]) if r[c1] != '' else 0, M))
        female = list(map(lambda r: int(r[c2]) if r[c2] != '' else 0, M))

        male = male[:-1]
        female = female[:-1]
        state_names = state_names[:-1]
        
        if p2=='0':
            trace1 = go.Bar(x=state_names, y=male, name='Male', marker=dict(color='blue'))
            trace2 = go.Bar(x=state_names, y=female, name='Female', marker=dict(color='pink'))
            layout = go.Layout(barmode='stack', title=f'Enrollment of male and female',height=900,  width=1200)
            fig = go.Figure(data=[trace2, trace1], layout=layout)
            # fig.show()
            t=plotly.offline.plot(fig,auto_open=False,output_type='div')

        else:
            data = {'State':state_names ,
                'Male': male,
                'Female': female,
            }

            df = pd.DataFrame(data)

            df_melted = pd.melt(df, id_vars=['State'], var_name='Category', value_name='Value')

            # Create a nested pie chart
            fig = px.sunburst(df_melted, path=['State', 'Category'], values='Value',
                            title=f'Nested Pie Chart: Education Level by Gender and State',height=900,width=1200)

            # fig.show()
            t=plotly.offline.plot(fig,auto_open=False,output_type='div')
        

        return render(request,"home/showplot.html",{'t':t,'username':username})
    else:
        messages.info(request,"Login Required")
        return render(request,'home/login.html')


def ret(request):
    if(request.session.get('username',False)):
        username = request.session.get('username',False)
        uname={
                    "username":username
            }
        return render(request,"home/visualize.html",{})
    else:
        messages.info(request,"Login Required")
        return render(request,'home/login.html')


def logout(request):
    request.session.flush()
    messages.success(request,'logout successful')
    return render(request,"home/home.html",{})