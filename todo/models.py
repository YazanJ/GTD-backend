from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return str(self.name)

class Area(Tag):
    pass

class Contact(Tag):
    # first_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    created = models.DateTimeField(auto_now_add=True)

class Label(Tag):
    pass

class Project(models.Model):
    PARALLEL = 'PA'
    SEQUENTIAL = 'SE'

    next_action_choices = [
        (PARALLEL, 'Parallel'),
        (SEQUENTIAL, 'Sequential')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, default='Project Name')
    is_focused = models.BooleanField(blank=True, default=False)
    tags = models.ManyToManyField(Tag, blank=True)
    notes = models.TextField(blank=True)
    due_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, default=True)
    next_action = models.CharField(
        max_length=2, choices=next_action_choices, blank=True, default=PARALLEL)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Action(models.Model):
    energy_level_choices = [
        ('lo', 'Low'),
        ('md', 'Medium'),
        ('hi', 'High'),
        ('no', 'None')
    ]

    state_choices = [
        ('inbox', 'Inbox'),
        ('next', 'Next'),
        ('waiting', 'Waiting'),
        ('scheduled', 'Scheduled'),
        ('someday', 'Someday')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, default='To do')
    is_focused = models.BooleanField(blank=True, default=False)
    tags = models.ManyToManyField(Tag, blank=True)
    notes = models.TextField(blank=True)
    time_required = models.DurationField(blank=True, null=True)
    energy_required = models.CharField(
        max_length=2, choices=energy_level_choices, blank=True, default='no')
    due_date = models.DateField(blank=True, null=True)
    state = models.CharField(max_length=10, choices=state_choices, blank=True, default='inbox')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class ScheduledAction(Action):
    scheduled_for = models.DateTimeField()

