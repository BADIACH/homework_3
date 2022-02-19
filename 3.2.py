def print_user(name, surname, year_of_birth, city_of_residence, email, phone, my_user=None):
    print(f'пользователь {name} {surname} {year_of_birth}-го рождения, проживает в городе {city_of_residence},'
          f'имеет Email {email} и телефон {phone}')
user_terminal = {
    'name' : 'имя',
    'surname' : 'фамилия',
    'year_of_birth' : 'год рождения',
    'city_of_residence': 'город',
    'email' : 'эмейл' ,
    'phone' : 'телефон'
    }
my_user = {}
for key, value in user_terminal.items():
    input_value = input(f'{value}: ')
    my_user.update({key: input_value})
print_user(**my_user)