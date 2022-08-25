from datetime import datetime, timedelta

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