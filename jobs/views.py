from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import JobApplication
from .forms import JobApplicationForm

@login_required
def dashboard(request):

    jobs = JobApplication.objects.filter(
        user=request.user
    )

    return render(
        request,
        'dashboard.html',
        {'jobs': jobs}
    )


@login_required
def add_job(request):

    if request.method == 'POST':

        form = JobApplicationForm(request.POST)

        if form.is_valid():

            job = form.save(commit=False)
            job.user = request.user
            job.save()

            return redirect('dashboard')

    else:
        form = JobApplicationForm()

    return render(
        request,
        'add_job.html',
        {'form': form}
    )