from .kosik import Kosik

def kosik(request):
    return {'kosik': Kosik(request)}