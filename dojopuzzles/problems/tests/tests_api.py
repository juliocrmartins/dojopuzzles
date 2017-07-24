from django.test import Client, TestCase
from django.urls import reverse

from ..models import Problem


class ProblemsAPITestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_problems_endpoint_exists(self):
        response = self.client.get(reverse('problems'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_returns_all_problems(self):
        problem1 = Problem.objects.create(
            title='Problem Title 1',
            description='Problem Description',
            contributor='Contributor Name',
        )
        problem2 = Problem.objects.create(
            title='Problem Title 2',
            description='Problem Description',
            contributor='Contributor Name',
        )

        response = self.client.get(reverse('problems'))

        self.assertEqual(response.json(), [
            {
                'title': problem1.title,
                'description': problem1.description,
                'contributor': problem1.contributor,
                'published': problem1.published,
                'slug': problem1.slug,
                'url': response.wsgi_request.build_absolute_uri(
                    reverse('problems-detail', args=[problem1.slug, ])),
                'chosen': 0,
            },
            {
                'title': problem2.title,
                'description': problem2.description,
                'contributor': problem2.contributor,
                'published': problem2.published,
                'slug': problem2.slug,
                'url': response.wsgi_request.build_absolute_uri(
                    reverse('problems-detail', args=[problem2.slug, ])),
                'chosen': 0,
            },
        ])

    def test_able_to_specify_which_fields_to_return(self):
        problem1 = Problem.objects.create(
            title='Problem Title 1',
            description='Problem Description',
            contributor='Contributor Name',
        )

        response = self.client.get(
            reverse('problems'),
            {'fields': 'title,url'}
        )

        self.assertEqual(response.json(), [
            {
                'title': problem1.title,
                'url': response.wsgi_request.build_absolute_uri(
                    reverse('problems-detail', args=[problem1.slug, ]))
            },
        ])


class ProblemsPublishedAPITestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_problems_published_endpoint_exists(self):
        response = self.client.get(reverse('problems-published'))
        self.assertEqual(response.status_code, 200)

    def test_returns_only_published_problems(self):
        problem = Problem.objects.create(
            title='Problem Title 1',
            description='Problem Description',
            contributor='Contributor Name',
            published=False,
        )
        response = self.client.get(reverse('problems-published'))
        self.assertEqual(response.json(), [])

        problem.published = True
        problem.save()

        response = self.client.get(reverse('problems-published'))
        self.assertEqual(response.json(), [
            {
                'title': problem.title,
                'description': problem.description,
                'contributor': problem.contributor,
                'published': problem.published,
                'slug': problem.slug,
                'url': response.wsgi_request.build_absolute_uri(
                    reverse('problems-detail', args=[problem.slug, ])),
                'chosen': 0,
            },
        ])


class ProblemsDetailAPITestCase(TestCase):

    def setUp(self):
        self.client = Client()

        self.problem = Problem.objects.create(
            title='Problem Title',
            description='Problem Description',
            contributor='Contributor Name',
        )

    def test_problems_detail_endpoint_exists(self):
        response = self.client.get(
            reverse('problems-detail', args=[self.problem.slug, ]))
        self.assertEqual(response.status_code, 200)

    def test_should_return_problem_details(self):
        response = self.client.get(
            reverse('problems-detail', args=[self.problem.slug, ]))

        self.assertEqual(response.json(), {
            'title': self.problem.title,
            'description': self.problem.description,
            'contributor': self.problem.contributor,
            'published': self.problem.published,
            'slug': self.problem.slug,
            'url': response.wsgi_request.build_absolute_uri(
                reverse('problems-detail', args=[self.problem.slug, ])),
            'chosen': 0,
        })


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
            published=True,
        )

        response = self.client.patch(
            reverse('problems-choose', args=[problem.slug, ]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {})

    def test_should_increase_chosen_number(self):
        problem = Problem.objects.create(
            title='Problem Title',
            description='Problem Description',
            contributor='Contributor Name',
            published=True,
        )
        self.assertEqual(problem.chosen, 0)

        self.client.patch(
            reverse('problems-choose', args=[problem.slug, ]))

        problem = Problem.objects.get(pk=problem.pk)
        self.assertEqual(problem.chosen, 1)

    def test_can_not_chose_unpublished(self):
        problem = Problem.objects.create(
            title='Problem Title',
            description='Problem Description',
            contributor='Contributor Name',
            published=False
        )
        self.assertEqual(problem.chosen, 0)

        response = self.client.patch(
            reverse('problems-choose', args=[problem.slug, ]))

        self.assertEqual(response.status_code, 403)

        problem = Problem.objects.get(pk=problem.pk)
        self.assertEqual(problem.chosen, 0)
