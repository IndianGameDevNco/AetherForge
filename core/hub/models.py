from django.db import models  

class Project(models.Model):  
    name = models.CharField(max_length=100)  
    description = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)  
    language = models.CharField(max_length=50, default="Python")  

    def __str__(self):  
        return self.name  
