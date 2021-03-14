from rest_framework import generics, serializers
from .serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
  '''
  Create a new user in the system
  '''
  serializer_class = UserSerializer

  