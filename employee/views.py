from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# التطبيق رقم 1 
# def get_employee(request):
#     template=loader.get_template('employee.html')
#     return HttpResponse(template.render())

# التطبيق رقم 2
# def get_employee(request):

#     employyes=[
#         {"id":1,"name":"جمال احمد","sal":6000,"email":"example@mail.com","phone":"1234577777"},
#         {"id":2,"name":",وليد خالد","sal":6500,"email":"example@mail.com","phone":"1234577777"},
#         {"id":3,"name":",حسين طلال","sal":7000,"email":"example@mail.com","phone":"1234577777"},
#         {"id":4,"name":",سعد  عبدالله","sal":8000,"email":"example@mail.com","phone":"1234577777"},
#         {"id":5,"name":",محمد  عمر","sal":8000,"email":"example@mail.com","phone":"1234577777"},        
#     ]
#     context={
#         'emp':employyes
#     }
#     return render(request,"employee.html",context)


# التطبيق رقم 3 ايجاد اعلى راتب واقل راتب 
def get_employee(request):

    employyes=[
        # {object الاقواس هذي معناها }
        {"id":1,"name":"جمال محمد","sal":6000,"email":"example@mail.com","phone":"1234577777"},
        {"id":2,"name":",وليد خالد","sal":6500,"email":"example@mail.com","phone":"1234577777"},
        {"id":3,"name":",حسين طلال","sal":7000,"email":"example@mail.com","phone":"1234577777"},
        {"id":4,"name":",سعد  عبدالله","sal":8000,"email":"example@mail.com","phone":"1234577777"},
        {"id":5,"name":",محمد  عمر","sal":9000,"email":"example@mail.com","phone":"1234577777"},        
    ]
    
    search=request.GET.get('search')
    action=request.GET.get('action')


    if search:
        filtred=[]
        for s in employyes:
            if search in s["name"]:
                filtred.append(s)


        employyes=filtred

    if action=="max":
        max_sal=max(s["sal"] for s in employyes) # ايجاد اعلى راتب 
        employyes=[s for s in employyes if s["sal"]==max_sal] # تخزين فقط السجل الذي يحتويعلى اعلى راتب
    

    if action=="min":
        max_sal=min(s["sal"] for s in employyes) # ايجاد اعلى راتب 
        employyes=[s for s in employyes if s["sal"]==max_sal] # تخزين فقط السجل الذي يحتويعلى اعلى راتب


    context={
        'emp':employyes
    }

    return render(request,"employee.html",context)