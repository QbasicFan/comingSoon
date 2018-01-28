from django.shortcuts import render
from comingSoon.forms import eMailForm

from .models import mainImage , comingDate , eMail , background
# Create your views here.

def index(request):
   title = mainImage.objects.all()
   cDate = comingDate.objects.all()
   email = eMail.objects.all()
   bkg = background.objects.all()




   image1 = title.filter(title="title1")
   image2 = title.filter(title="title2")
   image3 = title.filter(title="title3")



   if request.method == 'POST':
        form = eMailForm(request.POST)
        if form.is_valid():
            form.save()
            joe = "thanks you for sharing your informations with us, you will be notified when 888vital will be ready"
            context = {'jack':joe,"image1":image1,"image2":image2,"image3":image3,"cDate":cDate,"email":email , "bkg":bkg}
            return render(request, 'vital/index.html', context )
        else:
            return render(request, 'vital/error.html', {})
   else:
        form = eMailForm()
        context = {'form':form,"image1":image1,"image2":image2,"image3":image3,"cDate":cDate,"email":email , "bkg":bkg}
   return render(request, 'vital/index.html', context )
