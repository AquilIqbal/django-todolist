from django.db import models

class task(models.Model):
        title = models.CharField(max_length=200)

        def __dir__(self):
                return self.title
