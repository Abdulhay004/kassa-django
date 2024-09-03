from django.db import models
from users.models import User
# Create your models here.

class Qarz(models.Model):
    summa = models.PositiveIntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    sana = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.author.username
    
    class Meta:
        db_table = 'qarz'
