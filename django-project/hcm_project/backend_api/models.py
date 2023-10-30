from django.db import models
from django.contrib.auth.models import AbstractUser
from hcm_project.backend_api.models2 import Department, JobTitle



class CustomUserModel(AbstractUser):
    NAME_MAX_CHARS = 50
    TELEPHONE_MAX_CHARS = 15
    LOCATION_MAX_CHARS = 100
    GENDERS = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('GF', 'Gender-fluid'),
        ('NB', 'Non-binary'),
    ]
    GENDER_MAX_CHARS = len(max(el for _, el in GENDERS))

    SENIORITY_LEVELS = [
        ('REG', 'Regular'),
        ('JR', 'Junior'),
        ('MID', 'Middle'),
        ('SR', 'Senior'),
    ]
    SENIORITY_MAX_CHARS = len(max(el for _, el in SENIORITY_LEVELS))

    email = models.EmailField(
        unique=True,
    )
    
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
