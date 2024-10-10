from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todoapp.urls')),  # todoapp uygulamasının URL'leri burada dahil ediliyor
]
