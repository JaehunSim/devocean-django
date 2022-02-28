from django.contrib import admin
from django.urls import include, path
from company import views as company_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/company/", company_views.CompanyList.as_view()),
    path("api/company/<int:pk>", company_views.CompanyDetail.as_view()),
]
