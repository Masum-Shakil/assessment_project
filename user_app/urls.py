from django.urls import path
from .views import signup, user_login, user_logout

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', user_login, name='signin'),
    path('signout/', user_logout, name='signout'),
]
