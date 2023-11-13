from django.urls import path

from budget.views import CategoryListView

urlpatterns = [
    path("categories", CategoryListView.as_view()),
]
