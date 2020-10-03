from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm
from django.contrib import messages

# Create your views here.
def insert_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"One record inserted successfully!!")
            return redirect('/')
    return render(request,'auth/insert.html',{'form':form})


def show_view(request):
    students = Student.objects.all()
    return render(request,'auth/show.html',{'students':students})

def delete_view(request,id):
    students = Student.objects.get(id = id)
    students.delete()
    messages.success(request,"One record deleted successfully!!")
    return redirect('/')

def update_view(request,id):
    students = Student.objects.get(id = id)
    form = StudentForm(request.POST,instance=students)
    if form.is_valid():
        form.save(commit=True)
        messages.success(request,"Record Updated Successfully!!")
        return redirect('/show')
    return render(request,'auth/update.html',{'students':students})



