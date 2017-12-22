from django.urls import path
from . import views

urlpatterns = [
    path('mycats/', views.MyCats, name='mycats'),
    path('addcat/', views.AddCat, name='addcat'),
    path('setupcat/', views.SetupCat, name='setupcat'),
    path('deletecat/', views.DeleteCat, name='deletecat'),
]