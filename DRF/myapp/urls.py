
from django.urls import path , include
from . import views
urlpatterns = [
    path('',views.drinklist,name='list'),
    path('drink/<int:id>',views.get_drink,name="getdrink")
]
   