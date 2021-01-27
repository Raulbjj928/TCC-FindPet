"""fpet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings
from django.conf.urls import include, url
from users.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^register/", register, name="register"),
    path('pet/user/', views.list_user_pets),
    path('pet/all/', views.list_all_pets, name="all"),
    path('pet/detail/<slug:id>/', views.pet_detail),
    path('pet/register/', views.register_pet),
    path('pet/register/submit', views.set_pet),
    path('pet/delete/<slug:id>/', views.delete_pet),
    path('logout/', views.logout_user),
    path('', RedirectView.as_view(url='pet/all/')),
    path('pet/euvi/', views.euvi_pet),
    path('pet/euvi/submit', views.set_euvi),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
