from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Client, Job
from .forms import ClientForm, JobForm

def dashboard(request):
    site_name = "JobTracker"
    clients_count = Client.objects.count()
    jobs_count = Job.objects.count()
    active_jobs = Job.objects.filter(status="in_progress").count()
    completed_jobs = Job.objects.filter(status="completed").count()
    upcoming_jobs = Job.objects.order_by('finish_date')[:5]  # next 5 jobs

    return render(request, 'dashboard.html', {
        'site_name': site_name,
        'clients_count': clients_count,
        'jobs_count': jobs_count,
        'active_jobs': active_jobs,
        'completed_jobs': completed_jobs,
        'upcoming_jobs': upcoming_jobs,
    })


# CLIENT CRUD
def client_list(request):
    query = request.GET.get("q")
    if query:
        clients = Client.objects.filter(name__icontains=query)
    else:
        clients = Client.objects.all()
    return render(request, "client_list.html", {"clients": clients, "query": query})

def client_create(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("client_list")
    else:
        form = ClientForm()
    return render(request, "client_form.html", {"form": form})

def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect("client_list")
    else:
        form = ClientForm(instance=client)
    return render(request, "client_form.html", {"form": form})

def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        client.delete()
        return redirect("client_list")
    return render(request, "client_confirm_delete.html", {"client": client})


# JOB CRUD
def job_list(request):
    query = request.GET.get("q")
    if query:
        jobs = Job.objects.filter(
            Q(description__icontains=query) |
            Q(client__name__icontains=query)
        )
    else:
        jobs = Job.objects.all()
    return render(request, "job_list.html", {"jobs": jobs, "query": query})

def job_create(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("job_list")
    else:
        form = JobForm()
    return render(request, "job_form.html", {"form": form})

def job_update(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect("job_list")
    else:
        form = JobForm(instance=job)
    return render(request, "job_form.html", {"form": form})

def job_delete(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == "POST":
        job.delete()
        return redirect("job_list")
    return render(request, "job_confirm_delete.html", {"job": job})
