from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.company.models import Company
from .serializers import CompanySerializer

@api_view(['GET'])
def getCompanyData(request):
    company_data_all = Company.objects.all()
    serializer = CompanySerializer(company_data_all, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addCompany(request):
    serializer = CompanySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)