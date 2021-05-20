
from my_todo.models import Todo, Category
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    """Category model serializer."""

    class Meta:
        model = Category
        fields = ['id', 'name']


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    """Todo model serializer."""

    category = CategorySerializer(many=False, read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Todo
        fields = '__all__'

    def validate(self, attrs):
        """Custom error for invalid category id for."""
        if not Category.objects.filter(pk=attrs['category_id']).exists():
            raise serializers.ValidationError({"category_id": " You have enterd Invalid category Id."})
        return attrs
