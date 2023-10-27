from rest_framework import serializers
from my_first_app.models import *


class EasyLevel_serializers (serializers.ModelSerializer):
    class Meta:
        model = EasyLevel
        fields = '__all__'

class MediumLevel_serializers (serializers.ModelSerializer):
    class Meta:
        model = MediumLevel
        fields = '__all__'

class HardLevel_serializers (serializers.ModelSerializer):
    class Meta:
        model = HardLevel
        fields = '__all__'

class AllDataSerializer(serializers.Serializer):
    easy_level_data = EasyLevel_serializers(many=True)
    medium_level_data = MediumLevel_serializers(many=True)
    hard_level_data = HardLevel_serializers(many=True)