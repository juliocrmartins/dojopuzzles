from django.test import Client, TestCase
from django.urls import reverse

from ..models import Problem

# API definition
# /problems - List all problems
# /problems/published - List all published problems
# /problems/<slug> - Problem detail
# /problems/random - Redirect to a random problem detail page

class ProblemsAPITestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_problems_endpoint_exists(self):
        response = self.client.get(reverse('problems'))
        self.assertEqual(response.status_code, 200)


class ProblemsPublishedAPITestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_problems_published_endpoint_exists(self):
        response = self.client.get(reverse('problems-published'))
        self.assertEqual(response.status_code, 200)


class ProblemsDetailAPITestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_problems_detail_endpoint_exists(self):
        problem = Problem.objects.create(
            title='Problem Title',
            description='Problem Description',
            contributor='Contributor Name',
        )
        response = self.client.get(
            reverse('problems-detail', args=[problem.slug, ]))
        self.assertEqual(response.status_code, 200)


class ProblemsRandomAPITestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_problems_random_endpoint_exists(self):
        response = self.client.get(
            reverse('problems-random'))
        self.assertEqual(response.status_code, 200)


class ProblemsChooseAPITestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_problems_choose_endpoint_exists(self):
        problem = Problem.objects.create(
            title='Problem Title',
            description='Problem Description',
            contributor='Contributor Name',
        )

        response = self.client.get(
            reverse('problems-choose', args=[problem.slug, ]))
        self.assertEqual(response.status_code, 200)
