from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save



# Create your models here.

class post(models.Model):
    name = models.CharField(max_length=50)
    news = models.TextField()


class crtateuser(models.Model):
    ID_studen = models.CharField(max_length=10 ,primary_key=True)
    f_name = models.CharField( max_length=50)
    l_name = models.CharField( max_length=50)
    sa_name = models.CharField( max_length=50)
    Confirm_Password = models.CharField( max_length=50)
    Password = models.CharField( max_length=50)
    

    class Meta:
        verbose_name = 'crtateuser'
        verbose_name_plural = 'crtateusers'
    def __str__(self):
        return self.ID_studen +" "+ self.f_name +" "+ self.l_name+" "+self.sa_name

class LOGIN(models.Model):
    IDname = models.CharField(max_length=10 ,primary_key=True)
    fname = models.CharField( max_length=50)
    lname = models.CharField( max_length=50)
    saka = models.CharField( max_length=50)

    class Meta:
        verbose_name = 'LOGIN'
        verbose_name_plural = 'LOGIN'
        
    def __str__(self):
        return self.IDname +" "+self.fname+" "+self.lname+" "+self.saka


class test9(models.Model):
    strtest1 = models.CharField(max_length=50)
    strtest2 = models.CharField(max_length=50)
    strtest3 = models.CharField(max_length=50)

class study_group(models.Model):
    study_ID = models.CharField(max_length=8,primary_key=True)
    study_name = models.CharField(max_length=50)

class activity(models.Model):
    activity_ID = models.CharField(max_length=10,primary_key=True)
    activity_name = models.CharField(max_length=255)
    activity_Date = models.DateField()
    


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    idstuden = models.CharField(max_length=10)
    fieldstudy = models.CharField(max_length=255)
    def __str__(self):
         return self.user.username

    def create_profile(sender,**kwargs):
        if kwargs['created']:
            user_profile=Profile.objects.create(user=kwargs['instance'])
    post_save.connect(create_profile,sender=User)

class add_ativity(models.Model):
    activity_name = models.CharField(max_length=255)
    activity_Date = models.CharField(max_length=50)
    activity_data = models.CharField(max_length=255)
    def __str__(self):
         return self.activity_name

class add_data(models.Model):
    id_name = models.CharField(max_length=255)
    activity = models.CharField(max_length=255)
    Date = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ('id_name', 'activity')

    def __str__(self):
         return self.id_name+" "+self.activity

class add_data_all(models.Model):
    add_user_name = models.CharField(max_length=255)
    add_Id_studen = models.CharField(max_length=255)
    add_f_name = models.CharField(max_length=255)
    add_l_name = models.CharField(max_length=255)
    add_fieldstudy = models.CharField(max_length=255)
    add_activity = models.CharField(max_length=255)
    add_id_activity = models.CharField(max_length=255)
    def __str__(self):
         return self.add_user_name+" "+self.add_f_name+" "+self.add_l_name+" "+self.add_activity+" "+self.add_id_activity