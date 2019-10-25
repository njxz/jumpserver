# coding:utf-8
#

from __future__ import absolute_import

from django.urls import path, include

from .. import views

app_name = 'authentication'

urlpatterns = [
    # openid
    path('openid/', include(('authentication.backends.openid.urls', 'authentication'), namespace='openid')),

    # login
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('login/otp/', views.UserLoginOtpView.as_view(), name='login-otp'),
    path('login/continue/', views.UserLoginContinueView.as_view(), name='login-continue'),
    path('login/wait/', views.UserLoginWaitConfirmView.as_view(), name='login-wait'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]
