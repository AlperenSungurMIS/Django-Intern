from django.urls import path
from . import views

urlpatterns = [
    path('list', views.kurslar),
    path('', views.kurslar),
    path('<kurs_adi>', views.details),
    path('<int:category_name>', views.getCoursesByCategory),
    path('<str:category_id>', views.getCoursesByCategoryId),
]
