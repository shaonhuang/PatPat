from django.db import models
from games.models import Gameinfo
from django.contrib.auth.models import User

# Create your models here.
class comments(models.Model):
    # id
    comment_id = models.AutoField(primary_key=True)

    # 游戏id
    game_id = models.ForeignKey(Gameinfo,on_delete=models.PROTECT)

    # 用户id
    user_id = models.ForeignKey(User,on_delete=models.PROTECT)

    # 评论内容
    comment_content = models.CharField(max_length=500,blank=False)

    # 评论时间
    comment_date = models.DateTimeField()

    # 用户评分
    rating = models.FloatField(null=True)
