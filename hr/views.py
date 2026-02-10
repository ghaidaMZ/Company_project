# from unittest import loader
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse('welcome to first lesson in views')

def total(request):
    return HttpResponse('1000')

def tax(request,number):
    return HttpResponse(number*0.15)

def landpage(request):
    return HttpResponse('welcome to home page')

def print(request,name):
    return HttpResponse(name)

def show_index(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())

def depts(request):

# URLجلب قيمة البحث من ال
# /depts/?search=البرمجة
    search=request.GET.get('search')

    departments = [
        "المحاسبة",
        "الموارد البشرية",
        "البرمجة",
        "قسم الشتريات ",
        ]
    
#  لو المستخدم كتب كلمة بحث نفلتر الأقسام ونخلي بس الأقسام اللي فيها كلمة البحث
# search = "البر" النتيجة 👉 "البرمجة"
# دي اسمها List Comprehension
    if search:
        departments=[d for d in departments if search in d]

    s="ghaida"
    tax="2500"
# هنا Django بيحمّل ملف depts.html من مجلد templates.
    template=loader.get_template('depts.html')

    context={
        'depts' : departments,
        's1' :s,
        't': tax,
        }
# البيانات اللي بتنرسل لصفحه وتستخدم كذا 
# {{ depts }}
    
    return HttpResponse(template.render(context,request))
# يتم دمج القالب مع البيانات ثم إرجاع الصفحة النهائية إلى المتصفح

#---------------------------------------------------------
# يمكن اختصار الكود باستخدام الدالة render:
# return render(request, 'depts.html', context)