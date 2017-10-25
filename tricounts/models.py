from django.db import models
from authentication.models import Account


class Tricount(models.Model):
    creator = models.ForeignKey(Account)
    name = models.CharField(max_length=50, null=False, blank=False)
    participants = models.ManyToManyField(Account)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.creator + ' ' + self.name


class Payment(models.Model):
    creator = models.ForeignKey(Account)
    amount = models.DecimalField(decimal_places=2)
    participants = models.ManyToManyField(Account)
    tricount = models.ForeignKey(Tricount)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.creator + ' ' + self.tricount.name
