from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import CaseTT, MSISDNIMSI
from .serializers import CaseTTSerializer, MSISDNIMSISerializer
from datetime import datetime, timedelta

class TransferDataView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # Restrict access to authenticated users

    def extract_date_from_description(self, description):
        try:
            #Extract date formatted as 'YYYY-MM-DD' from the case description
            date_str = description.split(' ')[-1]  
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            return None

    def get(self, request):
        # Fetch data from ctt_dummy
        case_data = CaseTT.objects.all()
        current_date = datetime.now()
        seven_days_ago = current_date - timedelta(days=7)

        # Insert data into datacollector_dummy for cases within the last 7 days
        for record in case_data:
            failure_date = self.extract_date_from_description(record.Case_Description)
            
            if failure_date and seven_days_ago <= failure_date <= current_date:
                # Check if the combination of MSISDN and IMSI already exists
                if not MSISDNIMSI.objects.filter(MSISDN=record.MSISDN, IMSI=record.IMSI).exists():
                    MSISDNIMSI.objects.create(
                        MSISDN=record.MSISDN,
                        IMSI=record.IMSI
                    )

        return Response({'message': 'MSISDN and IMSI transferred successfully for cases within 7 days'}, status=status.HTTP_200_OK)
