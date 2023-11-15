from django.urls import path
from expenditure.views import ExpenditureListView, DailyExpenditureView

urlpatterns = [
    path("", ExpenditureListView.as_view()),
    path("spending", DailyExpenditureView.as_view()),
]
