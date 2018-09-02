from django.db import models
from django.utils import timezone
from .atrList import textColor , bgColor , textSize , textFont
# Create your models here.



class SBtn(models.Model):

    title = models.CharField(max_length=200 , blank=True, null=True , help_text ="Use ThatDate title to show on the page")



    facebook = models.BooleanField(default=False , help_text ="Check to display on page")
    fbLink = models.CharField(max_length=500 , blank=True, null=True , help_text ="Enter link")

    instagram = models.BooleanField(default=False , help_text ="Check to display on page")
    instagramLink = models.CharField(max_length=500 , blank=True, null=True , help_text ="Enter link")

    snapchat = models.BooleanField(default=False , help_text ="Check to display on page")
    snapchatLink = models.CharField(max_length=500 , blank=True, null=True , help_text ="Enter link")

    pinterest = models.BooleanField(default=False , help_text ="Check to display on page")
    pinterestLink = models.CharField(max_length=500 , blank=True, null=True , help_text ="Enter link")

    twitter = models.BooleanField(default=False , help_text ="Check to display on page")
    twitterLink = models.CharField(max_length=500 , blank=True, null=True , help_text ="Enter link")

    linkedin = models.BooleanField(default=False , help_text ="Check to display on page")
    linkedinLink = models.CharField(max_length=500 , blank=True, null=True , help_text ="Enter link")

    delicious = models.BooleanField(default=False , help_text ="Check to display on page")
    deliciousLink = models.CharField(max_length=500 , blank=True, null=True , help_text ="Enter link")

    google = models.BooleanField(default=False , help_text ="Check to display on page")
    googleLink = models.CharField(max_length=500 , blank=True, null=True , help_text ="Enter link")

    qq = models.BooleanField(default=False , help_text ="Check to display on page")
    qqLink = models.CharField(max_length=500 , blank=True, null=True , help_text ="Enter link")

    soundcloud = models.BooleanField(default=False , help_text ="Check to display on page")
    soundcloudLink = models.CharField(max_length=500 , blank=True, null=True , help_text ="Enter link")

    steam = models.BooleanField(default=False , help_text ="Check to display on page")
    steamLink = models.CharField(max_length=500 , blank=True, null=True , help_text ="Enter link")

    youtube = models.BooleanField(default=False , help_text ="Check to display on page")
    youtubeLink = models.CharField(max_length=500 , blank=True, null=True , help_text ="Enter link")

    fcc = models.BooleanField(default=False , help_text ="Check to display on page")
    fccLink = models.CharField(max_length=500 , blank=True, null=True , help_text ="Enter link")

    quora = models.BooleanField(default=False , help_text ="Check to display on page")
    quoraLink = models.CharField(max_length=500 , blank=True, null=True , help_text ="Enter link")

    reddit = models.BooleanField(default=False , help_text ="Check to display on page")
    redditLink = models.CharField(max_length=500 , blank=True, null=True , help_text ="Enter link")

    vine = models.BooleanField(default=False , help_text ="Check to display on page")
    vineLink = models.CharField(max_length=500 , blank=True, null=True , help_text ="Enter link")

    amazon = models.BooleanField(default=False , help_text ="Check to display on page")
    amazonLink = models.CharField(max_length=500 , blank=True, null=True , help_text ="Enter link")

    codepen = models.BooleanField(default=False , help_text ="Check to display on page")
    codepenLink = models.CharField(max_length=500 , blank=True, null=True , help_text ="Enter link")

    etsy = models.BooleanField(default=False , help_text ="Check to display on page")
    etsyLink = models.CharField(max_length=500 , blank=True, null=True , help_text ="Enter link")

    skype = models.BooleanField(default=False , help_text ="Check to display on page")
    skypeLink = models.CharField(max_length=500 , blank=True, null=True , help_text ="Enter link")

    whatsapp = models.BooleanField(default=False , help_text ="Check to display on page")
    whatsappLink = models.CharField(max_length=500 , blank=True, null=True , help_text ="Enter link")

    vimeo = models.BooleanField(default=False , help_text ="Check to display on page")
    vimeoLink = models.CharField(max_length=500 , blank=True, null=True , help_text ="Enter link")

    stack = models.BooleanField(default=False , help_text ="Check to display on page")
    stackLink = models.CharField(max_length=500 , blank=True, null=True , help_text ="Enter link")

    jsfiddle = models.BooleanField(default=False , help_text ="Check to display on page")
    jsfiddleLink = models.CharField(max_length=500 , blank=True, null=True , help_text ="Enter link")




    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title











class frontErrorPage(models.Model):
    title = models.CharField(max_length=200 , help_text ="Title for set of menu and footer pattern")

    frontImage = models.ImageField(upload_to='static/image/comingSoon/' , help_text ="front page background image")
    frontText  = models.CharField(max_length=200 , blank=True, null=True , help_text = "Front Text ")

    frontTextColor = models.CharField(max_length=20 , blank=True, null=True , choices=textColor , help_text = "Choose front text color")
    frontTextBgColor = models.CharField(max_length=20 , blank=True, null=True , choices=bgColor , help_text = "Choose front background text color")
    textTitleSize = models.CharField(max_length=20 , blank=True, null=True , choices=textSize , help_text = "Choose front text size")
    textTitleFont = models.CharField(max_length=20 , blank=True, null=True , choices=textFont , help_text = "Choose front text font")

    aboutText  = models.TextField( blank=True, null=True , help_text = "About Text ")

    aboutTextColor = models.CharField(max_length=20 , blank=True, null=True , choices=textColor , help_text = "Choose front text color")
    aboutTextBgColor = models.CharField(max_length=20 , blank=True, null=True , choices=bgColor , help_text = "Choose front background text color")
    aboutitleSize = models.CharField(max_length=20 , blank=True, null=True , choices=textSize , help_text = "Choose front text size")
    aboutitleFont = models.CharField(max_length=20 , blank=True, null=True , choices=textFont , help_text = "Choose front text font")

    errorImage = models.ImageField(upload_to='static/image/comingSoon/' , help_text ="404 page background image")
    errorText  = models.CharField(max_length=200 , blank=True, null=True , help_text = "Error Text")

    errorTextColor = models.CharField(max_length=20 , blank=True, null=True , choices=textColor , help_text = "Choose front text color")
    errorTextBgColor = models.CharField(max_length=20 , blank=True, null=True , choices=bgColor , help_text = "Choose front background text color")
    errorTitleSize = models.CharField(max_length=20 , blank=True, null=True , choices=textSize , help_text = "Choose front text size")
    errorTitleFont = models.CharField(max_length=20 , blank=True, null=True , choices=textFont , help_text = "Choose front text font")



    created_date = models.DateTimeField(default=timezone.now , help_text = "When this date has been created")

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class backgroundImage(models.Model):
    title = models.CharField(max_length=200 , help_text ="---")
    image = models.ImageField(upload_to='static/image/comingSoon/' , help_text ="---")

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
	    ("I want to lose weight", "I want to lose weight"),
        ("Health coaching", "Health coaching"),
        ("I am curious about your services", "I am curious about your services"),
        ("let me know when the site is ready", "let me know when the site is ready"),
        )

    name = models.CharField(max_length=200 , help_text ="This is provided by the website visitors")
    email = models.CharField(max_length=500 , help_text ="This is provided by the website visitors")

    message = models.CharField(max_length=400 ,default="I want to lose weight" , choices=select , blank = True , help_text ="This is provided by the website visitors")

    created_date = models.DateTimeField(default=timezone.now , help_text ="This is provided by the website visitors")

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
