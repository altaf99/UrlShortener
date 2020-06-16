from hashlib import md5

from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from graphql import GraphQLError


class URL(models.Model):
    full_url = models.URLField(unique=True)
    url_hash = models.TextField(unique=True)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def clicked(self):
        self.clicks += 1
        self.save()

    # def save(self, *args, **kwargs):
    #     validate = URLValidator()
    #     try:
    #         validate(self.full_url)
    #     except ValidationError as e:
    #         raise GraphQLError('invalid url')

    #     return super().save(*args, **kwargs)