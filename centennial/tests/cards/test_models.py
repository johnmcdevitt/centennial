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
                    priority=1,
                    status='100'):
        return Card.objects.create(title=title,description=description,
                                   priority=priority,status=status)

    def test_card_creation(self):
        c = self.create_card()
        self.assertTrue(isinstance(c, Card))
        self.assertEqual(c.__str__(),c.title)

    def test_card_status_and_labels(self):
        c1 = self.create_card()
        c2 = self.create_card(status='200')
        c3 = self.create_card(status='300')
        c4 = self.create_card(status='400')
        c5 = self.create_card(status='500')

        # Backlog card test
        self.assertTrue(isinstance(c1, Card))
        self.assertEqual(c1.get_status_display(), "Backlog")
        # To do card test
        self.assertTrue(isinstance(c2, Card))
        self.assertEqual(c2.get_status_display(), "To do")
        # In progress
        self.assertTrue(isinstance(c3, Card))
        self.assertEqual(c3.get_status_display(), "In progress")
        # Review
        self.assertTrue(isinstance(c4, Card))
        self.assertEqual(c4.get_status_display(), "Review")
        # Done
        self.assertTrue(isinstance(c5, Card))
        self.assertEqual(c5.get_status_display(), "Done")
