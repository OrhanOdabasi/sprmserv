from datetime import date
import random
import string

def serviceReportNumberGen(u):
    # service report number generator // last 6 digit
    rapor_no = ""
    for _ in range(u):
        rapor_no += (random.choice(string.digits))
    return rapor_no


def createReportNo(instance, central):
    # creates full request number with date information
    rapor_no = serviceReportNumberGen(6)
    klass = instance.__class__
    request_exists = klass.objects.filter(rapor_no=rapor_no)
    if request_exists:
        return createReportNo()
    else:
        now = date.today()
        return f"{str(central)}{rapor_no}{now.day}{now.month}{str(now.year)[-2:]}"
