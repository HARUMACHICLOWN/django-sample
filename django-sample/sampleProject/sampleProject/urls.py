from django.urls import path
from Sample import views

urlpatterns = [
    path("", views.index),
    path("about/", views.about),
    path("contact/", views.contact),
    path('form/', views.form)
]
