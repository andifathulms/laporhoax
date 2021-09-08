"""laporhoax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from rest_framework.authtoken.views import obtain_auth_token

from accounts.api.views import registrationView, activate
from reports.api.views import category_list, post_report, report_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('api/register/', registrationView, name="api-register"),
    path('api/login/',obtain_auth_token,name="api-login"),
    path('api/getcategory/', category_list, name= "api-getcategory"),
    path('api/postreport/', post_report, name= "api-postreport"),
    path('api/getreport/', report_list, name= "api-getreport"),
]
