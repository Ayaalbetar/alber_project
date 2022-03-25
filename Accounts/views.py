from django.shortcuts import render,redirect
from  django.contrib import messages
from Services.models import Person,Request,Service_details
import  re


########################################################

import  os
from django.http import HttpResponse
import mimetypes

def download_image(request, image_id):
    img = Person.objects.get(id=image_id)
    wrapper      = open(img.file)  # img.file returns full path to the image
    content_type = mimetypes.guess_type("photo")[0]  # Use mimetypes to get file type
    response     = HttpResponse(wrapper,content_type=content_type)
    response['Content-Length']      = os.path.getsize(img.file)
    response['Content-Disposition'] = "attachment; filename=%s" %  img.name
    return response
#########################################################

# Create your views here.
def newstudent(request,):
   if request.method =='POST' and 'btnsign' in  request.POST:

       # variabls for  fields
       email=None
       fname=None
       lname =None
       place_birth=None
       birthday = None
       gender=None
       pname=None
       mname=None
       motherln=  None
       nationality=None
       id_namber=None
       phone =None
       address=None
       fatherdie =None
       photo1=None
       is_added=None # من اجل ان نختر هل تم الاضافة



       # Get  values from the form
       if 'fname' in request.POST:
           fname = request.POST['fname']
       else:
           messages.error(request, 'error in fname')


       if 'bornplace' in request.POST:
           place_birth = request.POST['bornplace']
       else:
           messages.error(request, 'error in bornplace')

       if 'lname' in request.POST:
           lname = request.POST['lname']
       else:
           messages.error(request, 'error in lname')


       if 'birthday' in request.POST:
         birthday=  request.POST['birthday']


       else:
           messages.error(request, 'خطأ في المواليد')


       if 'pname' in request.POST:
           pname = request.POST['pname']
       else:
           messages.error(request, 'هخطأ فياسم الاب')


       if 'motherln' in request.POST:
           motherln = request.POST['motherln']
       else:
           messages.error(request, 'خطأ في عدم ادخال نسبة الأم')

       if 'id_namber' in request.POST:
           id_namber = request.POST['id_namber']
          # id_namber= str(id_namber)
           if  str(id_namber).__len__()!=10:
               messages.success(request," الرقم الوطني غير صالح")
               return render(request, 'pages/newstudent.html')
              # id_namber=int(id_namber)
       else:
           messages.error(request, 'خطأ في عدم ادخال الرقم الوطني')

       if 'nationality' in request.POST:
           nationality = request.POST['nationality']
       else:
           messages.error(request, 'خطأ في عدم ادخال الجنسية ')
       if 'email' in request.POST:
               email = request.POST['email']
       else:
               messages.error(request, 'error in email')

       if 'phone' in request.POST:
           phone = request.POST['phone']
       else:
           messages.error(request, 'error in phone')

       if 'address' in request.POST:
           address = request.POST['address']
       else:
           messages.error(request, 'error in address')

       if 'mname' in request.POST: mname = request.POST['mname']
       else: messages.error(request, 'اسم الام')

      # if  'f1' in request.POST and 'f2' in request.POST :

       #ممكن هيك هذه صحيحة
     #  photo1 = [request.POST['f1'], request.POST['f2']]
     # رح جرب
     #     photo1=request.FILES.getlist('f1')
      # else:messages.error(request,'phooooooootos')

       if 'father_die'in request.POST:fatherdie=request.POST['father_die']
       #gender=request.POST['Radios1']

       if 'Radios1' in request.POST:gender=request.POST['Radios1']
       #elif 'Radios2' in request.POST: gender=request.POST['Radios2']

# check the value:
       if  fname and lname and mname and pname and email and place_birth and gender and phone and address and nationality and id_namber and motherln :
           if fatherdie =='on':
               f=True
           else: f=False

