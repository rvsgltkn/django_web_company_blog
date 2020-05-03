from django.urls import path

from . import views

urlpatterns=[
    path('lang/<lang>/<page>/', views.LangView.as_view(), name="lang"),
    path('',views.DefaultView.as_view(),name="default"),
    path('index',views.IndexView.as_view(),name="index"),
    path('about',views.AboutView.as_view(),name="about"),
    path('services', views.ServicesView.as_view(), name="services"),
    path('index_detail', views.IndexDetailView.as_view(), name="index_detail"),
    path('contact', views.ContactView.as_view(), name="contact"),

]