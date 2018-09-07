from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=20)

class Email(models.Model):
    email_address = models.CharField(max_length=30)

class ServerList(models.Model):
    asset_status = (
        (0, '在线'),
        (1, '下线'),
        (2, '未知'),
        (3, '故障'),
        (4, '备用'),
    )
    operation = (
        (0, '管理'),
        (1, '远程链接'),
        (2, '续费'),
        (3, '升级'),
        (4, '更多'),
    )
    name = models.CharField(max_length=20,verbose_name='设备名称')
    ip = models.CharField(max_length=20,verbose_name='ip地址')
    status = models.SmallIntegerField(choices=asset_status, default=0, verbose_name='设备状态')
    config = models.CharField(max_length=50,verbose_name='配置')
    opera = models.SmallIntegerField(choices=operation, default=0, verbose_name='操作')