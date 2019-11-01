from django.db import models

class ICC(models.Model):
    team_name = models.CharField(max_length=200)
    matches = models.IntegerField()
    matches_won = models.IntegerField()
    matches_lost = models.IntegerField()
    net_r_r = models.CharField(max_length=200)
    points = models.IntegerField()

    def __str__(self):
        return self.team_name

    class Meta:
        db_table = "ICC"
# Create your models here.

