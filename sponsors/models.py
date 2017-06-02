from django.db import models


class Sponsor(models.Model):
    SPONSOR_PACKAGES = (('Bronze', 'Bronze - $500'),
                        ('Silver', 'Silver - $1000'),
                        ('Gold', 'Gold - $2000'),
                        ('Platinum', 'Platinum - $5000'),
                        ('Other', 'Other'),
                        )

    SPONSOR_TYPE =(('C', 'Corporate Sponsor'),
                   ('I', 'Individual Sponsor'),)

    name = models.CharField("sponsor name", max_length=200)
    category = models.CharField(max_length=15, choices=SPONSOR_PACKAGES)
    logo = models.ImageField(max_length=255, blank=True, null=True)
    type = models.CharField("sponsor type", max_length=1, choices=SPONSOR_TYPE)
    website = models.CharField("website URL/ Twitter handler", max_length=200, blank=True, null=True)

    class Meta:
        managed = True

    def __str__(self):
        return self.name

