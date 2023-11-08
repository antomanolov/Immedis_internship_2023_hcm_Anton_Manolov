from django.db import models
from hcm_project.backend_api.appuser import AppUser

# work models
class Payroll(models.Model):
    gross_salary = models.DecimalField(
        max_digits=9,
        decimal_places=2
    )
    taxes = models.DecimalField(
        max_digits=9,
        decimal_places=2
    )
    deductions = models.DecimalField(
        max_digits=9,
        decimal_places=2
    )
    bonuses = models.DecimalField(
        max_digits=9,
        decimal_places=2
    )
    net_salary = models.DecimalField(
        max_digits=9,
        decimal_places=2
    )
    day_of_monthly_payment = models.PositiveIntegerField()

    payed_on = models.DateField(
        auto_now_add=True,
    )
    
    employee = models.ForeignKey(
        AppUser,
        on_delete=models.RESTRICT
    )

    def __str__(self) -> str:
        return self.net_salary

# leave/attendance models

class LeaveBallance(models.Model):
    #TODO research how to make the relation on the moment the user is created!
    DEFAULT_ANNUAL_SICK_LEAVE = 20
    DEFAULT_MARRIAGE_LEAVE = 7
    DEFAULT_FUNERAL_LEAVE = 2
    

    annual_ballance = models.PositiveIntegerField(
        default=DEFAULT_ANNUAL_SICK_LEAVE,
    )

    marriage_ballance = models.PositiveIntegerField(
        default=DEFAULT_MARRIAGE_LEAVE,
    )

    funeral_ballance = models.PositiveIntegerField(
        default=DEFAULT_FUNERAL_LEAVE,
    )

    sick_ballance = models.PositiveIntegerField(
        default=DEFAULT_ANNUAL_SICK_LEAVE,
    )

    employee = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f'Leave ballance for {self.employee} with ID:{self.employee.pk}'

class LeaveRequest(models.Model):
    #TODO if have more time make validation for requesting no more days than the
    # days left of every leave type!

    SICK_LEAVE = 'sick leave'
    ANNUAL_LEAVE = 'anual leave'
    FUNERAL_LEAVE = 'funeral leave'
    MARRIAGE_LEAVE = 'marriage leave'
    LEAVE_TYPES = [(el, el) for el in (SICK_LEAVE, ANNUAL_LEAVE, FUNERAL_LEAVE, MARRIAGE_LEAVE)]
    LEAVE_MAX_CHARS = max(len(el) for _, el in LEAVE_TYPES)

    type_of_leave = models.CharField(
        max_length=LEAVE_MAX_CHARS,
        choices=LEAVE_TYPES,
    )

    days_needed = models.PositiveIntegerField()
    
    status = models.CharField(
        max_length=20,
        default='Pending',
    )

    starting_date = models.DateField()
    ending_date = models.DateField()

    employee = models.ForeignKey(
        AppUser,
        on_delete=models.RESTRICT,
    )

class LeaveHistory:
    #TODO this is made to put every leave by date and to show who approved the leave
    #TODO try what happens when deleting the user that approved the request 
    # in different scenarios
    
    approved_on_date = models.DateTimeField(
        auto_now_add=True,
    )
    
    leave_request = models.OneToOneField(
        LeaveRequest,
        on_delete=models.RESTRICT,
    )
    
    approved_by = models.ForeignKey(
        AppUser,
        on_delete=models.RESTRICT
    )


class Attendance(models.Model):
    check_in = models.TimeField(
        auto_now_add=True,
    )
    
    check_out = models.TimeField()
    
    current_date = models.DateField(
        auto_now_add=True
    )

    employee = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
    )

    

#Performance review and tasks

class PerformanceReview(models.Model):
    #TODO make validations for the min/max review points!
    
    review_points = models.PositiveIntegerField()
    
    feedback = models.TextField()
    
    goals_achieved = models.TextField()
    
    improvement_areas = models.TextField()
    
    employee = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        related_name= 'reviewed_employees_set'
    )
    
    reviewed_by = models.ForeignKey(
        AppUser,
        on_delete=models.RESTRICT,
        related_name= 'reviewers_set'
    )

class Task(models.Model):
    NAME_MAX_CHARS = 50

    name = models.CharField(
        max_length=NAME_MAX_CHARS,
    )

    description = models.TextField()
    pushed_on = models.DateTimeField(
        auto_now_add=True,
    )
    deadline = models.DateField()
    
    employee = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        related_name='tasked_employees_set'
    )

    tasked_by = models.ForeignKey(
        AppUser,
        on_delete=models.RESTRICT,
        related_name= 'taskers_set'
    )

