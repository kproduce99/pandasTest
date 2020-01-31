from django.db import models

# Create your models here.
class Goods(models.Model):
    GoodsID = models.CharField(max_length=100)
    GoodsIDSeqNo = models.IntegerField()
    GoodsPrice = models.IntegerField()


class Tx(models.Model):
    TrasactionID = models.CharField(max_length=100)
    GoodsID = models.CharField(max_length=100)
    GoodsIDSeqNo = models.IntegerField()
    Quantity = models.IntegerField()



class Sumifs(models.Model):
    GoodsID = models.CharField(max_length=100)
    GoodsIDSeqNo = models.IntegerField()
    Quantity = models.IntegerField()
    GoodsPrice = models.IntegerField()

