'''from django.urls import path
from . import views
app_name='food'
urlpatterns=[path('amar',views.my_Intro,name='my_Intro'),
            # path('',views.item,name='item'),
             path('menu/',views.Food_List,name='Food_List'),
             path('<str:dish>',views.FoodDetail_classview.as_view(),name='FoodDetail_classview'),
             path('',views.FoodList_classview.as_view(),name='FoodList_classview'),
             path('add/',views.add_food,name='add_food'),
             path('update/<str:dish>',views.update_food,name='update_food'),
             path('delete/<str:dish>',views.delete_food,name='delete_food'),
             path('<str:dish>',views.Food_details,name='Food_details'),
             
             ]'''
from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [

    # List all food items
    path('', views.FoodList_classview.as_view(),
         name='Food_List'),

    # Detail page
    path('<int:pk>/',
         views.FoodDetail_classview.as_view(),
         name='Food_Detail'),

    # Add new food
    path('add/',
         views.FoodCreateView.as_view(),
         name='add_food'),

    # Update food
    path('update/<int:pk>/',
         views.update_food,
         name='update_food'),

    # Delete food
    path('delete/<int:pk>/',
         views.delete_food,
         name='delete_food'),
]