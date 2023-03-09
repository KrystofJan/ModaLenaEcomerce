from django.shortcuts import render,get_object_or_404
from .models import Adresa,Zakaznik,ZakazikAccount,Produkt,Kategorie, Objednavka, ObjednavkaProdukt,Dorucovatel,Zakaznik, Kosik, KosikProdukt
from .forms import AdresaForm,ZakaznikForm,LogInForm,ProduktForm
# Create your views here.


def index(request):

    return render(request,'aplikace\index.html')

def all_product(request):
    produkt = Produkt.products.all()

    return render(request,'aplikace\store.html',{'produkty': produkt})

def produkt_detail(request,id):
    product = get_object_or_404(Produkt,produkt_id=id)
    if request.method == 'POST':
        kosik = Kosik(zakaznik = Zakaznik.objects.get(kosik_id = 12))
        kosik.save()
        kosik_produkt = KosikProdukt(kosik = kosik, produkt= product)
        kosik_produkt.save()
         
    return render(request,'aplikace\produkty\detail.html',{'produkt':product})

 
def logIn(request):
    if request.method == 'POST':
        logInForm = LogInForm(request.POST)
        if logInForm.is_valid():
            uzivatelske_jmeno_b = logInForm.cleaned_data['uzivatelske_jmeno']
            heslo_b = logInForm.cleaned_data['heslo']
            zakaznikacc = ZakazikAccount.objects.all()
            
            for i in zakaznikacc:
                if zakaznikacc.uzivazelske_jmeno == uzivatelske_jmeno_b:
                    zakacc= i
            if heslo_b == zakacc.heslo:
                return(request,'aplikace/success.html')
            else:
                return(request,'aplikace/failed.html')
    logInForm = LogInForm()
    return render(request,'aplikace/signIn.html',{'logInForm': logInForm})