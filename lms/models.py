from django.db import models

# Create your models here.

class Books(models.Model):
    book_name=models.CharField(max_length=300)
    author_name=models.CharField(max_length=150)
    publishedon=models.DateField(auto_now_add=True)
    isbn = models.CharField(max_length=13)
    pages = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        ordering=['-publishedon']
        verbose_name_plural='Books'
    

    def __str__(self):
        return '{}        {}'.format(self.book_name, self.publishedon)

