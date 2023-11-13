from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from budget.models import Category, Budget
from rest_framework.views import APIView
from budget.serializers import CategorySerializer, BudgetSerializer


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BudgetView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        category_name = request.data.get("category_name")
        try:
            category = Category.objects.get(name=category_name)
        except Category.DoesNotExist:
            return Response("카테고리가 존재하지 않습니다.", status=status.HTTP_404_NOT_FOUND)

        existing_category = Budget.objects.filter(
            user=request.user, category=category
        ).first()
        if existing_category:
            return Response(
                "카테고리에 이미 예산이 등록되어 있습니다.", status=status.HTTP_400_BAD_REQUEST
            )

        serializer = BudgetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            budget = Budget.objects.get(pk=pk, user=request.user)
        except Budget.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BudgetSerializer(budget, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
