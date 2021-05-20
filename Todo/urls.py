
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from my_todo.views import CategoryViewSet, TodoViewSet

router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet)
router.register(r'category', CategoryViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]
