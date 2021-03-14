from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user: token')

def create_user(**params):
  return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
  """
  Test the users API without authentication
  """
  def setUp(self):
    self.client = APIClient()

  def test_create_valid_user_success(self):
    '''
    Test creatign user with valid payload is successful
    '''
    payload = {
      "email": "test@thisapp.com",
      "password": "testpassword",
      "name": "Test User"
    }
    res = self.client.post(CREATE_USER_URL, payload)

    self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    user = get_user_model().objects.get(**res.data)
    self.assertTrue(user.check_password(payload['password']))
    self.assertNotIn('password', res.data)

  def test_user_exist(self):
    '''
    Test creating user that already exists fails
    '''
    payload = {
      'email': 'test@thisapp.com',
      'password': 'testpassword'
    }
    create_user(**payload)

    res = self.client.post(CREATE_USER_URL, payload)
    self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

  def test_password_too_short(self):
    '''
    Test that the password entered must be atleast 8 character
    '''
    payload = {
      'email': 'test@thisapp.com',
      'password': 'pwd'
    }
    res = self.client.post(CREATE_USER_URL, payload)
    self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
    user_exists = get_user_model().objects.filter(
      email = payload['email']
    ).exists()
    self.assertFalse(user_exists)
