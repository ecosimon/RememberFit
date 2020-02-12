from django.test import TestCase
from .models import UserProfile, User

class UserProfileTestCase(TestCase):
    def test_str(self):
        simon_obj = User.objects.create(username="Simon")
        simon_profile = UserProfile.objects.create(user=simon_obj)

        self.assertEqual(str(simon_profile), 'Simon')
