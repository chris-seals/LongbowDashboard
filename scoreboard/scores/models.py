from django.db import models

# Create your models here.
class Score(models.Model):
    score_date = models.DateField(auto_now=True)
    name = models.CharField(max_length=40)
    score = models.IntegerField()

    def __str__(self):
        return self.name

    def date_pretty(self):
        return self.score_date.strftime('%m/%d/%Y')