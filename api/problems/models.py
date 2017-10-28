from django.db import models
from django.template.defaultfilters import slugify


class Problem(models.Model):

    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    contributor = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def choose(self):
        if self.published:
            ProblemChosen.objects.create(problem=self)
        else:
            raise ValueError('Problem must be published to be chosen')

    @property
    def chosen(self):
        return ProblemChosen.objects.filter(problem=self).count()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse(
            'problems-detail', args=[self.slug, ])


class ProblemChosen(models.Model):

    problem = models.ForeignKey('Problem')
    chosen_date = models.DateField(auto_now=True)
