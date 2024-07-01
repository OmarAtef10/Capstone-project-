from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from Restaurant.models import Booking, Menu
from Restaurant.serializers import BookingSerializer, MenuSerializer


# Create your views here.

def index(request):
    return render(request, 'index.html', {})


class BookingView(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


class MenuItemsView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