# chek if id_naber is uniqc and user is token
           if Person.objects.filter(id_namber=id_namber).exists():
                messages.error(request,'لقد سجلت مسبقا!!! ')
           else:
               #add student profile
               def user_directory_path(instance, filename):
                   # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
                   return 'user_{0}/{1}'.format(instance.id_namber, filename)


               student=Person(fname=fname,lname=lname,pname=pname,mname=mname,address=address,motherln=motherln,phone=phone,nationality=nationality,
                          id_namber=id_namber,place_birth=place_birth,gender=gender,email=email,birthday=birthday,father_die=f)
               photo1 = request.FILES.get("f1")
              # photo=user_directory_path(Person.objects.get(id_namber=id_namber),"user"))
                            #father_die=fatherdie
                         #)
               #Person.birthday.auto_created=request.POST['birthday']
               #pp=request.POST['f1']
              # photo1=user_directory_path(student,pp)
             #  from  ALber import settings
               #photo1 = os.path.join(settings.MEDIA_ROOT, user_directory_path(student, request.POST['f1']))
               student.photo=photo1
               student.save()
               photo1 = request.FILES.get("f2")
               student.photo = photo1
               student.save()

               photo1 = request.FILES.get("f3")
               student.photo = photo1
               student.save()
               photo1 = request.FILES.get("f4")
               student.photo = photo1
               student.save()
               photo1 = request.FILES.get("f5")
               student.photo = photo1
               student.save()
               photo1 = request.FILES.get("f6")
               student.photo = photo1
               student.save()
               photo1 = request.FILES.get("f7")
               student.photo = photo1
               student.save()
               photo1 = request.FILES.get("f8")
               student.photo = photo1
               student.save()
               photo1
               photo1
               photo1
               is_added=True


               id1=Person.objects.get(fname=fname,lname=lname,pname=pname,mname=mname,address=address,motherln=motherln,phone=phone,nationality=nationality,
                          id_namber=id_namber,place_birth=place_birth,gender=gender,birthday=birthday)
               fname = '',
               lname = '' ,
               pname = ' ',
               mname =  ' ',
               address = ' ',
               motherln = ' ',
               phone = ' ',
               nationality = ' ',
               id_namber = ' ',
               place_birth = ' ',
               gender = ' ',
               birthday = ' ',
               fatherdie = ' '
               id2=Service_details.objects.get( name='كفالة طالب علم',status=True)
               req=Request( idperson=id1,idd=id2,request_place=None ,status=1)
               req.save()
               # sucsses messages
               messages.success(request,'تم تسجيل طلبك ستصلك رسالة في حال تم قبولك ')

       else:
           messages.error(request,'هناك حقول فارغة ')
       context ={
              'fname':fname,
             'lname':lname,
             'pname':pname,
             'mname':mname,
             'address':address,
             'motherln':motherln,
             'phone':phone,
             'nationality':nationality,
             'id_namber':id_namber,
             'place_pirth':place_birth,
             'gender':gender,
             'birthday':birthday,
             'father_die':fatherdie,
              'is_added':is_added
       }

       #return render(request, 'pages/newstudent.html', context)
       return render(request,'part/success.html',context)
   else:
   # messages.info(request, 'لقد تم تسجيل طلبك ')
     context={ }
   return render(request,'pages/newstudent.html',context)
