from django.db import models
from django.contrib.auth.models import User

from word.models import Word


# Create your models here.
class Learner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)

    stage_learning_word = models.CharField(choices=[
        ('Unknown', 'Unknown'),
        ('Learning_0_stage', 'Learning_0_stage'),
        ('Learning_1_stage', 'Learning_1_stage'),
        ('Learning_2_stage', 'Learning_2_stage'),
        ('Learning_3_stage', 'Learning_3_stage'),
        ('Learning_4_stage', 'Learning_4_stage'),
        ('Learning_5_stage', 'Learning_5_stage'),
        ('Learned', 'Learned'),
    ], default='Unknown')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
