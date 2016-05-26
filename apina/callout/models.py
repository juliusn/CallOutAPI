from __future__ import unicode_literals
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


class User(models.Model):
    email_address = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def __unicode__(self):
        return self.first_name + " " + self.last_name


class Beacon(models.Model):
    major = models.CharField(max_length=60, blank=True)
    minor = models.CharField(max_length=60, blank=True)
    uuid = models.CharField(max_length=70)

    def __str__(self):
        return self.uuid

    def __unicode__(self):
        return self.uuid


class Workspace(models.Model):
    creator = models.ForeignKey(
        'User',
        related_name='workspaces',
    )
    date_starting = models.DateField(null=True)
    date_ending = models.DateField(null=True)
    name = models.CharField(max_length=50)
    beacons = models.ManyToManyField(
        Beacon,
        blank=True,
        related_name='workspaces',
        )

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


@receiver(post_save, sender=Workspace)
def ensure_subscription_exists(instance, **kwargs):
    if kwargs.get('created', False):
        Subscription.objects.get_or_create(
            workspace=instance,
            user=instance.creator,
            role=2
        )


class Subscription(models.Model):
    ROLES = (
        (1, 'Attendee'),
        (2, 'Admin'),
    )
    role = models.IntegerField(
        choices=ROLES,
        default=1)
    feedback = models.TextField(max_length=1000, blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscriptions'
    )
    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE,
        related_name='subscriptions'
    )

    def __str__(self):
        return self.workspace.__str__() + " subscribed by " + self.user.__str__()

    def __unicode__(self):
        return self.workspace.__unicode__() + " subscribed by " + self.user.__unicode__()


@receiver(post_save, sender=Subscription)
def ensure_status_exists(instance, **kwargs):
    if kwargs.get('created', False):
        Status.objects.get_or_create(subscription=instance)


class Status(models.Model):
    subscription = models.ForeignKey(
        Subscription,
        on_delete=models.CASCADE,
        related_name='statuses')
    date_created = models.DateTimeField(auto_now_add=True)
    STATES = (
        ('F', 'Following'),
        ('U', 'Unsure'),
        ('R', 'Requesting assistance'),
    )
    state = models.CharField(max_length=1,
                             choices=STATES,
                             default='F')

    def __str__(self):
        return self.state

    def __unicode__(self):
        return self.state
