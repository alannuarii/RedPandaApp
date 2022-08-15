from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
import pandas as pd
from sqlalchemy import create_engine


# Create Engine 
engine = create_engine('sqlite:///redpandadb.db')


# HALAMAN HOME 
def home(request):
    # print(dir(request))
    context={
        'title':'Home | RedPAnda',
        }
    return render(request, 'pages/home.html', context)


# HALAMAN FORECAST FEEDER
def forecast_feeder(request):

    context={
        'title':'Forecast Feeder | RedPanda',
        }
    return render(request, 'pages/feeder/forecast.html', context)


# HALAMAN DATA FEEDER
def data_feeder(request):
    
    if request.method == 'POST':
        try:
            feeder = request.FILES['feeder']
            if not feeder.name.endswith('xlsx'):
                messages.warning(request, 'Format file harus .xlsx')
                return redirect('/feeder/data')
            data_excel = pd.read_excel(feeder)
            data_excel.to_sql(name='redpanda_feeder', con=engine, if_exists='append', index=False)
        except Exception as error:
            print(error)
    
    context={
        'title':'Data Feeder | RedPanda',
        }
    return render(request, 'pages/feeder/data.html', context)
