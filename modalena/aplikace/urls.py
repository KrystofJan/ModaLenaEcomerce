from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('',views.index,name='index'),
    path('vsechny_produkty',views.all_product,name='vsechny_produkty'),
    path('produkt/<int:id>',views.produkt_detail,name='produkt_detail')
]