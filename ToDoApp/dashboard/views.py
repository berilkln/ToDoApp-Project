from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

@login_required
def dashboard_home(request):
    # Kullanıcının görevlerini al
    tasks = Task.objects.filter(user=request.user)
    
    # Kullanıcı ve görevler ile birlikte şablona gönder
    return render(request, 'dashboard/dashboard.html', {
        'user': request.user,
        'tasks': tasks
    })

@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        is_completed = request.POST.get('is_completed') == 'on'
        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            is_completed=is_completed
        )
        return redirect('dashboard_home')
    return redirect('dashboard_home')




@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    
    if request.method == "POST":
        task.delete()
    
    return redirect('dashboard_home')  # Silme işleminden sonra kullanıcıyı dashboard'a yönlendir