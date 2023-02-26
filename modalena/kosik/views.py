from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .kosik import Kosik
from aplikace.models import Produkt
from django.http import JsonResponse
# Create your views here.
def kosik_shrnuti(request):
    return render(request,'aplikace/kosik/summary.html')

def kosik_pridat(request):
    kosik = Kosik(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        produkt = get_object_or_404(Produkt, produkt_id = product_id)
        kosik.add(product = produkt)
        response = JsonResponse({'test':'data'})
        return response