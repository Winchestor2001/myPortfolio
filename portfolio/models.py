from django.db import models


class Portfolio(models.Model):
    CHOICES = (
        ('Web Site', 'Web'),
        ('Telegram Bot', 'TgBot'),
        ('Other', 'Other')
    )
    CHOICES_2 = (
        ('Web', 'Web'),
        ('TgBot', 'TgBot'),
        ('Other', 'Other')
    )

    category = models.CharField(max_length=100, choices=CHOICES)
    category_2 = models.CharField(max_length=100, choices=CHOICES_2, null=True)
    title = models.CharField(max_length=50, null=True)
    client = models.CharField(max_length=50)
    image_1 = models.ImageField(upload_to='articles/', null=True)
    image_2 = models.ImageField(upload_to='articles/', null=True)
    project_date = models.DateTimeField(auto_now_add=True)
    project_url = models.CharField(max_length=100)
    about_project = models.TextField()


class MyInfoConfig(models.Model):
    myPic = models.ImageField(upload_to='articles/')
    myCv = models.FileField(upload_to='docs/', null=True)
    myName = models.CharField(max_length=80)
    mySurname = models.CharField(max_length=80)
    my_location = models.CharField(max_length=200)

    html_status = models.IntegerField(default=50)
    css_status = models.IntegerField(default=50)
    js_status = models.IntegerField(default=50)
    python_status = models.IntegerField(default=50)
    django_status = models.IntegerField(default=50)
    react_status = models.IntegerField(default=50)
    tgbot_status = models.IntegerField(default=50)
    bootstrap_status = models.IntegerField(default=50)
    sql_status = models.IntegerField(default=50)

    birthday = models.CharField(max_length=100)
    myPhone_number = models.CharField(max_length=50)
    now_city = models.CharField(max_length=100)
    my_age = models.CharField(max_length=20)
    my_email = models.CharField(max_length=100)
    freelance_status = models.CharField(max_length=50)
    about_text = models.TextField()
