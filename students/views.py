from django.shortcuts import render
from .models import Student

def home(request):
    return render(request, 'students/home.html')

def add_student(request):
    if request.method == "POST":
        name = request.POST['name']
        roll = request.POST['roll']
        course = request.POST['course']
        marks = request.POST['marks']

        Student.objects.create(
            name=name,
            roll_number=roll,
            course=course,
            marks=marks
        )

    return render(request, 'students/add_student.html')
def view_students(request):
    students = Student.objects.all()
    return render(request, 'students/view_students.html', {'students': students})
from django.shortcuts import render, redirect

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('view_students')
def edit_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.name = request.POST['name']
        student.roll_number = request.POST['roll']
        student.course = request.POST['course']
        student.marks = request.POST['marks']
        student.save()

        return redirect('view_students')

    return render(request, 'students/edit_student.html', {'student': student})