# -------------------------
def neworphan(request):
  if request.method == 'POST' and 'btnsign' in request.POST:

     name=None
     lname=None
     fname=None
     pname=None
     count_child=None
     id_namber=None
     email=None
     nationality=None
     phone=None
     address=None
     is_added = None

     if 'name' in request.POST:
         name = request.POST['name']
     else:
         messages.error(request, 'error in name')

     if 'lname' in request.POST:
         lname = request.POST['lname']
     else:
         messages.error(request, 'error in  lname')

     if 'pname' in request.POST:
         pname = request.POST['pname']
     else:
         messages.error(request, 'error in  pname')

     if 'count_child' in request.POST:
         count_child = request.POST['count_child']
     else:
         messages.error(request, 'error in  count_child')

     if 'id_namber' in request.POST:
         id_namber = request.POST['id_namber']
     else:
         messages.error(request, 'error in  id_namber')
     if 'email' in request.POST:
         email = request.POST['email']
     else:
         messages.error(request, 'error in email')
     if 'phone' in request.POST:
         phone = request.POST['phone']
     else:
         messages.error(request, 'error in  phone')
     if 'nationality' in request.POST:
         nationality = request.POST['nationality']
     else:
         messages.error(request, 'error in الجنسية')
     if 'address' in request.POST:
         address = request.POST['address']
     else:
         messages.error(request, 'error in  address')
     if address and  phone and email and phone and id_namber and count_child and pname and  name and lname:
          if Person.objects.filter(id_namber=id_namber).exists():
               messages.error(request, 'لقد سجلت مسبقا!!! ')
          else:
               # add student profile
               def user_directory_path(instance, filename):
                   # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
                   return 'user_{0}/{1}'.format(instance.id_namber, filename)

               orphan = Person(fname=name, pname=pname, count_child=count_child, email=email,lname=lname,
                               id_namber=id_namber, address=address, phone=phone,nationality=nationality,birthday=None,
                           place_birth = None, gender = None     )

               photo1 = request.FILES.get("f1")
               orphan.photo = photo1
               orphan.save()
               photo1 = request.FILES.get("f2")
               orphan.photo = photo1
               orphan.save()
               photo1 = request.FILES.get("f3")
               orphan.photo = photo1
               orphan.save()
               photo1 = request.FILES.get("f4")
               orphan.photo = photo1
               orphan.save()
               photo1 = request.FILES.get("f5")
               orphan.photo = photo1
               orphan.save()
               photo1 = request.FILES.get("f6")
               orphan.photo = photo1
               orphan.save()
               photo1 = request.FILES.get("f7")
               orphan.photo = photo1
               orphan.save()
               photo1 = request.FILES.get("f8")
               orphan.photo = photo1
               orphan.save()
               is_added = True
          id1 = Person.objects.get(fname=name, lname=lname, pname=pname,  address=address,
                                    phone=phone, nationality=nationality,
                                   id_namber=id_namber)
          name = '',
          lname = '',
          pname = ' ',
          address = ' ',
          phone = ' ',
          nationality = ' ',
          id_namber = ' ',
          place_birth = ' ',
          gender = ' ',
          birthday = ' ',
          fatherdie = ' '
          id2 = Service_details.objects.get(name='كفالة أيتام', status=True)
          req = Request(idperson=id1, idd=id2, request_place=None, status=2)
          req.save()
          # sucsses messages
          messages.success(request, 'تم تسجيل طلبك ستصلك رسالة في حال تم قبولك ')

     else:
         messages.error(request, 'هناك حقول فارغة ')
     context = {
          'name':name,
          'lname':lname,
          'email':email,
         'address': address,
         'phone': phone,
         'id_namber': id_namber,
         'is_added': is_added
     }
     return render(request, 'part/success.html')
    # return render(request, 'pages/neworphan.html', context)
  else:


    return render(request,'pages/neworphan.html')
