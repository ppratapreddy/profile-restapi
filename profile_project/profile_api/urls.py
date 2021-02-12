from django.urls import path
from . import views

app_name = 'profile_api'

urlpatterns=[
path('',views.indexView.as_view(),name='indexpage'),

]