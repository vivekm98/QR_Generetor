from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
import qrcode
import os
from django.conf import settings
def home(request):
    if request.method=='POST':
        form=QRcodeForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            url=form.cleaned_data['url']

            qr=qrcode.make(url)
            file_name=name.replace(" ","_").lower()+'_menu.png'
            file_path=os.path.join(settings.MEDIA_ROOT,file_name)
            qr.save(file_path)

            #img---
            qr_url=os.path.join(settings.MEDIA_URL,file_name)
            context={
                'name':name,
                'qr_url':qr_url,
            }
            return render(request,'qr.html',context)

    else:
       form=QRcodeForm()
       context={
         'form':form
        }
       return render(request,'home.html',context)