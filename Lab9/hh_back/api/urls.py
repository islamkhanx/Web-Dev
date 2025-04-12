from django.urls import path
from . import views

urlpatterns = [
    path("companies/", views.CompanyList.as_view(), name="company-list"),
    path(
        "companies/<int:id>/",
        views.CompanyDetail.as_view(),
        name="company-detail",
    ),
    path(
        "companies/<int:id>/vacancies/",
        views.company_vacancies,
        name="company-vacancies",
    ),
    path("vacancies/", views.VacancyList.as_view(), name="vacancy-list"),
    path(
        "vacancies/<int:id>/",
        views.VacancyDetail.as_view(),
        name="vacancy-detail",
    ),
    path(
        "vacancies/top_ten/",
        views.TopTenVacancies.as_view(),
        name="top-ten-vacancies",
    ),
]
