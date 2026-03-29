from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, JoinRequest


@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'collaboration/project_list.html', {'projects': projects})


@login_required
def create_project(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        skills = request.POST['skills']

        Project.objects.create(
            title=title,
            description=description,
            skills_required=skills,
            created_by=request.user
        )

        return redirect('project_list')

    return render(request, 'collaboration/create_project.html')

# send join requrest to the project creater
@login_required
def send_join_request(request, project_id):
    print("JOIN CLICKED")
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        if not JoinRequest.objects.filter(project=project, student=request.user).exists():
            JoinRequest.objects.create(
                project=project,
                student=request.user
            )

    return redirect('project_list')


@login_required
def project_requests(request):
    projects = Project.objects.filter(created_by=request.user)
    requests = JoinRequest.objects.filter(project__in=projects)

    return render(request, 'collaboration/project_requests.html', {'requests': requests})

# add team member
@login_required
def accept_join(request, request_id):
    req = get_object_or_404(JoinRequest, id=request_id)

    if request.user == req.project.created_by:
        req.status = 'accepted'
        req.project.members.add(req.student)  # 🔥 add to team
        req.save()

    return redirect('project_requests')


@login_required
def reject_join(request, request_id):
    req = get_object_or_404(JoinRequest, id=request_id)
    req.status = 'rejected'
    req.save()
    return redirect('project_requests')


@login_required
def my_projects(request):
    projects = request.user.joined_projects.all()
    return render(request, 'collaboration/my_projects.html', {'projects': projects})