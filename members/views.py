from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .forms import RegisterUserForm
from datetime import datetime
from .models import Task
from .forms import TaskForm
import pandas as pd
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Task
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.username == "admin11":
                return redirect('export_users_data')  # Redirect to the export view if the user is lena13
            return redirect('success')  # Redirect to success page for other users
        else:
            messages.error(request, "Ошибка, попробуйте снова")
            return redirect('login')
    else:
        return render(request, 'members/auth/login.html', {})




def register_user(request):

    if request.method == 'POST':
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get("password1") # This ensures that the data is safe and meets the required criteria before it is used.
            user= authenticate(username= username, password = password)
            login(request, user)
            messages.success(request, f'Вы успешно зарегистрированы, {username}')
            return redirect('login')
    else:
        form = RegisterUserForm()

    return render(request, 'members/html/registration.html', {'form': form})





def main(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            today = datetime.now().date()
            user = request.user

            # Check if a task exists for the user for today's date
            if Task.objects.filter(user=user, date__date=today).exists():
                # If a task already exists, show an error message
                error = "Вы уже ввели данные сегодня. Повторный ввод невозможен."
            else:
                # If no task exists, save the new task
                task = form.save(commit=False)
                task.user = user
                task.date = datetime.now()  # Set the current date and time
                task.save()
                return redirect('success')  # Redirect to a success page

    else:
        form = TaskForm()

    # Render the form with the error message if any
    return render(request, 'members/html/main.html', {'form': form, 'error': error})








def export_users_data(request):
    # Ensure the user is authenticated and is lena13
    if not request.user.is_authenticated or request.user.username != 'admin11':
        messages.error(request, "Unauthorized access")
        return redirect('login')  # Redirect to login if user is not authorized

    data = []

    users = User.objects.all()

    for user in users:
        tasks = Task.objects.filter(user=user)
        gruz_translation = lambda gruz: 'Кукурудза' if gruz == 'corn' else 'Пшениця' if gruz == 'wheat' else gruz

        for task in tasks:
            data.append({
                'Имя': user.first_name,
                'Фамилия': user.last_name,
                'Мiсце заправки': task.misto,
                'Груз': gruz_translation(task.gruz),
                'Количество топлива всього': task.litres,
                'Ціна за паливо всього': task.price,
                'Масса': task.massa,
                'Мiсце завантаження': task.punkt,
                'Мiсце розвантаження': task.rozvantazhennya_mistse, #!!!!!!!!!!!!!!!!!

                'Держномер авто': task.derzh_nomer,
                'Номер ТТН': task.ttn_nomer,
                'Дата и время завантаження': task.zavantazhennya_datetime.strftime('%Y-%m-%d %H:%M:%S') if task.zavantazhennya_datetime else '',
                'Дата и время розвантаження': task.rozvantazhennya_datetime.strftime('%Y-%m-%d %H:%M:%S') if task.rozvantazhennya_datetime else '',
                'Количество перевезенного вантажу': task.skilki_vantazhu,
                'Показ одометра при выезде': task.odometr_viyizd,
                'Показ одометра при заезде': task.odometr_zayizd,
                'Заправка дата и время': task.zapravka_datetime.strftime('%Y-%m-%d %H:%M:%S') if task.zapravka_datetime else '',
                'Примечания': task.prymitky,
                'Дата отправки формы': task.date.strftime('%Y-%m-%d %H:%M:%S'),
            })

    df = pd.DataFrame(data)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=users_data.xlsx'

    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)

    return response

