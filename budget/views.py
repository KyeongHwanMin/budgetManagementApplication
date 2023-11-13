from rest_framework import status
from rest_framework.response import Response

from budget.models import Category
from rest_framework.views import APIView
from budget.serializers import CategorySerializer


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
