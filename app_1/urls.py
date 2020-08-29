from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('home',views.interface_list,name='home'),
    path('add_interface/',views.add_interface,name='add_interface'),
    path('approve/',views.approve,name='approve'),
    path('assign/',views.assign,name='assign'),
    path('modify/<int:modify_pk>',views.modify,name='modify'),
    path('logout/', auth_views.LogoutView.as_view(), name='logoutuser'),
    path('interface_detail/<int:num>',views.interface_detail,name='interface_detail'),
    path('detail/<int:pk>',views.detail,name='detail'),
    path('detail_modify/<int:detail_modify>',views.detail_modify,name='detail_modify'),
    path('interface_filter',views.filter_interface,name='interface_filter'),
    path('field_detail/<int:interface_detail>',views.field_detail,name='field_detail'),
]

# path('logoutuser',views.logout,name='logoutuser'),