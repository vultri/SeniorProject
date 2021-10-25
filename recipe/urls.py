from django.urls import path
from . import views

urlpatterns = [
    path('browse_recipes/', views.browse_recipes, name = 'recipe-browse_recipes'),
    path('view_recipes/', views.view_recipe, name = 'recipe-view_recipe'),
]