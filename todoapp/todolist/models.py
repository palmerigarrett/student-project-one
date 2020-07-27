from django.db import models
from datetime import datetime
 
from django.utils import timezone
class Category(models.Model): # Category Class inherits models.Model
   name = models.CharField(max_length=100) #Like a varchar
   class Meta:
       verbose_name = ("Category")
       verbose_name_plural = ("Categories")
       ordering = ["name"]
   def __str__(self): # _str_ method will specify what to return when you call str() on am object
       return self.name # string to be shown when calling an instance of the Todo class

class Todo(models.Model): # Todo Class that inherits models.Model
    title = models.CharField(max_length=250) # a varchar
    content = models.TextField(blank=True) # a text field
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    dueness = models.IntegerField(default=0)
    progress = models.TextField(default="notStarted")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    class Meta:
       ordering = ["-created"] #ordering by the created field
    def __str__(self):
       return self.title #name to be shown when called
    def dueness_calculator(self):
        due, now = self.due_date, datetime.date(datetime.now())
        due_days = due - now
        self.dueness = int(due_days.days)
