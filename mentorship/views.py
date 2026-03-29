from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import MentorRequest

User = get_user_model()


# 🔹 1. Show all mentors (only for students)
@login_required
def mentor_list(request):
    if request.user.role != 'student':
        return redirect('dashboard:home')   # ✅ fixed

    mentors = User.objects.filter(role='alumni')
    return render(request, 'mentorship/mentor_list.html', {'mentors': mentors})


# 🔹 2. Send mentorship request
@login_required
def send_request(request, mentor_id):
    mentor = get_object_or_404(User, id=mentor_id)

    # prevent duplicate request
    if MentorRequest.objects.filter(student=request.user, mentor=mentor).exists():
        return redirect('mentor_list')

    if request.method == 'POST':
        message = request.POST.get('message', '')

        MentorRequest.objects.create(
            student=request.user,
            mentor=mentor,
            message=message
        )

    return redirect('my_requests')


# 🔹 3. Student: view their requests
@login_required
def my_requests(request):
    requests = MentorRequest.objects.filter(student=request.user)
    return render(request, 'mentorship/my_requests.html', {'requests': requests})


# 🔹 4. Student: cancel request
@login_required
def cancel_request(request, request_id):
    req = get_object_or_404(MentorRequest, id=request_id)

    if req.student == request.user:
        req.delete()

    return redirect('my_requests')


# 🔹 5. Mentor panel (only alumni)
@login_required
def mentor_requests(request):
    if request.user.role != 'alumni':
        return redirect('home')

    requests = MentorRequest.objects.filter(mentor=request.user)
    return render(request, 'mentorship/mentor_requests.html', {'requests': requests})


# 🔹 6. Accept request
@login_required
def accept_request(request, request_id):
    req = get_object_or_404(MentorRequest, id=request_id)

    if request.user == req.mentor:
        req.status = 'accepted'
        req.save()

    return redirect('mentor_requests')


# 🔹 7. Reject request
@login_required
def reject_request(request, request_id):
    req = get_object_or_404(MentorRequest, id=request_id)

    if request.user == req.mentor:
        req.status = 'rejected'
        req.save()

    return redirect('mentor_requests')