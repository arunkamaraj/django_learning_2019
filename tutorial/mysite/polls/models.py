from django.db import models
from django.utils import timezone
from datetime import timedelta


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=250)
    publication_date = models.DateTimeField()

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.publication_date > timezone.now() - timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=250)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Publication(models.Model):
    title = models.CharField(max_length=250)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Article(models.Model):
    heading = models.CharField(max_length=250)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['heading']

    def __str__(self):
        return self.heading


class CommmonInfo(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ['age']


class Student(CommmonInfo):
    home = models.CharField(max_length=250)

    class Meta(CommmonInfo.Meta):
        db_table = 'students_info'

    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline

class ArunBookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(author="Arun")


class kiruthikaQuerySet(models.QuerySet):
    def kiruthika(self):
        return self.filter(author='Kiruthika')

# manager with query set
class TanviQuerySet(models.QuerySet):
    def tanvi(self):
        return self.filter(author='tanvi')

class TanviBookManager(models.Manager):
    def get_queryset(self):
        return TanviQuerySet(model=self.model, using=self._db)

    def tanvi(self):
        return self.get_queryset().tanvi()


class book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    pdf = models.FileField(upload_to="book/pdf")
    cover = models.ImageField(upload_to="cover/img", null=True, blank=True)
    objects = models.Manager() # order should be important  to handle the default manager
    arun = ArunBookManager() # custom manager
    tanvi = TanviBookManager() # custom manager with queryset
    kiruthika = kiruthikaQuerySet.as_manager() # quesryset as manager


    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.pdf.delete()
        self.cover.delete()
        super().delete()



