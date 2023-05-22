from django.db import models

# Create your models here.
class Doctor(models.Model):
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email

class Pacient(models.Model):
    name = models.CharField(max_length=150)
    age = models.TextField()
    diagnostico = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.CharField(max_length=200)
    diagnostico = models.TextField()
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE)

    def __str__(self):
        return self.title