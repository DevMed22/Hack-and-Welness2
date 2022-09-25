from django.urls import path
from .views import AboutPageView , HomePageView, CheckList


urlpatterns = [
    path('about/',AboutPageView.as_view(),name='about'),
    path('',HomePageView.as_view(),name='home'),
    path('check/<int:pk>/', CheckList.as_view(), name='check')

]