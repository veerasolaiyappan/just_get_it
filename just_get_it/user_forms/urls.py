from django.urls import path,include
from . import views

urlpatterns = [

    path('form/',views.form,name="form"),
    path('table/',views.table,name="table")
    
]
