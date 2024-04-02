from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('userlogin/', views.UserLogin, name='userlogin'),
    path('userlogout/', views.UserLogout, name='userlogout'),
    path('userregister/', views.UserRegister, name='userregister'),
    path('booking/', views.UserBookings, name='bookings'),
    path('userbooks/', views.UserBooks, name='userbooks'),
    path('feedback/', views.Feedbacks, name='feedback'),
    path('query/', views.Query, name='query'),


    # Admin Routes (Nandita)
    path('dash/', views.Dashboard, name='dashboard'),
    path('dashfeedback/', views.Dashfeedback, name='dashfeedback'),
    path('dashenquiry/', views.Dashenquiry, name='dashenquiry'),
    path('dashpackage/', views.DashPackage, name='dashpackage'),
    path('dashpackageedit/<str:pk>/', views.DashPackageEdit, name='dashpackageedit'),
    path('dashpackagedelete/<str:pk>/', views.DashPackageDelete, name='dashpackagedelete'),

]