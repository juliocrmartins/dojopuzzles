import datetime

from django.db import IntegrityError
from django.test import TestCase

from ..models import Problem, ProblemChosen


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

    def test_register_when_a_problem_is_chosen(self):
        self.assertEqual(ProblemChosen.objects.count(), 0)
        problem = Problem.objects.create(
            title='Problem Title',
            description='Problem Description',
            contributor='Contributor Name',
            published=True,
        )
        problem.choose()
        self.assertEqual(
            ProblemChosen.objects.filter(problem=problem).count(), 1)
        problem.choose()
        self.assertEqual(
            ProblemChosen.objects.filter(problem=problem).count(), 2)

    def test_get_number_of_times_a_problem_is_chosen(self):
        self.assertEqual(ProblemChosen.objects.count(), 0)
        problem = Problem.objects.create(
            title='Problem Title',
            description='Problem Description',
            contributor='Contributor Name',
            published=True,
        )
        problem.choose()
        problem.choose()
        problem.choose()
        problem.choose()

        self.assertEqual(problem.chosen, 4)

    def test_unpublished_problem_can_not_be_chosen(self):
        problem = Problem.objects.create(
            title='Problem Title',
            description='Problem Description',
            contributor='Contributor Name',
            published=False
        )
        with self.assertRaises(ValueError):
            problem.choose()


class ProblemChosenTestCase(TestCase):

    def setUp(self):
        self.problem = Problem.objects.create(
            title='Problem Title',
            description='Problem Description',
            contributor='Contributor Name',
        )

    def test_create_a_problem_chosen_register(self):
        self.assertEqual(ProblemChosen.objects.count(), 0)
        ProblemChosen.objects.create(
            problem=self.problem,
        )
        self.assertEqual(ProblemChosen.objects.count(), 1)

    def test_chosen_date_defaults_to_today(self):
        today = datetime.date.today()
        problem_chosen = ProblemChosen.objects.create(
            problem=self.problem,
        )
        self.assertEqual(problem_chosen.chosen_date, today)
