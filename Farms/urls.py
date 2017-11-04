from django.conf.urls import url
from Farms import views

urlpatterns = [
    url(r'^Farms/(?P<name>[a-z]+)/$', views.send_table_data),
]