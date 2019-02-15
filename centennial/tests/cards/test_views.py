from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from django.test import Client

# project specific imports
from cards.models import Card

#

class CardViewTest(TestCase):
    # TODO: This is not DRY create card in test model and test views
    def create_card(self, title= "This is a test card",
                    description='Lorem ipsum dolor sit amet, consectetur \
                    adipisicing elit, sed do eiusmod tempor incididunt ut \
                    labore et dolore magna aliqua.',
                    priority=1):
        return Card.objects.create(title=title,description=description,priority=1)


    def test_card_list_view_contains_created_cards(self):
        # create cards
        c1 = self.create_card()
        c2 = self.create_card(title="just another card",priority=3)
        # get view
        conn = Client()
        url = reverse("backlog")
        response = conn.get(url)

        self.assertEqual(response.status_code, 200)
        # self.assertContains(c1.title, response.content)
        self.assertContains(response, c1.title)
        self.assertContains(response, c2.title)
        self.assertNotContains(response, "No cards available")

    def test_card_view_with_no_cards(self):
        conn = Client()
        url = reverse("backlog")
        response = conn.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No cards available")
