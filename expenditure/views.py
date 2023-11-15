from django.db.models import Sum, Q
from django.utils import timezone
from django.utils.dateparse import parse_date
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from budget.models import Budget
from expenditure.models import Expenditure
from expenditure.serializers import ExpenditureSerializer


class ExpenditureListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")
        category = request.query_params.get("category")
        min_amount = request.query_params.get("min_amount")
        max_amount = request.query_params.get("max_amount")

        filters = Q(user=request.user)
        if start_date and end_date:
            start_date = parse_date(start_date)
            end_date = parse_date(end_date)
            filters &= Q(date__range=[start_date, end_date])

        if min_amount and max_amount:
            filters &= Q(amount__get=min_amount, amount__lte=max_amount)
        elif min_amount:
            filters &= Q(amount__gte=min_amount)
        elif max_amount:
            filters &= Q(amount__lte=max_amount)

        if category:
            filters &= Q(category__name=category)

        expenditures = Expenditure.objects.filter(filters, excluded_total=False)
        total_expenditure = expenditures.aggregate(Sum("amount"))
        category_totals = expenditures.values("category__name").annotate(
            total=Sum("amount")
        )

        serializer = ExpenditureSerializer(expenditures, many=True)
        data = {
            "지출": serializer.data,
            "지출 합계": total_expenditure["amount__sum"],
            "카테고리 별 지출 합계": category_totals,
        }
        return Response(data)

    def post(self, request):
        serializer = ExpenditureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DailyExpenditureView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        today = timezone.now().date()
        today_expenditures = Expenditure.objects.filter(
            user=request.user, date__date=today
        )
        month_budgets = Budget.objects.filter(
            user=request.user, period__month=today.month, period__year=today.year
        )

        total_expenditure = (
            today_expenditures.aggregate(total=Sum("amount"))["total"] or 0
        )
        category_totals = today_expenditures.values("category__name").annotate(
            total=Sum("amount")
        )

        category_total_dict = {
            item["category__name"]: item["total"] for item in category_totals
        }

        statistics = []
        for budget in month_budgets:
            category_name = budget.category.name
            expected_amount = budget.amount / today.day
            spent_amount = category_total_dict.get(category_name, 0)
            print(category_name, spent_amount)
            risk = (spent_amount / expected_amount) * 100 if expected_amount > 0 else 0

            statistics.append(
                {
                    "category": category_name,
                    "expected_amount": expected_amount,
                    "spent_amount": spent_amount,
                    "risk_percentage": risk,
                }
            )

        return Response(
            {
                "total_expenditure": total_expenditure,
                "category_totals": list(category_totals),
                "statistics": statistics,
            }
        )
