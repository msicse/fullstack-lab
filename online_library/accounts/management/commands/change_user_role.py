from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import UserProfile

class Command(BaseCommand):
    help = 'Change user role (user/admin)'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username to change role for')
        parser.add_argument('role', type=str, choices=['user', 'admin'], help='New role (user or admin)')

    def handle(self, *args, **options):
        username = options['username']
        new_role = options['role']
        
        try:
            user = User.objects.get(username=username)
            profile = user.profile
            old_role = profile.role
            
            profile.role = new_role
            profile.save()
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully changed {username} role from "{old_role}" to "{new_role}"'
                )
            )
            
        except User.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(f'User "{username}" does not exist')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error changing role: {e}')
            )