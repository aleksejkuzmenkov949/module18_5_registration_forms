from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


def sign_up_by_html(request):
    users = ['Alex', 'Darja', 'Cat31']
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        # Выводим информацию в консоль
        print(f'Полученные данные: username={username}, password={password}, '
              f'repeat_password={repeat_password}, age={age}')

        if username in users:
            info['error'] = 'Пользователь уже существует'
            print(info['error'])
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
            print(info['error'])
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            print(info['error'])
        else:
            print(f'Приветствуем,  {username} !')
            return render(request, 'fifth_task/registration_page.html',
                          {'username': username})

    return render(request, 'fifth_task/registration_page.html', {'info': info})


def sign_up_by_django(request):
    users = ['Alex', 'Darja', 'Cat31']
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)

        # Проверяем, валидна ли форма
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            try:
                age = int(form.cleaned_data['age'])

                # Проверка на несовпадение паролей
                if password != repeat_password:
                    form.add_error('repeat_password', 'Пароли не совпадают')
                elif age < 18:
                    form.add_error('age', 'Вы должны быть старше 18 лет')
                elif username in users:
                    form.add_error('username', 'Пользователь уже существует')
                else:
                    info['success'] = f"Приветствуем, {username}!"
                    # Возвращаем объект HttpResponse с приветственным сообщением
                    return HttpResponse(info['success'])

            except ValueError:
                form.add_error('age', 'Введите корректное число для возраста')

        # Если форма невалидна, выводим ошибки формы
        info['form_errors'] = form.errors
    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'fifth_task/sign_up.html', info)