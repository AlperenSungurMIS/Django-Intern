from rest_framework import generics
from .models import Item, Location
from .serializers import ItemSerializer, LocationSerializer  # Düzeltildi

class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(itemLocation=location)  # Filtreleme doğru yapılıyor
        return queryset  # Düzeltildi

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer  # Düzeltildi
    queryset = Location.objects.all()

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer  # Düzeltildi
    queryset = Location.objects.all()
