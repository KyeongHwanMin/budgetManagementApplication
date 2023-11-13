from rest_framework import serializers
from expenditure.models import Expenditure


class ExpenditureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenditure
        fields = ["id", "date", "amount", "category", "memo", "user", "excluded_total"]
        extra_kwargs = {"user": {"read_only": True}}
