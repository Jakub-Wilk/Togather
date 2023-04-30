from togather.models import User
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q


class EmailAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(kwargs.get(User.EMAIL_FIELD), kwargs.get(User.USERNAME_FIELD))
            if not User.objects.filter(username=username).is_staff:
                return
        if username is None or password is None:
            return
        try:
            user = User._default_manager.get(
                Q(username__exact=username) | Q(email__iexact=username)
            )  # (Q(email__iexact=username) & Q(email_verified=True))
            if not user.is_staff and user.email != username:
                return
        except User.DoesNotExist:
            # run the default password hasher once to reduce the timing difference between an existing and a nonexistent user
            User().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
