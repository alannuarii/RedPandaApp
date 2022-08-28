from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from redpanda.models import Unit, Mesin, Har
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime, timedelta
from redpanda.utils import getfriday


# Create Engine 
engine = create_engine('sqlite:///redpandadb.db')


# HALAMAN SIGN-IN 
def sign_in(request):
    
    context={
        'title':'Sign In | RedPanda',
        }
    
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'pages/auth/sign-in.html', context)
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username atau password Anda salah')
            return redirect('/auth/sign-in')
    

# Fungsi Sign Out 
def sign_out(request):
    logout(request)
    return redirect('/auth/sign-in')


# HALAMAN HOME 
@login_required(login_url='sign_in')
def home(request):

    context={
        'title':'Home | RedPAnda',
        'active_home':'active'
        }
    return render(request, 'pages/home.html', context)


# HALAMAN FORECAST FEEDER
@login_required(login_url='sign_in')
def forecast_feeder(request):

    today = datetime.now()
    day7 = today + timedelta(days=-7)
    day14 = today + timedelta(days=-14)
    day21 = today + timedelta(days=-21)
    day28 = today + timedelta(days=-28)

    data1 = pd.read_sql_query("SELECT * FROM redpanda_feeder WHERE tanggal='{}'".format(day7.strftime('%Y-%m-%d')), con=engine).iloc[0:24,2:19]
    data2 = pd.read_sql_query("SELECT * FROM redpanda_feeder WHERE tanggal='{}'".format(day14.strftime('%Y-%m-%d')), con=engine).iloc[0:24,2:19]
    data3 = pd.read_sql_query("SELECT * FROM redpanda_feeder WHERE tanggal='{}'".format(day21.strftime('%Y-%m-%d')), con=engine).iloc[0:24,2:19]
    data4 = pd.read_sql_query("SELECT * FROM redpanda_feeder WHERE tanggal='{}'".format(day28.strftime('%Y-%m-%d')), con=engine).iloc[0:24,2:19]

    list_data = [data1,data2,data3,data4]
    data_concat = pd.concat(list_data,keys=range(len(list_data))).groupby(level=1)
    forecast = data_concat.max()

    total = forecast.iloc[0:24,1:16].sum(axis=1)
    pltd_tahuna = forecast.iloc[0:24,1:7].sum(axis=1)
    pltd_petta = forecast.iloc[0:24,7:11].sum(axis=1)
    pltd_tamako = forecast.iloc[0:24,11:15].sum(axis=1)
    pltd_lesabe  = forecast.iloc[0:24,15:19].sum(axis=1)
    forecast.insert(7,'Sub Total Tahuna',pltd_tahuna)
    forecast.insert(12,'Sub Total Petta',pltd_petta)
    forecast.insert(16,'Sub Total Tamako',pltd_tamako)
    forecast.insert(20,'Sub Total Lesabe',pltd_lesabe)
    forecast.insert(21,'Total',total)

    context={
        'title':'Forecast Feeder | RedPanda',
        'active_feeder':'active',
        'rows':list(forecast.values.tolist()),
        }
    return render(request, 'pages/feeder/forecast.html', context)


# HALAMAN DATA FEEDER
@login_required(login_url='sign_in')
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

    if 'tanggal' in request.GET:
        query = request.GET.get('tanggal')
        tanggal = datetime.strptime(query, '%Y-%m-%d')
    
        feeder_sql = pd.read_sql("SELECT * FROM redpanda_feeder WHERE tanggal='{}'".format(query), con=engine).iloc[0:24,2:]
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
        rows = list(feeder_sql.values.tolist())

    else:
        rows = None
        tanggal = None

    context={
        'title':'Data Feeder | RedPanda',
        'active_feeder':'active',
        'rows':rows,
        'tanggal':tanggal,
        }
    return render(request, 'pages/feeder/data.html', context)


# HALAMAN RENCANA PEMELIHARAAN
@login_required(login_url='sign_in')
def rencana_har(request):

    mesins = Mesin.objects.all()
    today = datetime.now().date()
    query = request.GET.get('tanggal')

    # Query Rencana Pemeliharaan Hari Ini 
    hars = Har.objects.filter(tanggal_jumat=getfriday(str(today)))
    
    if query:
        friday = datetime.strptime(query, '%Y-%m-%d')
        delta = friday + timedelta(days=+6)
        delta_friday = delta.date()

        # Query Rencana Pemeliharaan Tanggal Pilihan
        hars = Har.objects.filter(tanggal_jumat=getfriday(query))

        if request.method == 'POST':
            try:
                result = dict(request.POST.lists())
                for i in range(len(mesins)):
                    tanggal_jumat = result['tanggal_jumat'][0]
                    jumat = result['jumat'][i]
                    sabtu = result['sabtu'][i]
                    minggu = result['minggu'][i]
                    senin = result['senin'][i]
                    selasa = result['selasa'][i]
                    rabu = result['rabu'][i]
                    kamis = result['kamis'][i]
                    mesin_id = result['mesin_id'][i]
                    har = Har(tanggal_jumat=tanggal_jumat, jumat=jumat, sabtu=sabtu, minggu=minggu, senin=senin, selasa=selasa, rabu=rabu, kamis=kamis, mesin_id_id=mesin_id)
                    har.save()
            except Exception as error:
                print(error)

    else:
        friday = None
        delta_friday = None

    context={
        'title':'Rencana Pemeliharaan | RedPanda',
        'active_har':'active',
        'mesins':mesins,
        'friday':friday,
        'delta_friday':delta_friday,
        'hars':hars,
        }
    return render(request, 'pages/pemeliharaan/rencana.html', context)
