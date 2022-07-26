from rest_framework.serializers import ModelSerializer
from unsaTur.models import Atr, List, Tipatr, Usucab, Zontur, ZonturList, Zonturcom, Zonturhor


class AtrSerializer(ModelSerializer):

    class Meta:
        model = Atr
        depth = 2
        fields = '__all__'


class ListSerializer(ModelSerializer):

    class Meta:
        model = List
        depth = 2
        fields = '__all__'


class TipatrSerializer(ModelSerializer):

    class Meta:
        model = Tipatr
        depth = 2
        fields = '__all__'


class UsucabSerializer(ModelSerializer):

    class Meta:
        model = Usucab
        depth = 2
        fields = '__all__'


class ZonturSerializer(ModelSerializer):

    class Meta:
        model = Zontur
        depth = 2
        fields = [
            "zonturide",
            "zonturnom",
            "zonturdir",
            "zonturpun",
            "zonturima",
            "zonturdes",
            "zonturnumvis",
            "fecpub",
            "fecingusu",
            "identificador_usuario"
        ]
        


class ZonturListSerializer(ModelSerializer):

    class Meta:
        model = ZonturList
        depth = 2
        fields = '__all__'


class ZonturcomSerializer(ModelSerializer):

    class Meta:
        model = Zonturcom
        depth = 2
        fields = '__all__'


class ZonturhorSerializer(ModelSerializer):

    class Meta:
        model = Zonturhor
        depth = 2
        fields = '__all__'
