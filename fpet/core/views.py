from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Pet



@login_required(login_url = '/login/')
def register_pet(request):
    return render(request, 'register-pet.html')

@login_required(login_url = '/login/')
def set_pet(request):
    city = request.POST.get('city')
    district = request.POST.get('district')
    description = request.POST.get('description')
    breed = request.POST.get('breed')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    photo = request.FILES.get('file')
    user = request.user
    pet = Pet.objects.create(city = city, district = district, description = description, breed = breed, 
                            phone = phone, email = email, photo = photo, user = user)
    url = '/pet/detail/{}/'.format(pet.id)
    return redirect(url)

@login_required(login_url = '/login/')
def delete_pet(request, id):
    pet = Pet.objects.get(id=id)
    pet.delete()
    return redirect('/')



@login_required(login_url = '/login/')
def list_all_pets(request):
    pet = Pet.objects.filter(active = True)
    return render(request, 'list.html',{'pet':pet})

def list_user_pets(request):
    pet = Pet.objects.filter(active = True, user = request.user)
    return render(request, 'list.html',{'pet':pet})

def pet_detail(request, id):
    pet = Pet.objects.get(active = True, id=id)
    print(pet.id)
    return render(request, 'pet.html',{'pet':pet})

def logout_user(request):
    logout(request)
    return redirect('/login/')

def login_user(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request,'Usuário e senha invalido! Tente novamente.')
    return redirect('/login/')
   

