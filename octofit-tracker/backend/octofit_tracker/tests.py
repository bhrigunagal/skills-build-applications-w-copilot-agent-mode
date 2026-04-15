from django.test import TestCase
from rest_framework.test import APIClient
from .models import User, Team, Activity, Leaderboard, Workout

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        User.objects.create(name="Test User", email="test@example.com", team="Marvel")
        Team.objects.create(name="Marvel", members=["Test User"])
        Activity.objects.create(user="Test User", activity="Test Activity", duration=10)
        Leaderboard.objects.create(user="Test User", points=50)
        Workout.objects.create(name="Test Workout", suggested_for=["Test User"])

    def test_users_endpoint(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)

    def test_teams_endpoint(self):
        response = self.client.get('/teams/')
        self.assertEqual(response.status_code, 200)

    def test_activities_endpoint(self):
        response = self.client.get('/activities/')
        self.assertEqual(response.status_code, 200)

    def test_leaderboard_endpoint(self):
        response = self.client.get('/leaderboard/')
        self.assertEqual(response.status_code, 200)

    def test_workouts_endpoint(self):
        response = self.client.get('/workouts/')
        self.assertEqual(response.status_code, 200)

    def test_api_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
