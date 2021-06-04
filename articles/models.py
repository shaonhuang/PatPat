from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class article(models.Model):
    # id
    article_id = models.AutoField(primary_key=True)

    article_title=models.CharField(max_length=100,blank=False,default="文章标题")

    article_subtitle=models.CharField(max_length=100,blank=False,default="文章简介")

    # 评论时间
    comment_date = models.DateTimeField()

    picurl=models.CharField(max_length=300,blank=False,default="url")

    # 用户评分
    rating = models.FloatField(null=True)

    #点赞数
    zan = models.IntegerField(default=0)

    cai = models.IntegerField(default=0)

    collection = models.IntegerField(default=0)


class collectiona(models.Model):

        # id
    collection_id = models.AutoField(primary_key=True)

        # 游戏id
    article = models.ForeignKey(article, on_delete=models.PROTECT)

        # 用户id
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
