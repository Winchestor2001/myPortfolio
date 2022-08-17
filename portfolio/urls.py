from django.urls import path

from portfolio.views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('detail/<int:pk>/', detail_page, name='detail'),
    path('send_mail/', contact, name='send_mail'),
]