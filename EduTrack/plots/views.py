from django.shortcuts import render
import pandas as pd
import numpy as np


def read_data(request):
    data = pd.read_csv('EduTrack/media/StateWise_Enrollment1.csv')
    print(data.head())   
    return render()
