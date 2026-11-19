from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
def home(request):
    if request.method == 'POST':
        # ফর্ম থেকে ডাটা নেওয়া
        name = request.POST.get('name')
        student_id = request.POST.get('student_id')
        dept = request.POST.get('dept')

        Student.objects.create(
            name=name,
            student_id=student_id,
            dept=dept
        )
        return redirect('home')  

    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.dept = request.POST.get('dept')
        student.save()  
        return redirect('home') 
        
    return render(request, 'edit_student.html', {'student': student})



def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete() 
    return redirect('home')  