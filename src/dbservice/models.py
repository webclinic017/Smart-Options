from django.db import models
from django.contrib.auth.views import UserModel

# Create your models here.
class RegisteredUsers(models.Model):
    user_name = models.ForeignKey(UserModel, on_delete = models.CASCADE)
    user_email = models.EmailField()
    user_phone = models.IntegerField()
    user_zerodha_id = models.CharField(max_length=128)

class UserPortfolio(models.Model):
    user_regid = models.ForeignKey(RegisteredUsers, on_delete = models.CASCADE)
    profit = models.IntegerField()

class UserTransactions(models.Model):
    user_regid = models.ForeignKey(RegisteredUsers, on_delete = models.CASCADE)
    trans_date = models.DateTimeField()
    option_range =  models.IntegerField()
    option_type = models.CharField(max_length=2) #PE or CE
    sell_price = models.FloatField()
    buy_price = models.FloatField()
    trans_profit = models.FloatField()

