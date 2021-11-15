# django command to delete user with specified email
from django.core.management import BaseCommand
from accounts.models import CustomUser


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--email', type=str, help='Email Address')

    def handle(self, *args, **kwargs):
        email = kwargs['email']
        try:
            if email:
                user = CustomUser.objects.get(email=email)
                user.delete()
                self.stdout.write(self.style.SUCCESS('User deleted successfully.'))
            else:
                self.stderr.write(self.style.ERROR('Email is required.'))
        except CustomUser.DoesNotExist:
            self.stderr.write(self.style.ERROR('User is not available.'))
