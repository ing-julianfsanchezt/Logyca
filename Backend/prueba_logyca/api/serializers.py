from rest_framework import serializers
import math


class NumerosSerializer(serializers.Serializer):
    n = serializers.CharField()

    
