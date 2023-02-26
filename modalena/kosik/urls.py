from django.urls import path
from . import views

app_name = 'kosik'

urlpatterns = [
    path('',views.kosik_shrnuti,name = 'kosik_shrnuti'),
    path('pridat/',views.kosik_pridat,name='kosik_pridat')
]