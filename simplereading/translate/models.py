from django.db import models

class Simple(models.Model):
    simple_text = models.TextField()
    def __str__(self):
        return self.simple_text

class Original(models.Model):
    hard_text = models.TextField()
    def __str__(self):
        return self.hard_text

class translation(models.Model):
    hard = models.ForeignKey(Original, on_delete=models.CASCADE)
    simple = models.ForeignKey(Simple, on_delete=models.CASCADE)
    


