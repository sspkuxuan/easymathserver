from django.db import models

# Create your models here.
class QuestionLib(models.Model):
    id = models.AutoField(primary_key=True)
    grade = models.IntegerField()
    question = models.CharField(max_length=512)
    choiceA = models.CharField(max_length=128)
    choiceB = models.CharField(max_length=128)
    choiceC = models.CharField(max_length=128)
    choiceD = models.CharField(max_length=128)
    answer = models.CharField(max_length=32)
class UserAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    openid = models.CharField(max_length=64)
    questionid = models.IntegerField()
    useranswer = models.CharField(max_length=64)


class MathUser(models.Model):
    openid = models.CharField(max_length=100,primary_key=True)
    telephone = models.CharField(max_length=12)
class ErrorAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    openid = models.CharField(max_length=64)
    questionid = models.IntegerField()
    useranswer = models.CharField(max_length=64)
    trueanswer = models.CharField(max_length=64)
class ErrorT(models.Model):
    id = models.AutoField(primary_key=True)
    openid = models.CharField(max_length=64)
    questionid = models.IntegerField()
    useranswer = models.CharField(max_length=128)
    trueanswer = models.CharField(max_length=128)
    qs = models.CharField(max_length=512)