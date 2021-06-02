from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users import views as user_views
from django.contrib.auth import views as auth_views


class TestUrls(SimpleTestCase):

    def test_register_path_resolved(self):
        path = reverse('register')
        self.assertEquals(resolve(path).func, user_views.register)

    def test_profile_path_resolved(self):
        path = reverse('profile')
        self.assertEquals(resolve(path).func, user_views.profile)

    def test_login_path_resolved(self):
        path = reverse('login')
        self.assertEquals(resolve(path).func.view_class, auth_views.LoginView)

    def test_logout_path_resolved(self):
        path = reverse('logout')
        self.assertEquals(resolve(path).func.view_class, auth_views.LogoutView)

    def test_password_reset_path_resolved(self):
        path = reverse('password_reset')
        self.assertEquals(resolve(path).func.view_class, auth_views.PasswordResetView)

    def test_password_reset_done_path_resolved(self):
        path = reverse('password_reset_done')
        self.assertEquals(resolve(path).func.view_class, auth_views.PasswordResetDoneView)

    def test_password_reset_complete_path_resolved(self):
        path = reverse('password_reset_complete')
        self.assertEquals(resolve(path).func.view_class, auth_views.PasswordResetCompleteView)
