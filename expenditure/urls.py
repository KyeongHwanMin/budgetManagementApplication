from django.urls import path
from expenditure.views import ExpenditureListView

urlpatterns = [
    path("", ExpenditureListView.as_view()),
]
