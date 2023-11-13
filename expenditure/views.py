from django.db.models import Sum
from django.utils.dateparse import parse_date
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from expenditure.models import Expenditure
from expenditure.serializers import ExpenditureSerializer


class ExpenditureListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")
        category = request.query_params.get("category")
        min_amount = request.query_params.get("min_amount", 0)
        max_amount = request.query_params.get("max_amount", 1000000)

        if start_date:
            # 날짜 문자열을 날짜 객체로 변환
            start_date = parse_date(start_date)
        if end_date:
            end_date = parse_date(end_date)

        expenditures = Expenditure.objects.filter(
            user=request.user,
            date__range=[start_date, end_date],
            amount__gte=min_amount,
            amount__lte=max_amount,
        )

        if category:
            expenditures = expenditures.filter(category__name=category)

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
