from django.db import models
from django.utils import timezone

# Create your models here.

class mainImage(models.Model):
    select = (
	    ("w3-tiny", "tiny"),
        ("w3-small", "small"),
        ("w3-medium", "medium"),
        ("w3-large", "large"),

        ("w3-xlarge", "xlarge"),
        ("w3-xxlarge", "xxlarge"),
        ("w3-xxxlarge", "xxxlarge"),
        ("w3-jumbo", "jumbo"),
        )


    title = models.CharField(max_length=200 , help_text = "USE title1 for the first background image , then title2 for the second background image and title3 for the last background image")

    textTitle = models.CharField(max_length=200 , blank=True, null=True , help_text = "Text title")
    textTitleSize = models.CharField(max_length=20 , blank=True, null=True , choices=select)

    text = models.TextField(help_text ="One sentence to describe the image")
    textSize = models.CharField(max_length=20 , blank=True, null=True , choices=select)

    image = models.ImageField(upload_to='static/image/comingSoon/' , help_text ="background image")
    created_date = models.DateTimeField(default=timezone.now , help_text = "When this background has been created")

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class background(models.Model):
    title = models.CharField(max_length=200 , help_text ="Title for set of menu and footer pattern")

    menuImage = models.ImageField(upload_to='static/image/comingSoon/' , help_text ="menu image")
    footerImage = models.ImageField(upload_to='static/image/comingSoon/' , help_text ="footer image")
    image = models.ImageField(upload_to='static/image/comingSoon/' , help_text ="Image in the footer")

    created_date = models.DateTimeField(default=timezone.now , help_text = "When this date has been created")

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class comingDate(models.Model):
    title = models.CharField(max_length=200 , help_text ="Use ThatDate title to show on the page")
    date = models.DateTimeField(default=timezone.now , help_text ="Set the D date")
    created_date = models.DateTimeField(default=timezone.now , help_text = "When this date has been created")

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class eMail(models.Model):

   # select = (
   # =>what is read by python , what user sees
   # ( , )
   #  )
    select = (
	    ("Let me know when the site ready", "Let me know when the site ready"),
        ("I am curious about your services", "I am curious about your services"),
        ("I need to get in shape", "I need to get in shape"),
        ("How much do charge ?", "How much do charge ?"),

        ("What services are you offering?", "What services are you offering?"),
        ("Any other concern ?", "Any other concern ?"),
        ("I am just passing by", "I am just passing by"),
        ("I am fine do not need anything", "I am fine do not need anything"),
        )

    name = models.CharField(max_length=200 , help_text ="This is provided by the website visitors")
    email = models.CharField(max_length=500 , help_text ="This is provided by the website visitors")

    message = models.CharField(max_length=400 ,default="Let me know when the site ready" , choices=select , blank = True , help_text ="This is provided by the website visitors")

    created_date = models.DateTimeField(default=timezone.now , help_text ="This is provided by the website visitors")

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
