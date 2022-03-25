from django.shortcuts import render,get_object_or_404
from .models import Services,Service_details,Person,Request,test,Advertising
from django.core.mail import send_mail
from  django.conf import settings
from  django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def index(request):
    #title= request.user
    title='جمعية البر والخدمات الاجتماعية '
    id2 = Service_details.objects.filter(name='كفالة طالب علم', status=True).get()
    c= 1333+ Request.objects.filter(idd=id2).count(),
    context={

        'ad': Advertising.objects.all(),
        'count': c,
        "template":title, }
   # return HttpResponse('<H1 align="center">جمعية البر والخدمات الاجتماعية</h1>')
    return render(request,'index.html',context)


def about(request):
    return  render(request,'about.html',)
def projects(request):
    return  render(request,'projects.html')
def i(request):
    return render(request,'test.html')

def success(request):
    return render(request,'part/success.html')
def services (request):


    services = Services.objects.all()
    s = Service_details.objects.all()
    context = {
        'services': services,
        's' : s, }
    return  render(request,'services.html', context)


def services_details(request,services_id):
   # services =Service_details.objects.get(pk=services_id)
   services=get_object_or_404(Services,pk=services_id)
   ss = Service_details.objects.all()
   context ={
      'services': services,
      'ss':  ss}
   return  render(request,'services_details.html', context)

def testt(request):

     if request.method=="POST":
         namee = request.POST.get("names")
         file=request.FILES.get("file")
         test(name=namee,file=file).save()
     return  render(request,'test.html')
def contact1 (request,):

    if request.method == 'POST' and 'btnsign' in request.POST:
        subject = request.POST["subject"]

        email= request.POST.get("email")

        message = request.POST.get("message")
        send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER],
            #settings.ADMIN_EMAILS

            )
    return render(request, 'contact/contact1.html')
def contact (request,):
    x=None


    if request.method == 'POST' and 'btnsign' in request.POST:
        p=Person.objects.filter(isseen=True , accepted=True)
        if p.exists():
            for e in p :

                 subject=request.POST["subject"]
            # email=request.POST["email"]
                 email= e.email
                 message=request.POST["message"]
                 send_mail(
                 subject,
                   message,
                   settings.EMAIL_HOST_USER,
                     [email],

          #  fail_silently=False,
                               )
                 e.accepted=False
                 e.save()
                 messages.success(request, 'تم ارسال الرسابة ')
                 return render(request, 'part/success.html')






    return render(request,'contact/contact.html',{'x':x})



#---------------------------------

# -------------------------
def neworphan(request):
    context ={
    }

    return render(request,'pages/neworphan.html',context)
#-------------------------
def newfamily(request):
    context={}
    return render(request,'pages/newfamily.html',context)

#-------------------------
def newmedicine(request):
    context={}
    return render(request,'pages/newmedicine.html',context)


from .models import Person
from .forms import NewPersonForm
def newperson(request,services_id):
   # ser = get_object_or_404(Service_details, pk=services_id)
    form= NewPersonForm()

    return render(request,'newperson.html',{'form':form})