#-------------------------
from Services import  forms
def newfamily(request):
    form =  forms.NewPersonForm
    if request.method == "POST":
        form =forms.NewPersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    context={
        'form':form
    }
    if request.method == 'POST' and 'btnsign' in request.POST:
        hasbend=None
        fhasbend=None
        count_child=  None
        id_namber=None
        address=None
        phone=None
        is_added = None  # من اجل ان نختر هل تم الاضافة

        if 'hasbend' in request.POST:
            hasbend = request.POST['hasbend']
        else:
            messages.error(request, 'error in  hasbend')

        if 'fhasbend' in request.POST:
           fhasbend = request.POST['fhasbend']
        else:
           messages.error(request, 'error in  fhasbend')

        if 'address' in request.POST:
            address = request.POST['address']
        else:
            messages.error(request, 'error in  address')

        if 'id_namber' in request.POST:
            id_namber = request.POST['id_namber']
        else:
            messages.error(request, 'error in   id_namber')

        if 'count_child' in request.POST:
                count_child = request.POST['count_child']
        else:
                messages.error(request, 'error in count_child')
        if 'phone' in request.POST:
              phone = request.POST['phone']
        else:
            messages.error(request, 'error in count_child')
        if  hasbend and fhasbend and  count_child and id_namber and address and  phone:
            if Person.objects.filter(id_namber=id_namber).exists():
                messages.error(request, 'لقد سجلت مسبقا!!! ')
            else:
                # add student profile
                def user_directory_path(instance, filename):
                    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
                    return 'user_{0}/{1}'.format(instance.id_namber, filename)
                family =Person( email='',fname=hasbend,hasbend=hasbend,fhasbend=fhasbend,count_child=count_child,id_namber=id_namber,address=address,phone=phone)

                photo1 = request.FILES.get("f1")
                family.photo = photo1
                family.save()
                photo1 = request.FILES.get("f2")
                family.photo = photo1
                family.save()
                photo1 = request.FILES.get("f3")
                family.photo = photo1
                family.save()
                photo1 = request.FILES.get("f4")
                family.photo = photo1
                family.save()
                photo1 = request.FILES.get("f5")
                family.photo = photo1
                family.save()
                photo1 = request.FILES.get("f6")
                family.photo = photo1
                family.save()
                photo1 = request.FILES.get("f7")
                family.photo = photo1
                family.save()
                photo1 = request.FILES.get("f8")
                family.photo = photo1
                family.save()


                id1 = Person.objects.get( fname=hasbend,hasbend=hasbend, fhasbend=fhasbend, phone=phone,  address=address,
                                      id_namber =id_namber, count_child =count_child)


                id2 = Service_details.objects.get(name='عائلات مستورة', status=True)
                req = Request(idperson=id1, idd=id2, request_place=None, status=2)
                req.save()
                is_added = True
              # sucsses messages
                messages.success(request, 'تم تسجيل طلبك ستصلك رسالة ')

        else:
            messages.error(request, 'هناك حقول فارغة ')
        context = {
        'fname': hasbend,
        'address': address,
        'phone': phone,
        'id_namber': id_namber,
        'is_added': is_added
      }
        return render(request, 'part/success.html')
      #  return render(request,'pages/newfamily.html',context)
    else:
        # messages.info(request, 'لقد تم تسجيل طلبك ')
        context = {}
    return render(request, 'pages/newfamily.html', context)

#-------------------------
def newmedicine(request):
    if request.method == 'POST' and 'btnsign' in request.POST:
        fname=None
        lname =None
        id_namber=None
        phone=None
        gender=None
        email=None
        address=None
        place_birth=None
        nationality=None
        birthday=None
        is_added = None
        if 'fname' in request.POST:
            fname = request.POST['fname']
        else:
            messages.error(request, 'error in fname')
        if 'lname' in request.POST:
            lname = request.POST['lname']
        else:
            messages.error(request, 'error in fname')
        if 'id_namber' in request.POST:
            id_namber = request.POST['id_namber']
        else:
            messages.error(request, 'error in fname')
        if 'phone' in request.POST:
            phone = request.POST['phone']
        else:
            messages.error(request, 'error in  phoneع')
        if 'email' in request.POST:
            email = request.POST['email']
        else:
            messages.error(request, 'error in email')
        if 'address' in request.POST:
            address = request.POST['address']
        else:
            messages.error(request, 'error in address')
        if 'place_birth' in request.POST:
            place_birth = request.POST['place_birth']
        else:
            messages.error(request, 'error in place_birth')
        if 'birthday' in request.POST:
            birthday = request.POST['birthday']
        else:
            messages.error(request, 'error in birthday')
        if 'Radios1' in request.POST:
            gender = request.POST['Radios1']
        if   fname and lname and id_namber and email and phone and place_birth and birthday and address and gender:
              if Person.objects.filter(id_namber=id_namber).exists():
                      messages.error(request,'لقد سجلت مسبقا!!! ')
              else:
                  def user_directory_path(instance, filename):
                      # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
                      return 'user_{0}/{1}'.format(instance.id_namber, filename)
                  medicine=Person(fname=fname,lname=lname,birthday=birthday,place_birth=place_birth,
                                  phone=phone,gender=gender,address=address,email=email,id_namber=id_namber)
                  photo1=request.FILES.get('f1')
                  medicine.photo=photo1
                  medicine.save()
                  photo1 = request.FILES.get('f2')
                  medicine.photo = photo1
                  medicine.save()
                  photo1 = request.FILES.get('f3')
                  medicine.photo = photo1
                  medicine.save()
                  photo1 = request.FILES.get('f4')
                  medicine.photo = photo1
                  medicine.save()
                  photo1 = request.FILES.get('f5')
                  medicine.photo = photo1
                  medicine.save()
                  photo1 = request.FILES.get('f6')
                  medicine.photo = photo1
                  medicine.save()
                  photo1 = request.FILES.get('f7')
                  medicine.photo = photo1
                  medicine.save()
                  photo1 = request.FILES.get('f8')
                  medicine.photo = photo1
                  medicine.save()
                  photo1 = request.FILES.get('f9')
                  medicine.photo = photo1
                  medicine.save()
                  is_added = True

                  id1 = Person.objects.get(fname=fname, lname=lname, address=address,
                                           phone=phone,
                                           id_namber=id_namber, place_birth=place_birth, gender=gender,
                                           birthday=birthday)
                  id2 = Service_details.objects.get(name='دواء دائم', status=True)
                  req = Request(idperson=id1, idd=id2, request_place=None, status=4)
                  req.save()
                  # sucsses messages
                  messages.success(request, 'تم تسجيل طلبك ستصلك رسالة في حال تم قبولك ')


        else:
              messages.error(request, 'هناك حقول فارغة ')
        context = {
             'fname': fname,
             'lname': lname,
             'address': address,
             'phone': phone,
             'nationality': nationality,
             'id_namber': id_namber,
             'place_pirth': place_birth,
             'gender': gender,
             'birthday': birthday,
             'is_added': is_added
         }

       # return render(request, 'pages/newstudent.html', context)
        return render(request, 'part/success.html', context)
    else:
          # messages.info(request, 'لقد تم تسجيل طلبك ')
          context = {}


    return render(request,'pages/newmedicine.html',context)


