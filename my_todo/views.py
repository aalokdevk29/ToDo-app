
from my_todo.models import Todo, Category
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from my_todo.serializers import CategorySerializer, TodoSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """Category API that allows category to be viewed or edited."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


class TodoViewSet(viewsets.ModelViewSet):
    """Todo API that allows todo to be viewed or edited."""

    queryset = Todo.objects.all().order_by('created_date')
    serializer_class = TodoSerializer
    permission_classes = (AllowAny,)

