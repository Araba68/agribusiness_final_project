# portal/urls.py
from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from .views import farmer_dashboard, contact_admin, access_finances
from .views import update_farmer_profile, update_buyer_profile
from django.views.generic import TemplateView
#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    path('signin/', views.signin, name='signin'),  # Sign In page URL
      path('signup_buyer/', views.signup_buyer, name='signup_buyer'),
    path('signup_farmer/', views.signup_farmer, name='signup_farmer'),
    path('buyer_dashboard/', views.buyer_dashboard, name='buyer_dashboard'),
    path('farmer_dashboard/', views.farmer_dashboard, name='farmer_dashboard'),
     path('update_buyer_profile/', views.update_buyer_profile, name='update_buyer_profile'),
      path('update_farmer_profile/', views.update_farmer_profile, name='update_farmer_profile'),
       path('logout/', LogoutView.as_view(next_page='signin'), name='logout'),  # Update this line
        path('contact_admin/', contact_admin, name='contact_admin'),
    path('access_finances/', access_finances, name='access_finances'),
     
   path('error/', TemplateView.as_view(template_name='portal/error.html'), name='error')
      

]