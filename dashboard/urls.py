from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('eis', views.connectsql, name='omega-eis'),
    path('member', views.sb_member, name='sb-member'),
    path('sms', views.sms, name="sms"),
]