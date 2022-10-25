from django.db import models
#from django.utils import timezone
from users.models import User

class Model2(models.Model):
    model_id = models.AutoField(primary_key=True)
    model_name = models.CharField("Models", max_length = 150)
    model_location = models.CharField("location", max_length = 50)
    model_file_name = models.CharField("Models file", max_length = 50)
    created_date =  models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    description = models.TextField("Description")

class Trends(models.Model):
    trends_id = models.AutoField(primary_key=True)
    trends_name = models.CharField("Trends", max_length = 150)
    trends_file_name = models.CharField("Trends file", max_length = 50)
    start_date =  models.DateTimeField(auto_now_add=True)  #юзер указывает 
    end_date =  models.DateTimeField(auto_now_add=True) # models.DateField(default=timezone.now().strftime("%Y-%m-%d")) #юзер указывает 
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    description = models.TextField("Description")

 
class Events(models.Model):
    events_id = models.AutoField(primary_key=True)
    events_name = models.CharField("Events", max_length = 150)
    trends_file_name = models.CharField("Events file", max_length = 50)
    created_date =  models.DateTimeField(auto_now_add=True)  #models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # дата создания 
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    description = models.TextField("Description")


class Scenario(models.Model):
    scenario_id = models.AutoField(primary_key=True)
    created_date =  models.DateTimeField(auto_now_add=True)# models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # дата создания models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    # run_date = models.DateTimeField
    # run_by = models.ForeignKey(User, on_delete=models.PROTECT)
    start_date = models.DateTimeField(auto_now_add=True) #юзер указывает 
    end_date = models.DateTimeField(auto_now_add=True) #юзер указывает 
    description = models.TextField("Description")
    model_id = models.ForeignKey(Model2,on_delete=models.PROTECT)
    trends_id = models.ForeignKey(Trends,on_delete=models.PROTECT)
    # scenario_config_id #таймстеп 
    events_id = models.ForeignKey(Events,on_delete=models.PROTECT)  

    # #таблица конфигов
    # загрузка через джейсон рест