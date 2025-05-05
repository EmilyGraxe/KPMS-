from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.enter_user_id, name='enter_user_id'),  # Home page URL
    path('login/password/', views.enter_passcode, name='enter_passcode'),  # Password page URL
    # path('dashboard_redirect/', views.dashboard_redirect, name='dashboard_redirect'),  # Dashboard redirect URL

    # path('logout/', views.custom_logout, name='logout'),  # logout page URL
    path('dashboard/', views.homepage, name='homepage'),  # Dashboard URL
    # path('manager/dashboard/', views.manager_dashboard, name='manager_dashboard'),  # Manager dashboard URL
    # path('attendant/dashboard/', views.attendant_dashboard, name='attendant_dashboard'),  # Attendant dashboard URL
    # path('director_dashboard/', views.director_dashboard, name='director_dashboard'),  # Director dashboard URL
    path('trusted/customer/', views.registerTrustedCustomer, name='trusted_customer'),
    path('trusted/list/', views.trustedCustomer_list, name='trusted_customer_list'),
     path('basic/', include('BasicSystem.urls')),  # Include URLs from the basic app
    path('sales/', include(('sales.urls', 'sales'),namespace='sales')),
    path('logout/',views.logout_view, name='logout'),
    # path('pin/', views.custom_pin, name='custom_pin'),  # Custom ID page URL
    
]