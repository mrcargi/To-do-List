from django.contrib import admin
from .models import Task

# Register your models here.

class cattask(admin.ModelAdmin):
    exclude = ('creation_date', )
    list_display = ('title','description','complete',)




admin.site.register(Task,cattask)