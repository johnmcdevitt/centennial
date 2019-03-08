from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from django.test import Client

# project specific imports
from webusers.models import WebUser

class WebuserTestViews(TestCase):

    def setUp(self):
        self.client = Client()

        # test user testuser
        self.testuser = WebUser.objects.create(username="testuser",
                                              first_name="test",
                                              last_name="user",
                                              email="test@example.com",
                                              password="secret_password")
        self.testuser.save()


    def test_registration_flow(self):
        # testuser does not exist yet
        un = "registrationtestuser"
        u = WebUser.objects.filter(username=un)
        self.assertEqual(len(u), 0)

        # test get returns 200
        get_response = self.client.get(reverse("register"))
        self.assertEqual(get_response.status_code, 200)

        # test posting data
        post_data = dict(username=un,password1="top_secret_password",password2="top_secret_password")
        post_response = self.client.post(reverse("register"),post_data)
        self.assertEqual(post_response.status_code,302)

        # confirm testuser was created
        u = WebUser.objects.filter(username=un)
        self.assertEqual(len(u),1)
        self.assertEqual(u[0].__str__(), post_data["username"])

    def test_profile_view(self):
        self.client.login(username="testuser", password="secret_password")
        response = self.client.get(reverse("profile"))

        self.assertEqual(response.status_code,200)
        print(response.content)
        self.assertContains(response, self.testuser.first_name)



    def test_update_profile_view(self):
        #self.assertTrue(False)
        pass
