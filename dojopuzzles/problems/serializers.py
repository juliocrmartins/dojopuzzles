from django.urls import reverse
from rest_framework import serializers

from .models import Problem


class ProblemSerializer(serializers.ModelSerializer):

    chosen = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    class Meta:
        model = Problem
        exclude = ('id', )

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    def get_url(self, problem):
        request = self.context.get('request')
        return request.build_absolute_uri(
            reverse('problems-detail', args=[problem.slug, ]))

    def get_chosen(self, problem):
        return problem.chosen
