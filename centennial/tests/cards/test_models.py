from django.test import TestCase
from django.utils import timezone

# project specific imports
from cards.models import Card

# test methods
class CardTest(TestCase):

    def create_card(self, title= "This is a test card",
                    description='Lorem ipsum dolor sit amet, consectetur \
                    adipisicing elit, sed do eiusmod tempor incididunt ut \
                    labore et dolore magna aliqua.',
                    priority=1):
        return Card.objects.create(title=title,description=description,priority=1)

    def test_card_creation(self):
        c = self.create_card()
        self.assertTrue(isinstance(c, Card))
        self.assertEqual(c.__str__(),c.title)
