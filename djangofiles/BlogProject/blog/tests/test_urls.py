from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import (
        about,
        question,
        displayPost,
        search,
        contact,
        newest,
        oldest,
        new_answer
        )
from users import views as user_views


class TestUrls(SimpleTestCase):

    def test_about_is_resolved(self):
        url = reverse('blog-about')
        print(resolve(url))
        self.assertEquals(resolve(url).func, about)

    def test_search_is_resolved(self):
        url = reverse('search')
        print(resolve(url))
        self.assertEquals(resolve(url).func, search)

    def test_oldest_is_resolved(self):
        url = reverse('oldest')
        print(resolve(url))
        self.assertEquals(resolve(url).func, oldest)

    def test_newest_is_resolved(self):
        url = reverse('newest')
        print(resolve(url))
        self.assertEquals(resolve(url).func, newest)

    def test_new_answer_is_resolved(self):
        url = reverse('new_answer')
        print(resolve(url))
        self.assertEquals(resolve(url).func, new_answer)

    def test_contact_is_resolved(self):
        url = reverse('Contact')
        print(resolve(url))
        self.assertEquals(resolve(url).func, contact)

    def test_post_detail_is_resolved(self):
        url = reverse('post-detail', kwargs={'pk' : 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func, displayPost)

    def test_question_is_resolved(self):
        url = reverse('questions')
        print(resolve(url))
        self.assertEquals(resolve(url).func, question)

    def test_profile_is_resolved(self):
        url = reverse('profile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, user_views.profile)

    def test_register_is_resolved(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, user_views.register)
