from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()

# 新增这个部门模型
class Department(models.Model):
    title = models.CharField(max_length=32)