from django.urls import path

from . import views

app_name = 'contents'

urlpatterns = [
    #contents/

    #path('<int:pk>/', views.ContentDetailView.as_view(), name='index'),
    path('<int:pk>/', views.IndexView.as_view(), name='index'),
]