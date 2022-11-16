from email.policy import default
from enum import unique

from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime, date
from accounts.models import *
from django.contrib.auth.models import User



# 성별 
# 운동 
# 모집인원
# 운동할날짜

# 운동 종류 
# class Exercise(models.Model):
#     Soccer = "축구"
#     BasketBall = "농구"
#     VolleyBall = "배구"
#     BaseBall = "야구"
#     Tennis = "테니스"
#     Badminton = "배드민턴"
#     Running = "산책/러닝"
    
#     EXERCISE_CHOICES = [
#     (Soccer, '축구'),
#     (BasketBall, '농구'),
#     (VolleyBall, '배구'),
#     (BaseBall, '야구'),
#     (Tennis, '테니스'),
#     (Badminton, '배드민턴'),
#     (Running, '산책/러닝'),
#     ]
    
#     exercise_choices = models.CharField(
#         max_length=10,
#         choices=EXERCISE_CHOICES,
#         default=Soccer,
#     )
class Exercise(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default="")
    
    
    def __str__(self):
        return self.name
    
class Sex(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default="")
    
    
    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    writer = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length = 300, default="")
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now=True, verbose_name="등록(수정)일")
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, blank=True, null=True)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE, blank=True, null=True) 
    count = models.IntegerField(null="True")
    countB = models.IntegerField(null="True")
    flag_enddate = models.BooleanField(default=False)
    # 좋아요
    like_user_set = models.ManyToManyField(User, blank=True, related_name='likes_user_set',through='Like')
    dislike_user_set = models.ManyToManyField(User, blank=True, related_name='dislikes_user_set',through='Dislike')
    # 같이 운동할 날짜
    start_date = models.DateField(auto_now=True,editable=True)
    end_date = models.DateField(auto_now=False,editable=True)
    # 모집마감
    completed = models.BooleanField(default=False)
    
    # 모집하는 시간 
    start_time = models.TimeField(default="12", editable=True)
    end_time = models.TimeField(default="12", editable=True)

    def duration(self):
        return self.end_date - self.start_date

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:20]

    @property
    def like_count(self):
        return self.like_user_set.count()

    @property
    def dislike_count(self):
        return self.dislike_user_set.count()
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user','post'))




class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
         unique_together = (('user', 'post'))