"""
URL configuration for pybank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from pybank.account import views as account_views
from pybank.user import views as user_views

router = routers.DefaultRouter()
router.register(r"users", user_views.UserViewSet)
router.register(r"groups", user_views.GroupViewSet)
router.register(r"accounts", account_views.AccountViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("admin/", admin.site.urls),
]
