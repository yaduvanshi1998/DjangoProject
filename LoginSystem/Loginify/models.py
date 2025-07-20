from django.db import models

# Create your models here.

class UserDetails(models.Model):
    Username = models.CharField(max_length=50, primary_key=True)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=12, blank=True)

    # Providing the customized table name
    class Meta:
        db_table = 'UserDetails'
    
    # Saving the data with username
    def __str__(self):
        return self.Username

    