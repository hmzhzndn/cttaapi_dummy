from rest_framework import serializers
from .models import CaseTT, MSISDNIMSI

class CaseTTSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseTT
        fields = ['MSISDN', 'IMSI']

class MSISDNIMSISerializer(serializers.ModelSerializer):
    class Meta:
        model = MSISDNIMSI
        fields = ['MSISDN', 'IMSI']
