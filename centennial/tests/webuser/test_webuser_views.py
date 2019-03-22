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
                                              email="test@example.com")
        self.testuser.set_password("secret_password")
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
        self.assertContains(response, self.testuser.first_name)

    def test_update_profile_view(self):
        self.client.login(username="testuser", password="secret_password")
        get_response = self.client.get(reverse("profile-update"))

        self.assertEqual(get_response.status_code,200)
        self.assertContains(get_response,self.testuser.email)

        # construct form_data
        post_data = dict(first_name="first",last_name="LAST",email="test@test.com")
        # post data and successfully redirected
        post_response = self.client.post(reverse('profile-update'),post_data,follow=True)
        self.assertRedirects(post_response,reverse('profile'),status_code=302,target_status_code=200)

        # get test user from the attributes from the database
        self.testuser = WebUser.objects.filter(username="testuser")[0]
        self.assertEqual(self.testuser.first_name, "first")
        self.assertEqual(self.testuser.last_name, "LAST")
        self.assertEqual(self.testuser.email, "test@test.com")

    def test_logout_view(self):
        self.client.login(username="testuser",password="secret_password")

        response = self.client.get(reverse("logout"),follow=True)
        self.assertRedirects(response,reverse("login"),status_code=302,target_status_code=200)
