from rest_framework import serializers
from budget.models import Category, Budget


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BudgetSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    category_name = serializers.CharField(write_only=True)

    class Meta:
        model = Budget
        fields = ["user", "amount", "period", "category_name"]

    def validate_category_name(self, value):
        try:
            category = Category.objects.get(name=value)
        except Category.DoesNotExist:
            raise serializers.ValidationError("없는 카테고리 입니다.")
        return category

    def create(self, validated_data):
        category_name = validated_data.pop("category_name")
        category = Category.objects.get(name=category_name)
        budget = Budget.objects.create(category=category, **validated_data)
        return budget

    def update(self, instance, validated_data):
        instance.category = validated_data.get("category_name", instance.category)
        instance.amount = validated_data.get("amount", instance.amount)
        instance.period = validated_data.get("period", instance.period)
        instance.save()
        return instance
