from django.contrib import admin
from django.urls import path, include
from employee_app.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('employee/', include('employee_app.urls')),
    path('user/', include('user_app.urls'))
]
