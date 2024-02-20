from django.contrib.auth.models import Permission, User
from django.db import models


class Websitelogo(models.Model):
    label = models.CharField(max_length=250)
    website_logo = models.ImageField(default='', upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.label


class Department(models.Model):
    # user = models.ForeignKey(User, default=1,on_delete=models.CASCADE)
    goal = models.CharField(max_length=250)
    department_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=10000)
    department_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.department_title + ' - ' + self.goal


class Activity(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    activity_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.activity_title


class News(models.Model):
    news_title = models.CharField(max_length=500)
    news_content = models.TextField(max_length=10000)
    news_date = models.DateField()
    new_author = models.CharField(max_length=100)
    news_mainphoto = models.ImageField(default='', upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.news_title


class Schools(models.Model):
    school_name = models.CharField(max_length=500)
    school_description = models.TextField(max_length=10000)
    school_mainphoto = models.ImageField(default='', upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.school_name

class Excellentscholar(models.Model):
    scholar_name = models.CharField(max_length=500)
    scholar_job = models.CharField(max_length=500, blank=True)
    scholar_facebook = models.CharField(max_length=500,blank=True)
    scholar_wechat = models.CharField(max_length=500, blank=True)
    scholar_linkedin = models.CharField(max_length=500, blank=True)
    scholar_description = models.TextField(max_length=500, blank=True)
    scholar_photo = models.ImageField(default='', upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.scholar_name


class Programstype(models.Model):
    programs_type_name = models.CharField(max_length=500)
    programs_type_description = models.TextField(max_length=10000)

    def __str__(self):
        return self.programs_type_name


class Programs(models.Model):
    schools = models.ForeignKey(Schools, on_delete=models.CASCADE)
    programs_type = models.ForeignKey(Programstype, on_delete=models.CASCADE)
    program_name = models.CharField(max_length=500)
    program_description = models.TextField(max_length=10000)
    program_intake = models.CharField(max_length=50)
    program_duration = models.IntegerField()
    program_tuition = models.IntegerField()
    program_language = models.CharField(max_length=50)
    program_mainphoto = models.ImageField(default='', upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.program_name

class Note(models.Model):
    note_title = models.CharField(max_length=500)
    note_content = models.TextField(max_length=10000)
    note_date = models.DateField()
    note_author = models.CharField(max_length=100)

    def __str__(self):
        return self.note_title

class Aboutus(models.Model):
    article_title = models.CharField(max_length=500)
    article_content = models.TextField(max_length=10000)
    article_date = models.DateField()
    articles_author = models.CharField(max_length=100)

    def __str__(self):
        return self.article_title


class Newsimages(models.Model):
    news = models.ForeignKey(News,on_delete=models.CASCADE)
    news_image = models.ImageField(default='', upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.news.news_title + " news_image"
