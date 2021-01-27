from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Pet, Euvi




@login_required(login_url = '/login/')
def register_pet(request):
    pet_id = request.GET.get('id')
    if pet_id:
        pet = Pet.objects.get(id=pet_id)
        if pet.user == request.user:
            return render(request, 'register-pet.html', {'pet':pet})
    return render(request, 'register-pet.html')


@login_required(login_url = '/login/')
def euvi_pet(request):
    return render(request, 'euvi.html')

@login_required(login_url = '/login/')
def set_euvi(request):
    city = request.POST.get('city')
    district = request.POST.get('district')
    description = request.POST.get('description')
    phone = request.POST.get('phone')
    photo = request.FILES.get('file')
    user = request.user
    euvi = Euvi.objects.create(city = city, district = district, description = description,
                            phone = phone, photo = photo, user = user)
    url = '/pet/euvi/{}/'.format(euvi.id)
    return redirect(url)


@login_required(login_url = '/login/')
def set_pet(request):
    name_pet = request.POST.get('name_pet')
    owner = request.POST.get('owner')
    city = request.POST.get('city')
    district = request.POST.get('district')
    description = request.POST.get('description')
    breed = request.POST.get('breed')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    photo = request.FILES.get('file')
    pet_id = request.POST.get('pet-id')
    user = request.user
    if pet_id:
        pet = Pet.objects.get(id=pet_id)
        if user == pet.user:
            pet.name_pet = name_pet
            pet.owner = owner
            pet.city = city
            pet.district = district
            pet.description = description
            pet.breed = breed
            pet.phone = phone
            pet.email = email
            if photo:
                pet.photo = photo
            pet.save()            
    else:
        pet = Pet.objects.create(name_pet = name_pet , owner = owner, city = city, district = district, description = description, breed = breed, 
                                phone = phone, email = email, photo = photo,  user = user)
    url = '/pet/detail/{}/'.format(pet.id)
    return redirect(url)

@login_required(login_url = '/login/')
def delete_pet(request, id):
    pet = Pet.objects.get(id=id)
    if pet.user == request.user:
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
   

