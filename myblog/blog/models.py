from django.db import models


class Publication(models.Model):
    """Publication data"""

    title = models.CharField('header', max_length=100)
    description = models.TextField('text')
    author = models.CharField('author', max_length=100)
    date = models.DateField('date')
    image = models.ImageField('image', upload_to='image/%Y')

    def __str__(self):
        return f"{self.title}, {self.author}"

    class Meta:
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'


class Comment(models.Model):
    """Comments"""

    email = models.EmailField()
    name = models.CharField('Name', max_length=50)
    text = models.TextField('Text', max_length=2000)
    publication = models.ForeignKey(Publication, verbose_name='Publication', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Like(models.Model):
    """Likes"""

    ip_address = models.CharField('IP-address', max_length=20)
    publication = models.ForeignKey(Publication, verbose_name='Publication', on_delete=models.CASCADE)
