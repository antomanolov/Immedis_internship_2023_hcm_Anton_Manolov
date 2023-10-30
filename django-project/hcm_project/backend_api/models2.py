from django.db import models

class Department(models.Model):
    DEP_MAX_CHARS = 50

    name = models.CharField(
        max_length=DEP_MAX_CHARS,
    )

    about = models.TextField()


class JobTitle(models.Model):
    TITLE_MAX_CHARS = 50
    title = models.CharField(
        max_length=TITLE_MAX_CHARS,
    )
