from django.shortcuts import render
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate,  login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, HttpResponse, redirect
import json
import datetime 
from datetime import date, datetime, time
from django.contrib import messages
from .models import Notes


def Home(request):
    if(request.user.is_authenticated):

        post = Notes.objects.filter(Admin_Email = request.user.email)


        return render(request, 'notes/notes.html', {"p":post})
    
    return render(request, 'notes/home.html')


    

def Pass(request):
    return render(request, 'notes/pass.html')

def dell(request, inn):
    ps = Notes.objects.filter(Admin_Email = request.user.email)
    for p in ps:
        if p.fno == inn:
            p.delete()
    return redirect('Home')

def read(request, innn):
    ps = Notes.objects.filter(Admin_Email = request.user.email)

    
    for p in ps:
        if p.fno == innn:
            return render(request, 'notes/read.html',{"p":p} )

            

            
    return redirect('Home')

    



def save(request):
    if request.method == "POST":
        title = request.POST.get('title')
        note = request.POST.get('note')
        auth = request.user.first_name
        e = request.user.email
        auth_us = request.user
        t = datetime.now()
        n =  Notes(Title = title, Disc=note, Admin_Name = auth,Admin_Username=auth_us,Admin_Email=e, Timestamp_Created=t  )
        if auth != "" and title != "":
            n.save()
    return redirect('Home')




    

def hlogout(request):
    logout(request)
    return redirect('Home')