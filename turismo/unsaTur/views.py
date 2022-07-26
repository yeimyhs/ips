from rest_framework.viewsets import ModelViewSet
from unsaTur.serializers import AtrSerializer, ListSerializer, TipatrSerializer, UsucabSerializer, ZonturSerializer, ZonturListSerializer, ZonturcomSerializer, ZonturhorSerializer
from unsaTur.models import Atr, List, Tipatr, Usucab, Zontur, ZonturList, Zonturcom, Zonturhor


class AtrViewSet(ModelViewSet):
    queryset = Atr.objects.order_by('pk')
    serializer_class = AtrSerializer


class ListViewSet(ModelViewSet):
    queryset = List.objects.order_by('pk')
    serializer_class = ListSerializer


class TipatrViewSet(ModelViewSet):
    queryset = Tipatr.objects.order_by('pk')
    serializer_class = TipatrSerializer


class UsucabViewSet(ModelViewSet):
    queryset = Usucab.objects.order_by('pk')
    serializer_class = UsucabSerializer


class ZonturViewSet(ModelViewSet):
    queryset = Zontur.objects.order_by('pk')
    serializer_class = ZonturSerializer


class ZonturListViewSet(ModelViewSet):
    queryset = ZonturList.objects.order_by('pk')
    serializer_class = ZonturListSerializer


class ZonturcomViewSet(ModelViewSet):
    queryset = Zonturcom.objects.order_by('pk')
    serializer_class = ZonturcomSerializer


class ZonturhorViewSet(ModelViewSet):
    queryset = Zonturhor.objects.order_by('pk')
    serializer_class = ZonturhorSerializer
