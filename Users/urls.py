from django.urls import include, re_path
from Users import views

urlpatterns =  [
    re_path(r'^userdetails/$',views.userdetailsApi),
    re_path(r'^userdetails/([0-9]+)$',views.userdetailsApi)
]