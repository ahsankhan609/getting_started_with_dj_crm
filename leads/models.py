from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
    # If we want another field to be added to the User model then we simply do this: The makemigrations and migrate
    # cellphone = models.CharField(max_length=100)

class Lead(models.Model):
    SOURCE_CHOICES = (
        ('YouTube', 'YouTube'),
        ('Google', 'Google'),
        ('NewsLetter', 'Newsletter'),
        ('TikTok', 'TikTok'),
        ('Twitter', 'Twitter'),
        ('Facebook', 'Facebook'),
        ('Friend', 'Friend')
    )
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    age = models.IntegerField()
    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES,max_length=100)
    #profile_picture = models.ImageField(blank=True,null=True)
    special_files = models.FileField(blank=True,null=True)
    #agent = models.ForeignKey('Agent', on_delete=models.SET_DEFAULT,default='Agent Left') # It will add default value if we delete any agent.
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Create only one user for this agent
    #profile_picture = models.ImageField(blank=True,null=True)
    #age = models.IntegerField(default=18, validators=[MinValueValidator(18), MaxValueValidator(60)])
    
    def __str__(self):
        return self.user.email
