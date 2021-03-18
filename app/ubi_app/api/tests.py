from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient, APIRequestFactory

from .models import Occurrence
import datetime
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class TestSuite(APITestCase):

    def setUp(self):
        """ Set up """
        self.admin = User.objects.create_user(
            username="admin", password="password", is_superuser=False, is_staff=True)

        self.user_one = User.objects.create_user(
            username="user_one", password="password", is_superuser=False, is_staff=False)

        self.user_two = User.objects.create_user(
            username="user_two", password="password", is_superuser=False, is_staff=False)

        self.occurrence_one = Occurrence.objects.create(
            description="occurrence one - user one", lat=40.639293, lon=-8.748694, category="CONSTRUCTION", author=self.user_one)

        self.occurrence_two = Occurrence.objects.create(
            description="occurrence two - user one", lat=40.630142,  lon=-8.746905, category="INCIDENT", author=self.user_one)

        self.occurrence_three = Occurrence.objects.create(
            description="occurrence three - user two", lat=40.643290,  lon=-8.651065, category="INCIDENT", author=self.user_two)

    def test_user_created_with_success(self):
        """Ensure that the users are created on set up """

        users = User.objects.all()
        self.assertEqual(len(users), 3)

    def test_occurrence_created_with_success(self):
        """Ensure that the occurrences are created on set up """

        occurrences = Occurrence.objects.all()
        self.assertEqual(len(occurrences), 3)

    def test_user_one_creates_occurrence(self):
        """ User one creates a new occurrence """
        login = self.client.login(username="user_one", password="password")

        data = {
            "description": "simple description for unit test",
            "lat": 40.640507,
            "lon": -8.653754,
            "category": "CONSTRUCTION",
            "author": self.user_one.pk
        }

        response = self.client.post("/occurrences/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Occurrence.objects.count(), 4)

    def test_user_two_creates_occurrence(self):
        """ User two creates a new occurrence """
        login = self.client.login(username="user_two", password="password")

        data = {
            "description": "simple description for unit test",
            "lat": 40.635711,
            "lon": -8.715310,
            "category": "INCIDENT",
            "author": self.user_one.pk
        }

        response = self.client.post("/occurrences/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Occurrence.objects.count(), 4)

    def test_get_all_occurrences(self):
        """ User one gets all the occurrences in the system """
        login = self.client.login(username="user_one", password="password")

        response = self.client.get(
            "/occurrences/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_get_all_occurrences_without_authentication(self):
        """ User one tries to get all the occurrences in the system, but doesn't have authentication """
        response = self.client.get(
            "/occurrences/")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_all_occurrences_by_author(self):
        """ User one gets all the occurrences in the system by author """
        login = self.client.login(username="user_one", password="password")

        response = self.client.get(
            "/occurrences/", {"author": self.user_one.pk})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_all_occurrences_by_category(self):
        """ User one gets all the occurrences in the system by category """
        login = self.client.login(username="user_one", password="password")

        response = self.client.get(
            "/occurrences/", {"category": "INCIDENT"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_all_occurrences_by_location_in_km(self):
        """ User one gets all the occurrences in the system by distance in km """
        login = self.client.login(username="user_one", password="password")

        response = self.client.get(
            "/occurrences/", {"distance": 1})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_occurrence_status_use_one(self):
        """ User one tries to update an occurrence, but doesn't have authentication """
        login = self.client.login(username="user_one", password="password")

        data = {
            "status": "VALIDADA"
        }

        response = self.client.put(
            '/occurrence/{}/'.format(self.occurrence_one.pk), data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_occurrence_status_admin(self):
        """ User admin updates an occurrence """
        login = self.client.login(username="admin", password="password")

        data = {
            "status": "VALIDADA",
            "author": self.user_one.pk
        }

        response = self.client.put(
            '/occurrence/{}/'.format(self.occurrence_one.pk), data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "VALIDADA")
