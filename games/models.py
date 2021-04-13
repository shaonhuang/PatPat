from django.db import models

# Create your models here.
class Gameinfo(models.Model):
    # id
    game_id = models.AutoField(primary_key=True)

    # 游戏名称
    name = models.CharField(max_length=200,blank=False)

    # 简介
    summary = models.CharField(max_length=500,blank=False)

    # 评论人数
    comment_num = models.IntegerField()

    # 上架时间
    date = models.DateTimeField()

    # 图标
    icon = models.ImageField()
    # 用户评分
    rating = models.FloatField(null=True)




