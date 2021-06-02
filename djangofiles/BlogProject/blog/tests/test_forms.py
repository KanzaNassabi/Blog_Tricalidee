from django.test import SimpleTestCase
from blog.forms import (
                        CommentForm,
                        AnonymousCommentForm,
                        AnswerForm)



class TestForms(SimpleTestCase):

    def test_CommentForm_valid_data(self):
        form=CommentForm(data={
        'text':'Good Article'
        })

        self.assertTrue(form.is_valid())

    def est_CommentForm_no_data(self):
        form=CommentForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),3)

    def test_AnonymousCommentForm_valid_data(self):
        form=CommentForm(data={
        'author':'anonymous',
        'text':'Good'
        })
        self.assertTrue(form.is_valid())

    def test_AnonymousCommentForm_no_data(self):
        form=CommentForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),1)


    def test_AnswerForm_no_data(self):
        form=CommentForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),1)
