from django.db import models


class Original(models.Model):
    hard_text = models.TextField()
    
    def __str__(self):
        return self.hard_text

class Simple(models.Model):
    hard = models.ForeignKey(Original, on_delete=models.CASCADE)
    simple_text = models.TextField()

def __str__(self):
    return self.simple_text

class History(models.Model):
    hard = models.ForeignKey(Original, on_delete=models.CASCADE)
    simple = models.ForeignKey(Simple, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

        