s3=Service_details.objects.get(name="دواء دائم")
def  newpatient(request):
    x=None
    if Service_details.objects.filter(name="بطاقة صحية",status=False):
        messages.info(request, ' هذه الخدمة غير مفعلة حاليا')


    return render(request,'pages/newpatient.html',{'x':x})

def elec(request):
    if Service_details.objects.filter(name="أدوات كهربائية",status=False):
        messages.info(request, ' هذه الخدمة غير مفعلة حاليا')
    if request.method == 'POST' and 'btnsign' in request.POST:
        fname=None
        id_namber=None
        card_number=None
        name=None


        if 'fname' in request.POST:
            fname = request.POST['fname']
        else:
            messages.error(request, 'error in fname')
        if 'name' in request.POST:
            name = request.POST['name']
        else:
            messages.error(request, 'error in name')
        if 'id_namber' in request.POST:
            id_namber = request.POST['id_namber']
        else:
            messages.error(request, 'error in id_namber')
        if 'card_number' in request.POST:
            card_number = request.POST['card_number']
        else:
                messages.error(request, 'error in card_number')
        is_added =False
        if Person.objects.filter(id_namber=id_namber,card_number=card_number ,).exists():
            p = Person.objects.get(id_namber=id_namber, card_number=card_number)
            id2 = Service_details.objects.get(name='عائلات مستورة', status=True)
            id4 = Service_details.objects.get(name='كفالة أيتام')
            #req = Request.objects.get(idperson=p, idd=id2, request_place=None, status=2)
            if Request.objects.filter(idperson=p, idd=id2,  status=2).exists() or Request.objects.filter(idperson=p, idd=id4,  status=2).exists() :
                id3 = Service_details.objects.get(name='أدوات كهربائية')
                req1 = Request(idperson=p, idd=id3, request_place=name, status=5)
                if  Request.objects.filter(idperson=p, idd=id3,  status=5).exists():
                    messages.success(request, 'سبق وان طلبت هذه الخدمة  ')

                else:
                  req1.save()
                  is_added = True
                  contex={
                      'is_added':is_added
                  }
                  if Service_details.objects.filter(name="أدوات كهربائية", status=False):
                    messages.success(request, 'تم تسجيل طلبك لكن الخدمة غير متاحة الأن ستصلك رسالة اذا تم تفعيل هذه الخدمة')
                  else:
                      messages.success(request,'تم تسيجل طلبك ستصلك رسالة في حال تم قبول طلبك')
        else:  messages.info(request, 'عذرا انت لست مسجلا في الجمعية أو ان رقم البطاقة غير صحيح')
        contex = {
           'is_added': is_added }
    else:

         context = {}
         return render(request, 'pages/elec.html', context)
    contex={'is_added':is_added}
    return render(request,'part/success.html',contex)


