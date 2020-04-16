from django.db import models

class List(models.Model):
    item_main = models.CharField(max_length = 200)
    completed = models.BooleanField(default = False)

    def __str__(self):
        return self.item_main + ' | ' + str(self.completed)

