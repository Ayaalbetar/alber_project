from django.contrib import admin
from .models import  Services ,Service_details,Person,Request,Advertising
# Register your models here.
class RequestInline(admin.TabularInline):
    model = Request
    extra = 0
class PersonInline(admin.TabularInline):
    model =Person
    extra = 0

admin.site.register(Services)
class AdminServic_details(admin.ModelAdmin):
    inlines = (RequestInline,)
admin.site.register(Service_details,AdminServic_details)

class AdminRrquest(admin.ModelAdmin):

    fields = []
    def  req(self,obj):
        return obj.request_date

    #def show(self,obj):
        #d = Request.objects.filter(idd= 1).count()
        #return d

    req.short_description = " تاريخ الطلب"
    f=[ 'idperson','req','status','idd',]
    f1 = ['request_date', 'status', 'idd', ]
    s=['idperson']
    list_display = f
    list_filter = f1
    list_display_links=s

    def get_form(self, request, obj=None, **kwargs):
      form = super().get_form(request, obj, **kwargs)
      form.base_fields["idd"].label = "اسم الخدمة"
      form.base_fields["idperson"].label = "اسم المستفيد:"
      form.base_fields["status"].label = "رقم الخدمة:"
      form.base_fields["request_place"].label = "مركز استلام الخدمة"
      return form

admin.site.register(Request,AdminRrquest)



class AdminPerson(admin.ModelAdmin):
    inlines = (RequestInline,)
    def full(self,obj):
        return obj.fname+" "+obj.lname
    def ids(self,obj):
        return obj.id_namber
    def amount_money(self,obj):
        return obj.amount_money;

    def isseens(self, obj):
        return obj.isseen;

    def acceptedd(self, obj):
        return obj.accepted;
    fields = []
    full.short_description = "الاسم الكامل"

   # isseens.short_description = "تمت مشاهدته"
    amount_money.short_description = " المبلغ"
    ids.short_description = " الرقم الوطني"
    ff=['full','ids','amount_money','isseen','accepted']
    f=['amount_money']
    f1 = ['full',  ]
    list_display = ff
    list_display_links =f1
    f3=['isseen','amount_money','accepted']
    list_editable = f3
    list_filter = f3
    search_fields = ff

    class Meta:
        ordering = ("last_name", "first_name")

    def get_form(self, request, obj=None, **kwargs):
      form = super().get_form(request, obj, **kwargs)
      form.base_fields["isseen"].label = "تمت مشاهدت"
      form.base_fields["fname"].label = "الاسم:"
      form.base_fields["pname"].label = "اسم الأب:"
      form.base_fields["mname"].label = "اسم الأم:"
      form.base_fields["lname"].label = "الكنية:"
      form.base_fields["motherln"].label = "انسبة الأم:"
      form.base_fields["phone"].label = "االهاتف:"
      form.base_fields["id_namber"].label = "االرقم الوطني:"
      form.base_fields["address"].label = "االعنوان:"
      form.base_fields["place_birth"].label = "امكان الولادة:"
      form.base_fields["hasbend"].label = "اسم الزوج:"
      form.base_fields["gender"].label = "الجنس:"
      form.base_fields["fhasbend"].label = "اسم الزوجة"
      form.base_fields["card_number"].label = "رقم البطاقة ا"
      form.base_fields["email"].label = "البريد الالكتروني"
      form.base_fields["accepted"].label = "تم قبوله:"
      form.base_fields["amount_money"].label = "المبلغ:"
      form.base_fields["percentage_health"].label = "النسبة المئوية للصحته"
      form.base_fields["birthday"].label = "المواليد:"
      form.base_fields["nationality"].label = "الجنسية:"
      form.base_fields["father_die"].label = "الأب متوفي:"
      form.base_fields["photo"].label = "الصور:"

      return form



admin.site.register(Person,AdminPerson)
class AdminAdvertisin (admin.ModelAdmin):
     fields = []

     def get_form(self, request, obj=None, **kwargs):
       form2 = super().get_form(request, obj, **kwargs)
       form2.base_fields["title"].label = "العنوان"
       form2.base_fields["details"].label = "التفاصيل"
       form2.base_fields["photo"].label = " الصور"
       return form2;


admin.site.register(Advertising,AdminAdvertisin)


