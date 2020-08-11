from django.shortcuts import render
from home.models import Setting

# Create your views here.

from home.models import ContactFormu, ContactFormMessage



def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting':setting, 'page':'home'}
    return render(request, 'index.html',context)





def hakkımızda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting':setting}
    return render(request, 'hakkımızda.html',context)





def referanslar(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting':setting}
    return render(request, 'referanslarımız.html',context)



def iletisim(request):

    if request.method == 'POST' : # form post edildiyse
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormu() # model ile bağlantı kur
            data.name = form.cleaned_data['name'] # formdan bilgiyi al
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.save() # Veritabanına kaydet
            messages.success(request, "mesajınız başarılı bir şekilde gönderilmiştir ")
            return HttpResponseRedirect ('/iletisim')

    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    context = {'setting':setting, 'form':form}
    return render(request, 'iletisim.html',context)