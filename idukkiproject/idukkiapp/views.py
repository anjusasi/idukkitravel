from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Package


# Create your views here.
def index(request):
    obj=Package.objects.all()
    return render(request, 'index.html', {'result': obj})




# def book(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         age = request.POST['age']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         where = request.POST['where']
#         how = request.POST['how']
#         arrivals = request.POST['arrivals']
#         leaving = request.POST['leaving']
#         user = Book.objects.create_user(name=name, age=age, email=email, phone=phone, where=where,how=how, arrivals=arrivals, leaving=leaving)
#         user.save();
#
#     return redirect('/')




