from django.urls import path

from . import views

urlpatterns = [
    path('t1', views.index, name='index2'),
    path('t2', views.index3, name='index3'),
    path('form1/', views.DefaultFormByFieldView.as_view(), name="form_Example")
]