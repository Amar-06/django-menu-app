from django.urls import path
from . import views
app_name='food'
urlpatterns=[path('amar',views.my_Intro,name='my_Intro'),
             path('',views.item,name='item'),
             path('menu/',views.Food_List,name='Food_List'),
             path('add/',views.add_food,name='add_food'),
             path('update/<str:dish>',views.update_food,name='update_food'),
             path('delete/<str:dish>',views.delete_food,name='delete_food'),
             path('<str:dish>',views.Food_details,name='Food_details'),
             
             ]