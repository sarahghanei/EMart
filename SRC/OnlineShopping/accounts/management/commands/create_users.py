# command for creating users with email included in the command

from django.core.management import BaseCommand
from accounts.models import CustomUser


class Command(BaseCommand):
    def add_arguments(self, parser):
        # positional argument for email
        parser.add_argument('--email', type=str, help='Email address')
        # optional argument for phone number
        parser.add_argument('--phone', type=str, help='Phone number')
        # flag argument for being admin or not
        parser.add_argument('-a', '--admin', action='store_true', help='Admin user')

    def handle(self, *args, **kwargs):
        email = kwargs['email']
        phone = kwargs['phone']
        admin = kwargs['admin']
        try:
            if email:
                is_unique = CustomUser.objects.filter(email=email).exists()
                if not is_unique:
                    # email address is new and not available in the database
                    if admin:
                        user = CustomUser.objects.create_superuser(email=email, password='1234')
                    else:
                        user = CustomUser.objects.create_user(email=email, password='1234')

                    if phone:
                        user.phone_number = phone
                        user.save()
                    self.stdout.write(self.style.SUCCESS('User created successfully with email {}'.format(email)))
                else:
                    # email is already exists in the database.
                    raise ValueError
            else:
                self.stderr.write(self.style.ERROR('Email is required.'))

        except ValueError:
            self.stderr.write(self.style.ERROR('A user with this email already exists.'))
