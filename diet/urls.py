from django.urls import path
from .views import IngList, IngDetail
urlpatterns = [
    path('', IngList.as_view(), name='list'),
    path('<int:pk>/', IngDetail.as_view(), name='ing'),
]