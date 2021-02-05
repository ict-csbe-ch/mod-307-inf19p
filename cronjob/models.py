from django.db import models


class Cronjob(models.Model):
    title = models.CharField(max_length=255,  null=False)
    address = models.CharField(max_length=255,  null=False)
    notification = models.CharField(max_length=45,  null=False)
    minute = models.CharField(max_length=45)
    hour = models.CharField(max_length=45)
    weekday = models.CharField(max_length=45)
    month = models.CharField(max_length=45)
    day = models.CharField(max_length=45)
    user = models.ForeignKey("User", on_delete=models.RESTRICT)


class Address(models.Model):
    street = models.CharField(max_length=255,  null=False)
    strassenNr = models.CharField(max_length=10,  null=False)
    plz = models.ForeignKey("Ort", on_delete=models.RESTRICT)


class Ort(models.Model):
    plz = models.CharField(max_length=25, null=False)
    name = models.CharField(max_length=255, null=False)


class User(models.Model):
    email = models.CharField(max_length=25, null=False)
    firstName = models.CharField(max_length=25, null=False)
    lastName = models.CharField(max_length=25, null=False)
    password = models.CharField(max_length=25, null=False)
    address = models.ForeignKey("Address", on_delete=models.RESTRICT)
     def __str__(self):
        return f'{self.firstName} {self.lastName} {self.address} {self.email}'
