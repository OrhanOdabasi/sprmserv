from datetime import date
import random
import string


def requestNumberGen(u):
    # request number generator // last 6 digit
    talep_no = ""
    for _ in range(u):
        talep_no += (random.choice(string.digits))
    return talep_no


def createRequetNo(instance):
    # creates full request number with date information
    talep_no = requestNumberGen(6)
    klass = instance.__class__
    request_exists = klass.objects.filter(talep_no=talep_no)
    if request_exists:
        return createRequetNo()
    else:
        now = date.today()
        return f"{now.day}{now.month}{str(now.year)[-2:]}{talep_no}"
