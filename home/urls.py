from django.urls import path
from home.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name="home"),
    path('patient_login', plogin, name='plogin'),
    path('doctor_login', dlogin, name='dlogin'),
    path('signup', signup, name='signup'),
    path('logout', Logout, name="logout"),
    path('search', search, name="search"),
    path('bookapp', bookapp, name="bookapp"),
    path('dashboard', dashboard, name='dashboard'),
    path('change-password/<token>/', change_password, name="change-password"),
    path('forgot_pass', forgot_pass, name="forgot_pass"),
    path('bookAppointment/<username>', bookapp, name='bookAppointment')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
