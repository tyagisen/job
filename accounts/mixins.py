from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.conf import settings
from django.contrib import messages


class SuperAdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        if user.is_super_admin or user.is_superuser:
            return True
        return False

    def handle_no_permission(self):
        messages.success(self.request, 'Please login superuser id.')
        return redirect(settings.LOGIN_URL)
