from django.db import IntegrityError
from django.test import TestCase

from .models import Problem


class ProblemTestCase(TestCase):

    def test_create_a_problem_with_minimum_required_fields(self):
        self.assertEqual(Problem.objects.count(), 0)
        problem = Problem.objects.create(
            title='Problem Title',
            description='Problem Description',
            contributor='Contributor Name',
        )
        self.assertEqual(Problem.objects.count(), 1)

    def test_new_problem_create_automatic_slug(self):
        problem = Problem.objects.create(
            title='Problem Title',
            description='Problem Description',
            contributor='Contributor Name',
        )
        self.assertEqual(problem.slug, 'problem-title')

    def test_automatic_slug_handling_special_characters(self):
        problem = Problem.objects.create(
            title='É um problemão com ç',
            description='Problem Description',
            contributor='Contributor Name',
        )
        self.assertEqual(problem.slug, 'e-um-problemao-com-c')

    def test_new_problem_unpublished_by_default(self):
        problem = Problem.objects.create(
            title='Problem Title',
            description='Problem Description',
            contributor='Contributor Name',
        )
        self.assertFalse(problem.published)

    def test_problem_title_must_be_unique(self):
        problem_title = 'Problem Title'

        problem = Problem.objects.create(
            title=problem_title,
            description='Problem Description',
            contributor='Contributor Name',
        )

        with self.assertRaises(IntegrityError):
            Problem.objects.create(
                title=problem_title,
                description='Problem Description',
                contributor='Contributor Name',
            )

    def test_problem_slug_must_be_unique(self):
        problem_slug = 'problem-title'
        problem = Problem.objects.create(
            title='Problem Title',
            description='Problem Description',
            contributor='Contributor Name',
            slug=problem_slug,
        )

        with self.assertRaises(IntegrityError):
            Problem.objects.create(
                title='Problem With Another Title',
                description='Problem Description',
                contributor='Contributor Name',
                slug=problem_slug,
            )

    def test_do_not_overwrite_provided_slug(self):
        problem_slug = 'i-am-forcing-this-slug'
        problem = Problem.objects.create(
            title='Problem Title',
            description='Problem Description',
            contributor='Contributor Name',
            slug=problem_slug,
        )
        self.assertEqual(problem.slug, problem_slug)
