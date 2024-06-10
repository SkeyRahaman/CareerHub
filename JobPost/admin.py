from django.contrib import admin
from .models import JobPost, Location, Author, Skill

# Register your models here.
admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skill)
