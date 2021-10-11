from django.db import models

# Create your models here.
class Notes(models.Model):
    fno=models.AutoField(primary_key=True)
    Title=models.TextField( default="")
    Disc=models.TextField( default="")
    Admin_Name=models.CharField(max_length=550)
    Admin_Email=models.CharField(max_length=550)
    Admin_Username=models.CharField(max_length=1000, default="")
    Timestamp_Created=models.CharField(max_length=505)
    
    Extras=models.TextField( default="")
    def __str__(self):
        return str(self.fno) +": "+ self.Admin_Name + " by " +self.Admin_Email
        



        








