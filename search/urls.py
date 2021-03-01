# path関数import
from django.urls import path

# ここからviewsに処理を飛ばすので
# viewsもimport
from . import views

app_name = 'search'

urlpatterns = [
    # pathが一致したらそれぞれのviewに処理を投げる
    path('', views.IndexView.as_view(), name="index"),
]