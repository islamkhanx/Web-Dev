from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Company, Vacancy
from .serializers import CompanySerializer, VacancySerializer


class CompanyList(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetail(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = 'id'


class VacancyList(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class VacancyDetail(generics.RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    lookup_field = 'id'


class TopTenVacancies(generics.ListAPIView):
    queryset = Vacancy.objects.all().order_by('-salary')[:10]
    serializer_class = VacancySerializer


@api_view(['GET'])
def company_vacancies(request, id):
    company = get_object_or_404(Company, id=id)
    vacancies = company.vacancies.all()
    serializer = VacancySerializer(vacancies, many=True)
    return Response(serializer.data)
