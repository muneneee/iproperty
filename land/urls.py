from django.urls import path
from . import views

urlpatterns = [
  path('api/properties/', views.PropertyList.as_view()),
  path('api/properties/update/<int:pk>', views.PropertyUpdate.as_view(), name = 'update'),
  path('api/properties/delete/<int:pk>', views.PropertyDelete.as_view(), name = 'delete'),
]