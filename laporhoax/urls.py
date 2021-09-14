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
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token

from accounts.api.views import registrationView, activate, isActive, verifyOTP
from reports.api.views import category_list, post_report, report_list
from feeds.api.views import post_feed, getHeaderFeed, getFeed

from accounts.views import testGoogleAuth #test only

urlpatterns = [
    path('',testGoogleAuth),
    path('admin/', admin.site.urls),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('api/register/', registrationView, name="api-register"), #ok
    path('api/login/',obtain_auth_token,name="api-login"), #ok
    path('api/isactive/', isActive, name= "api-isactive"), #ok
    path('api/verifyotp/', verifyOTP, name= "api-verifyotp"), #ok
    path('api/getcategory/', category_list, name= "api-getcategory"), #ok
    path('api/postreport/', post_report, name= "api-postreport"),
    path('api/getreport/', report_list, name= "api-getreport"),
    path('api/postfeed/', post_feed, name= "api-postfeed"),
    path('api/getfeed/', getHeaderFeed, name= "api-getfeed"),
    path('api/getfeed/<pk>', getFeed, name= "api-getfeed-pk"),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/allauth/', include('allauth.urls')), #test
]
