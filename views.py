from django.shortcuts import render

from comingSoon.forms import eMailForm

from .models import comingDate , eMail , frontErrorPage , SBtn , backgroundImage

# Create your views here.

def index(request):
   cDate = comingDate.objects.all()
   email = eMail.objects.all()
   bkg = frontErrorPage.objects.all()
   SB = SBtn.objects.all()
   bkgImg = backgroundImage.objects.all()


   if request.method == 'POST':
        form = eMailForm(request.POST)
        if form.is_valid():
            form.save()
            joe = "Thank you for contacting us, you will be notified when  888vital is ready!!!!"
            context = {'jack':joe,"cDate":cDate,"email":email , "bkg":bkg , "SBtn":SB , "bkgImg":bkgImg}
            return render(request, 'comingSoon/index.html', context )
        else:
            return render(request, 'comingSoon/error.html', {})
   else:
        form = eMailForm()
        context = {'form':form,"cDate":cDate,"email":email , "bkg":bkg , "SBtn":SB , "bkgImg":bkgImg}
   return render(request, 'comingSoon/index.html', context )


##############################################

def handler404(request):
    bkg = frontErrorPage.objects.all()

    return render(request,'comingSoon/error.html', {"bkg":bkg})

