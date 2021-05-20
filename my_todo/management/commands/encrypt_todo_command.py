
from django.core.management.base import BaseCommand
from django.conf import settings
from my_todo.models import Todo
from cryptography.fernet import Fernet
import requests


class Command(BaseCommand):
    """To perform summetric encryption on todo's."""

    help = "Displays Todo's symmetric encryption"

    def handle(self, *args, **kwargs):
        """To perform summetric encryption on todo's."""
        try:
            todo = Todo.objects.first()
            if todo:
                key = Fernet.generate_key()
                response = requests.get(settings.API_ROOT_URL + '/todos/' + str(todo.id) + '/')
                f = Fernet(key)
                print('\033[1m Before encryption: \033[0;0m \n', response.content, '\n')
                encrypted = f.encrypt(response.content)
                print('\033[1m After encryption: \033[0;0m \n', encrypted, '\n')
                decrypted_encrypted = f.decrypt(encrypted)
                print('\033[1m After dcryption: \033[0;0m \n', decrypted_encrypted, '\n')
                exit()
            self.stdout.write("There is no todo recods in database.")
        except Exception as e:
            print('Something went wrong.')


