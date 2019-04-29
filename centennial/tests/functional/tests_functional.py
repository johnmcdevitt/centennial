from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import LiveServerTestCase
import time
from webusers.models import WebUser

class SiteVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        ## creating a test user to login to the site, then starting browser
        self.testuser = WebUser.objects.create(username="natasha")
        self.testuser.set_password("secret_code")
        self.testuser.save()
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def login(self, username="natasha",password="secret_code"):
        # Natasha has heard about a cool new online app for her house, the Perkiomen Homestead. She goes
        # to check out its homepage
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention Perkiomen Homestead lists
        self.assertIn('Perkiomen Homestead', self.browser.title)

        # Natasha notices a login button, and has already registered so wants to login
        # She clicks the button and is taken to a login page
        login_btn = self.browser.find_element_by_id("login-btn")
        login_btn.click()
        time.sleep(1)

        labels = self.browser.find_elements_by_tag_name("label")
        self.assertTrue(
            any(label.text == "Username:" for label in labels)
        )

        # She enters her credentials
        username_field = self.browser.find_element_by_id("id_username")
        username_field.send_keys(username)
        password_field = self.browser.find_element_by_id("id_password")
        password_field.send_keys(password)
        self.browser.find_element_by_id("login-submit").click()
        time.sleep(1)
        # she is taken to her profile page
        page_title = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("profile", page_title)

    def logout(self):
        pass

    # start of functional tests

    def test_user_creates_cards_a_card_type_and_sees_them_on_the_board(self):
        # Natasha goes to the site and logs in
        self.login()

        # Natasha sees the Navigation change now that she is logged in
        # She clicks the link for the Board to see that page
        navlinks = self.browser.find_elements_by_class_name("nav-link")
        for link in navlinks:
            if link.text == "Board":
                link.click()
                break
        time.sleep(1)

        # She is taken to a page that has a KANBAN board. She hates Kanban, but
        # the title on the page is Task board. She sighs with relief and thinks
        # maybe this is ok
        page_title = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("Task board", page_title)

        # she sees a link to add a card to the board, and clicks that link to get started
        self.browser.find_element_by_class_name("create-card").click()
        time.sleep(1)

        # a form pops up on the screen, she completes the form to see if her
        # card is created. She creates a task to buy a wood burning stove as a
        # high priority
        title = self.browser.find_element_by_id("title_head")
        title.send_keys("buy a wood burning stove")
        self.browser.find_element_by_id("dropdownMenuPriority").click()
        self.browser.find_element_by_class_name("fa-fire-alt").click()
        self.browser.find_element_by_id("dropdownMenuType").click()
        # she sees that there are no type options and submits her card
        # self.browser.find_element_by_class_name("fa-hammer").click()
        self.browser.find_element_by_id("card-submit").click()

        # Natasha goes to the card types page to create her own card type.
        self.fail("finish test")

        # Natasha wants to create a new card with the type she just created

        # She returns to the board to see her cards
        time.sleep(1)
        card_titles = map(lambda x: x.text, self.browser.find_elements_by_class_name("portlet-header"))
        card_titles = set(card_titles)
        self.assertIn("buy a wood burning stove".upper(), card_titles)
