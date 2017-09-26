from django.db import models
from django.utils import timezone
# Create your models here.
class RequestDetails(models.Model):
    request_date=models.DateTimeField(default=timezone.now)
    user_phone_number=models.CharField(max_length=20)
    user_email=models.EmailField(max_length=254)
    request_category=models.CharField(max_length=100)
    request_datetime=models.CharField(max_length=100) # should be a datetime field
    request_name=models.CharField(max_length=100)
    request_ownername=models.CharField(max_length=100)

    def create_request(self,number,email,category,date_time,name,owner):
        self.request_date=timezone.now()
        self.user_phone_number=number
        self.user_email=email
        self.request_category=category # Category is sent by form element to the view and then to this model function. We use this to filter the records as per user logged in
        self.request_datetime=date_time
        self.request_name=name
        self.request_ownername=owner # the user id of the service user
        self.save()
