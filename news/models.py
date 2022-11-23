from django.db import models

# Create your models here.

class Journalist(models.Model): 
    first_name= models.CharField(max_length=60)
    last_name= models.CharField(max_length=60)
    biograpy= models.TextField(blank=True)
    
    
    def __str__(self):
        return f"{ self.first_name } { self.last_name }"  
    
class Article(models.Model):
    author= models.ForeignKey(Journalist, 
                              on_delete=models.CASCADE,
                              related_name="articles")
    title= models.CharField(max_length=120)
    description= models.CharField(max_length=120)
    body= models.TextField()
    location= models.CharField(max_length=120)
    publication_date = models.DateField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return f"{self.author } {self.title }" 

class JobOffer(models.Model):

    company_name= models.CharField(max_length=120)
    company_email= models.EmailField(max_length=120)
    job_title= models.CharField(max_length=120)
    job_description= models.CharField(max_length=120)
    salary = models.PositiveBigIntegerField()
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return f"{self.company_name } {self.job_title }" 


