from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import user
from django.contrib import messages

def home(request):
    obj=user.objects.all()
    parms={"userdata":obj}
    return render(request,"home.html",parms)

def adduser(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        id=request.POST.get("id")
        print(id)
        if id:
            obj=user.objects.get(pk=id)
            obj.name=name
            obj.email=email
            obj.password=password
            obj.save()
            obj2=user.objects.values()
            userdata=list(obj2)
            return JsonResponse({"status":2,"userdata":userdata})
        else:    
            obj1=user(name=name,email=email,password=password)
            obj1.save()
            obj2=user.objects.values()
            userdata=list(obj2)
            return JsonResponse({"status":1,"userdata":userdata})
    else:
         return JsonResponse({"status":0})    

def delete(request):
    if request.method=="POST":
        id=request.POST["id"]
        obj=user(pk=id)
        obj.delete()
        return JsonResponse({"status":1})
    else:
        return JsonResponse({"Status":0}) 

def Edit(request):
    if request.method=="POST":
       id=request.POST["id"]
       print(id)
       obj=user.objects.get(pk=id) 
       params={"name":obj.name,"email":obj.email,"password":obj.password,"id":obj.id}
       return JsonResponse({"status":1,"userdata":params})
    else:
        return JsonResponse({"Status":0})

            