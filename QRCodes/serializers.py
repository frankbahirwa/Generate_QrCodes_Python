from rest_framework import serializers
from .models import *

class driverSerializer(serializers.Serializer):
                  class Meta:
                          model = Driver
                          fields = '__all__'
                          def create(self, validated_data):
                                  return Driver.objects.create(**validated_data)