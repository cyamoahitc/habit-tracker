from rest_framework import generics
from django.contrib.auth.models import User

from users.serializers import UserSerializer


class UserListView(generics.ListAPIView):
    """
    View to list all users.
    """
    queryset = User.objects.filter(is_staff=False)  # Exclude admin users
    serializer_class = UserSerializer

