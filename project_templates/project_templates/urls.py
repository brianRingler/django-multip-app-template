from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('profile_app.urls')),
    path('profile/', include('login_app.urls')),
    path('profile/', include('register_app.urls'))
]
