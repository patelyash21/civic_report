from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_views, name='register'),
    path('home/', views.home, name='home'),
    path('map/', views.map_view, name='map'),
    path('reports/', views.report_list, name='report_list'),
    path('login/', views.login_view, name='login'),
    path('create-report/', views.create_report, name='create'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('notifications/', views.notification, name='notification'),
    path('profile/', views.user_profile, name='profile'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('register/', views.register_views, name='register'),
    path('report/<int:report_id>/', views.report_detail, name='report_detail'),
]