from django.urls import path
from Main import views

app_name = 'Main'
urlpatterns = [
    path('dynamicmenu/', views.dynamicmenu, name='dynamicmenu'),
#    path('MotorModify/', views.MotorModify, name='MotorModify'),
#    path('MotorEditData/<int:data_id>/', views.MotorEditData, name='MotorEditData'),
#    path('datatables/', views.datatables, name='datatables'),    
#    path('datatables/getSomething', views.getSomething, name='getSomething'),
]