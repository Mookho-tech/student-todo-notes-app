from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.db.models import Q
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
import calendar

from django.http import JsonResponse
from django.conf import settings

from .models import Task, Note
from .forms import TaskForm, NoteForm, CustomUserCreationForm
from .calendar_api import GoogleCalendarAPI

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def settings(request):
    # Simple placeholder page for now
    return render(request, 'todo_app/settings.html')


@login_required
def profile(request):
    return render(request, 'profile.html', {})


@login_required
def calendar_view(request):
    today = timezone.now().date()

    # Fetch only incomplete tasks for this month
    tasks = Task.objects.filter(
        user=request.user,
        due_date__month=today.month,
        due_date__year=today.year,
        is_completed=False
    )

    # Notes for this month
    notes = Note.objects.filter(
        user=request.user,
        created_at__month=today.month,
        created_at__year=today.year
    )

    # Build calendar grid
    cal = calendar.Calendar()
    month_days = cal.monthdayscalendar(today.year, today.month)

    # Prepare events list
    events = []

    # Tasks
    for task in tasks:
        if task.due_date:
            events.append({
                "title": task.title,
                "date": task.due_date,
                "type": "task",
                "priority": task.priority,
                "url": reverse("task_detail", args=[task.id]),
                "is_completed": task.is_completed,
            })

    # Notes
    for note in notes:
        events.append({
            "title": note.title,
            "date": note.created_at.date(),
            "type": "note",
            "url": reverse("note_detail", args=[note.id])
        })

    context = {
        "today": today,
        "month_days": month_days,
        "events": events,
        "month_name": today.strftime("%B"),
        "year": today.year,
    }

    return render(request, "calendar.html", context)


# -----------------------------
# GOOGLE CALENDAR EVENT CREATION
# -----------------------------
@login_required
def create_calendar_event(request, task_id=None):
    try:
        calendar_api = GoogleCalendarAPI(settings.GOOGLE_CALENDAR_CREDENTIALS_FILE)

        if task_id:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            start_time = task.due_date.isoformat() if task.due_date else "2025-11-26T09:00:00"

            event_data = {
                "summary": f"Task: {task.title}",
                "description": task.description,
                "start": {"dateTime": start_time, "timeZone": "Africa/Johannesburg"},
                "end": {"dateTime": start_time, "timeZone": "Africa/Johannesburg"},
            }
        else:
            event_data = {
                "summary": "Test Event",
                "start": {"dateTime": "2025-11-26T09:00:00", "timeZone": "Africa/Johannesburg"},
                "end": {"dateTime": "2025-11-26T10:00:00", "timeZone": "Africa/Johannesburg"},
            }

        created_event = calendar_api.create_event("primary", event_data)

        return JsonResponse({
            "status": "success",
            "event_url": created_event.get("htmlLink"),
            "event_id": created_event.get("id")
        })

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)


# -----------------------------
# AUTHENTICATION
# -----------------------------
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = CustomUserCreationForm()

    return render(request, "registration/register.html", {"form": form})


# -----------------------------
# DASHBOARD
# -----------------------------
@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user).order_by("-created_at")[:5]
    notes = Note.objects.filter(user=request.user).order_by("-created_at")[:5]

    context = {"tasks": tasks, "notes": notes}
    return render(request, "dashboard.html", context)


# -----------------------------
# TASK VIEWS
# -----------------------------
@login_required
def task_list(request):
    search_query = request.GET.get("search", "")
    tasks = Task.objects.filter(user=request.user)

    if search_query:
        tasks = tasks.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))

    return render(request, "tasks/task_list.html", {
        "tasks": tasks,
        "search_query": search_query
    })


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    return render(request, "tasks/task_detail.html", {"task": task})


@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("task_list")
    else:
        form = TaskForm()

    return render(request, "tasks/task_form.html", {"form": form, "title": "Create Task"})


@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)

    return render(request, "tasks/task_form.html", {"form": form, "title": "Update Task"})


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect("task_list")

    return render(request, "tasks/task_confirm_delete.html", {"task": task})


# -----------------------------
# NOTE VIEWS
# -----------------------------
@login_required
def note_list(request):
    search_query = request.GET.get("search", "")
    notes = Note.objects.filter(user=request.user)

    if search_query:
        notes = notes.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))

    return render(request, "notes/note_list.html", {"notes": notes, "search_query": search_query})


@login_required
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    return render(request, "notes/note_detail.html", {"note": note})


@login_required
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect("note_list")
    else:
        form = NoteForm()

    return render(request, "notes/note_form.html", {"form": form, "title": "Create Note"})


@login_required
def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm(instance=note)

    return render(request, "notes/note_form.html", {"form": form, "title": "Update Note"})


@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == "POST":
        note.delete()
        return redirect("note_list")

    return render(request, "notes/note_confirm_delete.html", {"note": note})
