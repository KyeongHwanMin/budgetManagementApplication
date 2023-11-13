from django.urls import path

from budget.views import CategoryListView, BudgetView

urlpatterns = [
    path("categories", CategoryListView.as_view()),
    path("", BudgetView.as_view()),
    path("<pk>", BudgetView.as_view()),
]
