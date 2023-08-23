from myb_app import models
from rest_framework import serializers


class PaesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Paes
        fields = '__all__'


class CarnesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Carnes
        fields = '__all__'


class OpcionaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Opcionais
        fields = '__all__'


class Status_burguerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status_burguer
        fields = '__all__'


class BurguersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Burguers
        fields = '__all__'
