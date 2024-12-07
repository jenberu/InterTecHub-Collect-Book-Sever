from django.urls import path,include
from rest_framework import routers
from .views import UserViewSet ,RegisterViewSet,LoginViewSet,LogoutView
router=routers.DefaultRouter()
router.register(r'users',UserViewSet,basename='user')
router.register(r'register', RegisterViewSet,basename='register')
router.register(r'login', LoginViewSet, basename='login')
urlpatterns = [
    path('',include(router.urls)),
    path('logout/',LogoutView.as_view(),name="logout"),
]