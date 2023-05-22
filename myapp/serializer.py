from rest_framework import serializers
from .models import Doctor, Pacient, Image

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        read_only_fields = ('id',)

class PacientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacient
        fields = '__all__'
        read_only_fields = ('id',)

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
        read_only_fields = ('id',)