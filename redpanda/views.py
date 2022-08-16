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
    
    feeder_sql = pd.read_sql('redpanda_feeder', con=engine).iloc[0:24,2:]
    total = feeder_sql.iloc[0:24,1:16].sum(axis=1)
    pltd_tahuna = feeder_sql.iloc[0:24,1:7].sum(axis=1)
    pltd_petta = feeder_sql.iloc[0:24,7:11].sum(axis=1)
    pltd_tamako = feeder_sql.iloc[0:24,11:15].sum(axis=1)
    pltd_lesabe  = feeder_sql.iloc[0:24,15:19].sum(axis=1)
    feeder_sql.insert(7,'Sub Total Tahuna',pltd_tahuna)
    feeder_sql.insert(12,'Sub Total Petta',pltd_petta)
    feeder_sql.insert(16,'Sub Total Tamako',pltd_tamako)
    feeder_sql.insert(20,'Sub Total Lesabe',pltd_lesabe)
    feeder_sql.insert(21,'Total',total)

    context={
        'title':'Data Feeder | RedPanda',
        'rows':list(feeder_sql.values.tolist()),
        }
    return render(request, 'pages/feeder/data.html', context)
