# encoding:utf-8
from __future__ import unicode_literals
from django.db import models

from django import utils
# Create your models here.
class User(models.Model):
    college=models.CharField(blank=True,null=True,max_length=32)
    major=models.CharField(blank=True,null=True,max_length=32)
    in_year=models.IntegerField(blank=True,null=True,default=0)
    campus=models.CharField(blank=True,null=True,max_length=16)

    nickname = models.CharField(blank=True,null=True,max_length=20,)
    contact=models.CharField(blank=True,null=True,max_length=40,default='None')
    student_id = models.CharField(blank=True, null=True, max_length=64)
    username = models.CharField(max_length=20,primary_key=True )#主码
    password = models.CharField(max_length=20, )
    image = models.ImageField(blank=True, null=True,upload_to='')
    states = (
        (0, "using"),
        (1, "closed"),
    )
    state = models.IntegerField(blank=True, null=True, choices=states,default=0)

    num=models.IntegerField(default=0)
    description=models.CharField(blank=True, null=True,max_length=200)

class Book(models.Model):
    ways = (
        (0, 'cancle'),
        (1, u'面交'),
        (2, u'快递'),
        (3, u'面交或快递'),
    )
    bookname = models.CharField(blank=True,null=True,max_length=20,)
    author=models.CharField(blank=True,null=True,max_length=20,)
    publisher=models.CharField(blank=True,null=True,max_length=20,)
    price = models.FloatField(blank=True,null=True,max_length=24)
    description=models.TextField(blank=True,null=True,)
    way=models.IntegerField(blank=True,null=True,choices=ways)
    picture=models.ImageField(blank=True,null=True,upload_to='',default='logo.png')
    seller= models.ForeignKey(User)
    states = (
        (0, 'on sale'),
        (1, 'sold'),
        (2, 'cancle'),
    )
    state = models.IntegerField(blank=True, null=True,choices=states,default=0)


#class relation(models.Model):
#   seller_name=models.CharField(blank=True,null=True,max_length=20,)
#    buyer_name=models.CharField(blank=True,null=True,max_length=20,)
#    book_id=models.CharField(blank=True,null=True,max_length=20,)
#    date=models.DateField(blank=True,null=True)
#    state=models.IntegerField(blank=True,null=True,default=0)
#    comment=models.CharField(blank=True,null=True,max_length=200,default='None')

class s_b(models.Model):
    user_id = models.CharField(blank=True, null=True, max_length=20, )
    book_id = models.CharField(blank=True, null=True, max_length=20, )
    relation = models.CharField(blank=True, null=True,max_length=10)

class Order(models.Model):
    states = (
        (0, 'buy'),
        (1, 'cancle'),
    )
    seller_name = models.CharField(blank=True, null=True, max_length=20, )
    buyer_name = models.CharField(blank=True, null=True, max_length=20, )
    seller_id = models.CharField(blank=True, null=True, max_length=64, )
    buyer_id = models.CharField(blank=True, null=True, max_length=64, )
    book_id=models.CharField(max_length=20)
    bookname = models.CharField(blank=True, null=True, max_length=20, )
    picture = models.ImageField(blank=True, null=True, upload_to='', default='logo.png')
    price = models.FloatField(blank=True,null=True,max_length=24)
    date=models.DateField(blank=True,null=True,default=utils.timezone.now)

    state=models.IntegerField(blank=True,null=True,default=0,choices=states)

    comment = models.CharField(blank=True, null=True, max_length=200, default='None')
    score=models.IntegerField(blank=True,null=True,default=0)
    anonymous=models.BooleanField(default=False)
    c_time=models.IntegerField(blank=True, null=True )
    tobuyer_comment = models.CharField(blank=True, null=True, max_length=200, default='None')
    tobuyer_score = models.IntegerField(blank=True, null=True, default=0)
    tobuyer_anonymous = models.BooleanField(default=False)
    tobuyer_c_time=models.IntegerField(blank=True, null=True)

    buyer_image = models.ImageField(blank=True, null=True,upload_to='')
    seller_image = models.ImageField(blank=True, null=True,upload_to='')

    ways = (
        (0, 'cancle'),
        (1, u'面交'),
        (2, u'快递'),
        (3, u'面交或快递'),
    )
    way=models.IntegerField(blank=True,null=True,choices=ways)