from django.urls import path
from basic_app import views

app_name='basic_app'

urlpatterns = [
    path('others/',views.other,name='other'),
    path('relative/',views.relative,name='relative'),

]