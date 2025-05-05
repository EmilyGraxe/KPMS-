from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('pos/', views.pos_view, name='pos'),
    path('receipt/<int:sale_id>/', views.receipt_pdf_view, name='receipt_pdf'),
    path('report/', views.sales_report_view, name='sales_report'),
    path('mark_as_paid/<int:sale_id>/', views.mark_sale_as_paid, name='markAspaid'),
    path('credit_sales_list/', views.credit_sales_list, name='credit_sales_list'),
   
   
]