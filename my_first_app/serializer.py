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

