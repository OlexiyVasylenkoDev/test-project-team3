from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='token_obtain_view'),
    path('registration/', views.Registration.as_view(), name='registration_view'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh_view'),
]
