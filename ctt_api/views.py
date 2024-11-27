from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CaseTT, MSISDNIMSI
from .serializers import CaseTTSerializer, MSISDNIMSISerializer

class TransferDataView(APIView):
    def get(self, request):
        # Fetch data from ctt_dummy
        case_data = CaseTT.objects.all()
        serializer = CaseTTSerializer(case_data, many=True)

        # Insert data into datacollector_dummy
        for record in serializer.data:
            msisdn = record['MSISDN']
            imsi = record['IMSI']

            # Check if the combination of MSISDN and IMSI already exists
            if not MSISDNIMSI.objects.filter(MSISDN=msisdn, IMSI=imsi).exists():
                MSISDNIMSI.objects.create(
                    MSISDN=msisdn,
                    IMSI=imsi
                )

        return Response({'message': 'Data transferred successfully!'}, status=status.HTTP_200_OK)
