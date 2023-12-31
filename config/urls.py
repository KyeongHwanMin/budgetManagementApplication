from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/user/", include("account.urls")),
    path("api/v1/budget/", include("budget.urls")),
    path("api/v1/expenditure/", include("expenditure.urls")),
]
