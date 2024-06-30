from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booking/tables/', views.BookingView.as_view({"get": "list","post":"create"}), name='booking'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view()),
]
