from django.db import models
from django.contrib.auth.models import AbstractUser


class Department(models.Model):
    #TODO if have more time make validation for only alpha in name
    DEP_MAX_CHARS = 50

    name = models.CharField(
        max_length=DEP_MAX_CHARS,
    )

    about = models.TextField()
    def __str__(self) -> str:
        return self.name


class JobTitle(models.Model):
    TITLE_MAX_CHARS = 50
    #TODO if have more time make validation for only alpha in name
    title = models.CharField(
        max_length=TITLE_MAX_CHARS,
    )

    def __str__(self) -> str:
        return self.title

class CustomUserModel(AbstractUser):
    NAME_MAX_CHARS = 51
    TELEPHONE_MAX_CHARS = 15
    LOCATION_MAX_CHARS = 100
    GENDERS = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('GF', 'Gender-fluid'),
        ('NB', 'Non-binary'),
    ]
    GENDER_MAX_CHARS = max(len(el) for _, el in GENDERS)

    SENIORITY_LEVELS = [
        ('REG', 'Regular'),
        ('JR', 'Junior'),
        ('MID', 'Middle'),
        ('SR', 'Senior'),
    ]
    SENIORITY_MAX_CHARS = max(len(el) for _, el in SENIORITY_LEVELS)

    email = models.EmailField(
        unique=True,
    )

    username = None
    
    first_name = models.CharField(
        max_length=NAME_MAX_CHARS,
        null=True,
        blank=False
    )

    last_name = models.CharField(
        max_length=NAME_MAX_CHARS,
        null=True,
        blank=False
    )

    date_of_birth = models.DateField(
        null=True,
        blank=False
    )

    gender = models.CharField(
        choices=GENDERS,
    )

    telephone_number = models.CharField(
        max_length=TELEPHONE_MAX_CHARS,
        null=True,
        blank=False
    )

    location = models.CharField(
        max_length=LOCATION_MAX_CHARS,
        null=True,
        blank=False
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        null=True,
    )

    job_title = models.ForeignKey(
        JobTitle,
        on_delete=models.RESTRICT,
        null=True,
        blank=False,
    )

    seniority = models.CharField(
        max_length=SENIORITY_MAX_CHARS,
        choices=SENIORITY_LEVELS,
        null=True,
        blank=False
    )

    date_of_hire = models.DateField(
        auto_now_add=True,
        
    )

    date_of_dismiss = models.DateField(
        blank=True,
        null=True,
    )

    is_hr = models.BooleanField(
        default=False,
    )

    is_eligible_for_payment = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', )

    def __str__(self):
        return self.get_full_name()