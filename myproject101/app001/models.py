from django.db import models
from django.contrib.auth.models import User

STATUS = {
    "COMPLETED":"DONE",
    "NOT COMPLETED":"NOT DONE",
}

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=50)
    task = models.CharField(max_length=500)
    task_date = models.DateTimeField(auto_now_add=True)
    task_status = models.CharField(max_length=100, choices=STATUS)
    
    def formated_date(self):
        return f"{self.task_name} performed on {self.task_date.strftime('%d/%m/%Y at %H:%M')} by {self.user.first_name}"