from django.db import models
from django.template.defaultfilters import slugify


class Problem(models.Model):

    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    contributor = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Problem, self).save(*args, **kwargs)