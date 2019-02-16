from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from django.test import Client

# project specific imports
from cards.models import Card


class CardViewTest(TestCase):
    # TODO: This is not DRY create card in test model and test views

    def get_response_from_name(self, name):
        conn = Client()
        url = reverse(name)
        return conn.get(url)

    @classmethod
    def setUp(self):

        def create_card(title= "This is a test card",
                        description='Lorem ipsum dolor sit amet, consectetur \
                        adipisicing elit, sed do eiusmod tempor incididunt ut \
                        labore et dolore magna aliqua.',
                        priority=1, status='100'):
            return Card.objects.create(title=title,description=description,
                                       priority=priority, status=status)
        # setup some test cards
        self.c1 = create_card(title="Backlog card")
        self.c2 = create_card(title="To do card", status='200')
        self.c3 = create_card(title="In progress card", status='300')
        self.c4 = create_card(title="Review card", status='400')
        self.c5 = create_card(title="Done card", status='500')
        self.c6 = create_card(title="Another backlog card")
        self.c7 = create_card(title="Another to do card", status='200')
        self.c8 = create_card(title="Another in progress card", status='300')
        self.c9 = create_card(title="Another review card", status='400')
        self.c10 = create_card(title="Another done card", status='500')


    def test_backlog_view_contains_correct_cards(self):

        response = self.get_response_from_name('backlog')

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, self.c1.title)
        self.assertContains(response, self.c6.title)
        # should not have non-backlog cards or no cards message
        self.assertNotContains(response, "No cards available")
        self.assertNotContains(response, self.c2.title)
        self.assertNotContains(response, self.c3.title)
        self.assertNotContains(response, self.c4.title)
        self.assertNotContains(response, self.c5.title)

    def test_backlog_view_with_no_cards(self):
        self.c1.status='500'
        self.c1.save()
        self.c6.status='300'
        self.c6.save()

        response = self.get_response_from_name('backlog')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No cards available")
        self.assertNotContains(response, self.c1.title)

    def test_to_do_view_with_no_cards(self):
        self.c2.status='100'
        self.c2.save()
        self.c7.status='300'
        self.c7.save()

        response = self.get_response_from_name('to-do')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No cards available")
        self.assertNotContains(response, self.c2.title)


    def test_to_do_view_has_correct_cards(self):
        response = self.get_response_from_name('to-do')

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, self.c2.title)
        self.assertContains(response, self.c7.title)
        # should not have non-backlog cards or no cards message
        self.assertNotContains(response, "No cards available")
        self.assertNotContains(response, self.c1.title)
        self.assertNotContains(response, self.c3.title)
        self.assertNotContains(response, self.c4.title)
        self.assertNotContains(response, self.c5.title)

    def test_in_progress_view_with_no_cards(self):
            self.c3.status='200'
            self.c3.save()
            self.c8.status='400'
            self.c8.save()

            response = self.get_response_from_name('in-progress')

            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "No cards available")
            self.assertNotContains(response, self.c3.title)

    def test_in_progress_view_has_correct_cards(self):
        response = self.get_response_from_name('in-progress')

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, self.c3.title)
        self.assertContains(response, self.c8.title)
        # should not have non-backlog cards or no cards message
        self.assertNotContains(response, "No cards available")
        self.assertNotContains(response, self.c2.title)
        self.assertNotContains(response, self.c1.title)
        self.assertNotContains(response, self.c4.title)
        self.assertNotContains(response, self.c5.title)

    def test_review_view_with_no_cards(self):
        self.c4.status='300'
        self.c4.save()
        self.c9.status='500'
        self.c9.save()

        response = self.get_response_from_name('review')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No cards available")
        self.assertNotContains(response, self.c4.title)

    def test_review_view_has_correct_cards(self):
        response = self.get_response_from_name('review')

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, self.c4.title)
        self.assertContains(response, self.c9.title)
        # should not have non-backlog cards or no cards message
        self.assertNotContains(response, "No cards available")
        self.assertNotContains(response, self.c2.title)
        self.assertNotContains(response, self.c3.title)
        self.assertNotContains(response, self.c1.title)
        self.assertNotContains(response, self.c5.title)

    def test_done_view_with_no_cards(self):
        self.c5.status='400'
        self.c5.save()
        self.c10.status='100'
        self.c10.save()

        response = self.get_response_from_name('done')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No cards available")
        self.assertNotContains(response, self.c5.title)

    def test_done_view_has_correct_cards(self):
        response = self.get_response_from_name('done')

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, self.c5.title)
        self.assertContains(response, self.c10.title)
        # should not have non-backlog cards or no cards message
        self.assertNotContains(response, "No cards available")
        self.assertNotContains(response, self.c2.title)
        self.assertNotContains(response, self.c3.title)
        self.assertNotContains(response, self.c4.title)
        self.assertNotContains(response, self.c1.title)

    def test_create_card_view(self):
        response = self.get_response_from_name("create-card")

        self.assertEqual(response.status_code, 200)
