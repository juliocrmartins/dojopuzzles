from django.http import HttpResponse

from rest_framework import generics
from rest_framework.response import Response

from .models import Problem
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


def problems_detail(request, slug):
    return HttpResponse(
        'Details of problem with slug {0}'.format(slug))


def problems_random(request):
    return HttpResponse(
        'Redirects to a random problem')


def problems_choose(request, slug):
    return HttpResponse(
        'Choose problem with slug {0}'.format(slug))
