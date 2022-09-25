from django.urls import path
from .views import MealDetail, MealsList


urlpatterns = [
    path('', MealsList.as_view(), name='meals'),
    path('<int:pk>/', MealDetail.as_view(), name='meal')
]