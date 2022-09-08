from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import base64
from io import BytesIO


# Hari Jumat 
def getfriday(tanggal):
    getdate = datetime.strptime(tanggal, '%Y-%m-%d')
    getday = getdate.strftime('%A')
    if getday == 'Saturday':
        deltafriday = getdate + timedelta(days=-1)
        return deltafriday.date()
    if getday == 'Sunday':
        deltafriday = getdate + timedelta(days=-2)
        return deltafriday.date()
    if getday == 'Monday':
        deltafriday = getdate + timedelta(days=-3)
        return deltafriday.date()
    if getday == 'Tuesday':
        deltafriday = getdate + timedelta(days=-4)
        return deltafriday.date()
    if getday == 'Wednesday':
        deltafriday = getdate + timedelta(days=-5)
        return deltafriday.date()
    if getday == 'Thursday':
        deltafriday = getdate + timedelta(days=-6)
        return deltafriday.date()
    if getday == 'Friday':
        deltafriday = getdate + timedelta(days=0)
        return deltafriday.date()


# Get Graph 
def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    img_png = buffer.getvalue()
    graph = base64.b64encode(img_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

# Get Plot 
def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    # plt.title('Grafik Data Beban Feeder')
    plt.plot(x,y)
    plt.xlabel('Jam')
    plt.ylabel('Total Beban')
    plt.xticks(rotation=45)
    plt.tight_layout()
    graph = get_graph()
    return graph