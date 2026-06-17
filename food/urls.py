from django.urls import path
from . import views
app_name='food'
urlpatterns=[path('amar',views.my_Intro,name='my_Intro'),
             path('',views.item,name='item'),
             path('menu/',views.Food_List,name='Food_List'),
             path('<str:dish>',views.Food_details,name='Food_details'),
             ]