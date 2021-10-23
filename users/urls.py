from django.urls import path
from .views import RegisterView, LoginView

urlpatterns = [
    path('sign-up/', RegisterView.as_view(), name='sign_up'),
    path('sign-in/', LoginView.as_view(), name='sign_in')
]
