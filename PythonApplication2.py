def ask_password():
    for i in range(0, 3):
        s = input()
        if s == 'password':
            print('Пароль принят.')
        elif i == 2:
            print('неправельный пароль')


ask_password()
