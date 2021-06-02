#from django.urls import reverse
#from .models import (Post,Tag,Comment,Question,Answer)
#import json


#class TestViews(TestCase):
    #def setUp(self):
        #self.client = Client()
        #self.oldest_url = reverse('oldest')
        #self.new_answer_url = reverse('new_answer')
        #self.user_posts_url = reverse('user-posts')
        #self.profile_url = reverse('profile')
        #self.post_detail_url = reverse('post-detail')
        #self.my_posts_url = reverse('my_posts')
        #self.post_create_url = reverse('post-create')
        #self.questions_url = reverse('questions')
        #self.post_update_url = reverse('post-update')
        #self.register_url = reverse('register')
        #self.blog_about_url = reverse('blog-about')
        #self.add_comment_to_post_url = reverse('add_comment_to_post')
        #self.add_anonymous_comment_to_post_url = reverse('add_anonymous_comment_to_post')
        #self.comment_approve_url = reverse('comment_approve')
        #self.comment_remove_url = reverse('comment_remove')
        #self.profile_remove_url = reverse('profile_remove')
        #self.profile_approve_url = reverse('profile_approve')
        #self.role_approve_url = reverse('role_approve')
        #self.role_remove_url = reverse('role_remove')
        #self.search_url = reverse('search')
        #self.Contact_url = reverse('Contact')

    #def test_profile_view_GET(self):
        #client = Client()

        #response = client.get(reverse('profile'))

        #self.assertEquals(response.status_code,204)

        #self.assertTemplateUsed(response,'users/profile.html')

    #def test_oldest_view_GET(self):
        #response = self.client.get(self.oldest_url)
        #self.assertEquals(response.status_code,204)
        #self.assertTemplateUsed(response,'blog/home.html')

    #def test_new_answer_view_GET(self):
        #response = self.client.get(self.new_answer_url)
        #self.assertEquals(response.status_code,204)
        #self.assertTemplateUsed(response,'blog/question.html')
