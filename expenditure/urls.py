from django.urls import path
from expenditure.views import ExpenditureListView, TodayExpenditureView

urlpatterns = [
    path("", ExpenditureListView.as_view()),
    path("spending", TodayExpenditureView.as_view()),
]
