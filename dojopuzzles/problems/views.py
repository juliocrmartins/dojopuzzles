from django.http import HttpResponseForbidden, \
    HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse

from rest_framework import generics

from .models import Problem, ProblemChosen
from .serializers import ProblemSerializer


class ProblemsList(generics.ListAPIView):

    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()

        fields = self.request.GET.get('fields', None)
        if fields is not None:
            fields = tuple(fields.split(','))

        kwargs['context'] = self.get_serializer_context()
        kwargs['fields'] = fields

        return serializer_class(*args, **kwargs)


class PublishedProblemsList(ProblemsList):

    queryset = Problem.objects.filter(published=True)


class ProblemsDetail(generics.RetrieveUpdateAPIView):

    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    lookup_field = 'slug'

    def patch(self, request, *args, **kwargs):
        problem = Problem.objects.get(slug=kwargs.get('slug', ''))

        if not problem.published:
            return HttpResponseForbidden()
        else:
            ProblemChosen.objects.create(problem=problem)
            return JsonResponse({})


class ProblemsRandom(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        problem = Problem.objects.filter(published=True).order_by('?').first()

        if problem is None:
            return HttpResponseNotFound()

        return redirect(
            reverse('problems-detail', args=[problem.slug, ]))
