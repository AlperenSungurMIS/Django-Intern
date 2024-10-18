
from django.urls import path
from . import views

urlpatterns = [
    path('list', views.kurslar),
    path('details', views.details),
    path('programlama', views.programlama),
    path('mobil-uygulamalar', views.mobiluygulamalar),
    path('<category>', views.getCoursesByCategory)
]


