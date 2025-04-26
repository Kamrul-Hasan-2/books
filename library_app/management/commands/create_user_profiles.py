from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from library_app.models import UserProfile

class Command(BaseCommand):
    help = 'Create user profiles for existing users'

    def handle(self, *args, **options):
        users_without_profile = 0
        for user in User.objects.all():
            try:
                # Skip if profile exists
                user.profile
            except UserProfile.DoesNotExist:
                # Create profile if it doesn't exist
                UserProfile.objects.create(user=user)
                users_without_profile += 1
                self.stdout.write(f"Created profile for user: {user.username}")

        self.stdout.write(self.style.SUCCESS(f'Created {users_without_profile} user profiles'))