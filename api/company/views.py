from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.company.models import Company, Employee
from .serializers import CompanySerializer, EmployeeSerializer

@api_view(['GET'])
def getCompanyData(request):
    company_data_all = Company.objects.all()
    serializer = CompanySerializer(company_data_all, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getEmployeeData(request):
    employee_data_all = Employee.objects.all()
    serializer = EmployeeSerializer(employee_data_all, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addEmployee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)