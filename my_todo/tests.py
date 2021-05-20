from django.test import TestCase
from rest_framework.test import APIClient
from django.conf import settings
from my_todo.models import Todo, Category
import json



class TodoTestCase(TestCase):

    def setUp(self):
        first_cat_obj = Category.objects.create(name="Signing")
        second_cat_obj = Category.objects.create(name="Dancing")
        Todo.objects.create(
            title="My first Todo", content="First todo created for testing",
            status='Hold',
            category=first_cat_obj,
        )
        Todo.objects.create(
            title="My Second Todo", content="Second todo created for testing",
            status='Start',
            category=second_cat_obj,
        )

    def test_add_category(self):
        """To test add category api."""
        client = APIClient()
        response = client.post(settings.API_ROOT_URL + '/category/', {'name': 'Play'},format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.content)['name'], 'Play')
        self.assertTrue(Category.objects.filter(name='Play').exists())

    def test_update_category(self):
        """To test update category api."""
        client = APIClient()
        cat_obj = Category.objects.first()
        url = settings.API_ROOT_URL + '/category/' + str(cat_obj.id) + '/'
        response = client.patch(url, {'name': 'Acting'}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['name'], Category.objects.get(pk=cat_obj.id).name)

    def test_get_category(self):
        """To test get category api."""
        client = APIClient()
        response = client.get(settings.API_ROOT_URL + '/category/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.content)), Category.objects.all().count())

    def test_delete_category(self):
        """To test delete category api."""
        client = APIClient()
        self.assertEqual(Category.objects.all().count(), 2)
        cat_obj = Category.objects.first()
        url = settings.API_ROOT_URL + '/category/' + str(cat_obj.id) + '/'
        response = client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Category.objects.all().count(), 1)

    def test_add_todo(self):
        """To test add todo api."""
        client = APIClient()
        cat_obj = Category.objects.first()
        post_data = {
            'title': "My Third Todo", 'content': "Third todo created for testing",
            'status': 'Hold', 'category_id': cat_obj.pk}
        response = client.post(settings.API_ROOT_URL + '/todos/', post_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.content)['title'], 'My Third Todo')
        self.assertTrue(Todo.objects.filter(title='My Third Todo').exists())

    def test_update_todo(self):
        """To test update todo api."""
        client = APIClient()
        todo_obj = Todo.objects.first()
        cat_obj = Category.objects.first()
        post_data = {
            'title': "Updated Third Todo",
            'content': "Third todo Updated for testing",
            'category_id': cat_obj.pk}
        url = settings.API_ROOT_URL + '/todos/' + str(todo_obj.id) + '/'
        response = client.patch(url, post_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['title'], Todo.objects.get(pk=todo_obj.id).title)

    def test_get_todo(self):
        """To test get todo api."""
        client = APIClient()
        response = client.get(settings.API_ROOT_URL + '/todos/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.content)), Todo.objects.all().count())

    def test_delete_todo(self):
        """To test delete todo api."""
        client = APIClient()
        self.assertEqual(Todo.objects.all().count(), 2)
        todo_obj = Todo.objects.first()
        url = settings.API_ROOT_URL + '/todos/' + str(todo_obj.id) + '/'
        response = client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Todo.objects.all().count(), 1)

