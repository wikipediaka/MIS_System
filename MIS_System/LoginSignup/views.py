from django.shortcuts import render,redirect
from .models import Accounts

# Create your views here.
def SignUp(request):
    if request.method == "POST":

        signUp = Accounts(Id_Number = request.POST["ID"], Full_Name = request.POST["full_name"],Status = request.POST["Status"],Department = request.POST["Department"],Email = request.POST.get("email",False),Contact = request.POST["contact_number"], Password = request.POST["Password"])
        signUp.save()
        return redirect ("home/")

        
        
    else:    
        return render (request, "Sign-Up.html")
    
    
def HomeView(request):
    return render (request, "index.html")
        
