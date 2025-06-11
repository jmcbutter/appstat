from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    url = models.URLField()
    linkedin = models.URLField()

    def __str__(self):
        return self.name

class JobDescription(models.Model):
    text = models.TextField()
    skills = models.TextField()
    experience = models.TextField()

class JobRequiredSkill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100)
    priority = models.IntegerField()
    job = models.ForeignKey('Job', on_delete=models.CASCADE, related_name='required_skills')

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    description = models.TextField()
# Create your models here.
