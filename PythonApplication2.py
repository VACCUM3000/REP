def ask_password():
    for i in range(0, 3):
        s = input()
        if s == 'password':
            print('������ ������.')
        elif i == 2:
            print('������������ ������')


ask_password()
