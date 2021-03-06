from django.test import TestCase
from django.utils import timezone
from django.db.utils import IntegrityError

# project specific imports
from cards.models import Card, CardType

# test methods
class CardTypeTest(TestCase):

    def test_create_card_type(self):
        ct = CardType.objects.create(cardtype="test type",color="123456")
        self.assertTrue(isinstance(ct, CardType))
        self.assertTrue(ct.cardtype, ct.__str__())


        with self.assertRaisesMessage(IntegrityError, 'duplicate key value violates unique constraint "cards_cardtype_cardtype_key"'):
            ct2=CardType.objects.create(cardtype="test type",color="654321")

    def test_card_type_count(self):
        ct = CardType.objects.create(cardtype="test type",color="123456")

        # test 0 cards of that type
        self.assertEqual(ct.cardcount(), 0)

        # test 3 cards with a certain types
        c1 = Card.objects.create(title="test card", type=ct)
        c2 = Card.objects.create(title="second test card", type=ct)
        c3 = Card.objects.create(title="third test card", type=ct)
        self.assertEqual(ct.cardcount(),3)

class CardTest(TestCase):

    def create_card(self, title= "This is a test card",
                    description='Lorem ipsum dolor sit amet, consectetur \
                    adipisicing elit, sed do eiusmod tempor incididunt ut \
                    labore et dolore magna aliqua.',
                    priority=1,
                    status='100'):
        return Card.objects.create(title=title,description=description,
                                   priority=priority,status=status)

    def test_card_default_order(self):
        c1 = self.create_card()
        c2 = self.create_card()
        c3 = self.create_card()

        # test default order function puts items in correct order
        self.assertTrue(c1.order > c2.order)
        self.assertTrue(c2.order > c3.order)
        self.assertTrue(c1.order < 101000000)
        self.assertTrue(c3.order > 100000000)

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

    def test_create_card_type(self):
        ct = CardType.objects.create(cardtype="Test type", color="000000")

        self.assertTrue(isinstance(ct, CardType))
        self.assertEqual(ct.cardtype, ct.__str__())

    def test_getcolor_for_card(self):
        ct = CardType.objects.create(cardtype="test type", color="777777")
        c = self.create_card()

        # color is 000000 when type is None
        self.assertTrue(c.type is None)
        self.assertEqual(c.getcolor(), "000000")

        c.type = ct
        c.save()
        self.assertEqual(ct.color, c.getcolor())
