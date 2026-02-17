from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, Q
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Student, Attendance
from .forms import StudentForm, AttendanceForm
import json


# ==============================
# AUTHENTICATION (SIGNUP)
# ==============================

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('student_list')
    else:
        form = UserCreationForm()

    return render(request, 'students/signup.html', {'form': form})


# ==============================
# USER LIST (ADMIN ONLY)
# ==============================

def is_admin(user):
    return user.is_superuser


@user_passes_test(is_admin)
def user_list(request):
    users = User.objects.all()
    return render(request, 'students/user_list.html', {'users': users})


# ==============================
# STUDENT VIEWS
# ==============================

@login_required
def student_list(request):
    query = request.GET.get('q')

    if query:
        students = Student.objects.filter(name__icontains=query)
    else:
        students = Student.objects.all()

    return render(request, 'students/student_list.html', {
        'students': students
    })


@login_required
def add_student(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'students/student_form.html', {'form': form})


@login_required
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'students/student_form.html', {'form': form})


@login_required
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')


# ==============================
# DASHBOARD
# ==============================

@login_required
def dashboard(request):
    total_students = Student.objects.count()

    department_data = Student.objects.values('department').annotate(
        count=Count('department')
    )

    departments = [item['department'] for item in department_data]
    counts = [item['count'] for item in department_data]

    context = {
        'total_students': total_students,
        'departments': json.dumps(departments),
        'counts': json.dumps(counts),
    }

    return render(request, 'students/dashboard.html', context)


# ==============================
# ATTENDANCE
# ==============================

@login_required
def attendance_list(request):
    records = Attendance.objects.all()

    summary = Student.objects.annotate(
        total_days=Count('attendance'),
        present_days=Count(
            'attendance',
            filter=Q(attendance__status='Present')
        ),
        absent_days=Count(
            'attendance',
            filter=Q(attendance__status='Absent')
        ),
    )

    for student in summary:
        if student.total_days > 0:
            student.percentage = round(
                (student.present_days / student.total_days) * 100, 2
            )
        else:
            student.percentage = 0

    context = {
        'records': records,
        'summary': summary,
    }

    return render(request, 'students/attendance_list.html', context)


@login_required
def add_attendance(request):
    form = AttendanceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('attendance_list')
    return render(request, 'students/attendance_form.html', {'form': form})


@login_required
def edit_attendance(request, pk):
    record = get_object_or_404(Attendance, pk=pk)
    form = AttendanceForm(request.POST or None, instance=record)

    if form.is_valid():
        form.save()
        return redirect('attendance_list')

    return render(request, 'students/attendance_form.html', {'form': form})


@login_required
def delete_attendance(request, pk):
    record = get_object_or_404(Attendance, pk=pk)
    record.delete()
    return redirect('attendance_list')
