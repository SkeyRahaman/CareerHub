from django.db import models
from django.utils.text import slugify
# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} from {self.company}"

class Location(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    zip = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.zip}, {self.country}"

class JobPost(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True) #add date when adding
    salary = models.IntegerField()
    slug = models.SlugField(null=True, max_length=40, unique=True)
    expiry = models.DateField(null=True)
    location = models.OneToOneField(Location,on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)
    type = models.CharField(max_length=200, null=False, choices=JOB_TYPE_CHOICES)

    def __str__(self) -> str:
        return f"{self.title} -> {self.salary}"
    
    def save(self, *args, **kwargs):
        if not self.id: # type: ignore
            self.slug = slugify(self.title)
        return super(JobPost, self).save(*args,**kwargs)

