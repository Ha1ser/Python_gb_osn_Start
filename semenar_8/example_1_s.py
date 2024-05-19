def show_menu():
    print("\n***Телефонная книжка***\n" 
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Изменить номер телефона\n"
          "6. Удалить абонента"
          "7. Закончить работу")  
    
    while True:
        try :
            choice = int(input('Выберите необходимое действие: '))
            if choice < 1 or choice > 7:
                work_with_phonebook()
            break
        except:
            print('Ошибка ввода')
        
    return choice

def read_show(filename):
    print('\n***Распечатан весь телефонный справочник***') 
    with open(filename,'r',encoding='utf-8') as data:
        names = data.readlines()
        #phonebook = sorted(names)
    print(*names) 

def read_txt(filename): 
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон']

    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)	
    return phone_book 

def write_txt(filename , phone_book): 

    with open(filename,'w' ,encoding='utf-8') as phout:

        for i in range(len(phone_book)):
            s='' 
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n') 

def add_user(user_lastname, user_number, user_firstname=''):
    with open('temp.txt', 'w', encoding='utf-8') as data:
        data.write(user_firstname +' ' + user_firstname + ' '+ user_number +' \n'+ ' \n' + ' \n')
    new_data = read_txt('temp.txt')
    return new_data



def work_with_phonebook():
    choice = show_menu() #меню

    filename = 'phonebook.txt'

    phone_book = read_txt('phonebook.txt') 

    while (choice != 8):

        if choice==1: #отобразить весь справочник
            read_show(filename)
            input('Для продолжения нажмите [Enter] .  .  .')

        elif choice==2: #найти абонента по фамилии
            last_name=input('Введите Фамилию: ').upper()
            print('Совпадения:', find_by_lastname(filename, last_name), sep='\n') 
            input('Для продолжения нажмите [Enter] .  .  .')

        elif choice==3: #найти абонента по номеру
            last_name=input('Введите номер: ')
            print('Совпадения:', *find_by_lastname(filename, number), sep='\n') 
            input('Для продолжения нажмите [Enter] .  .  .')
            print(change_number(phone_book,last_name,new_number))
	    	
        elif choice==4: # добавить абонента в справочник
            print('\n***Добавить нового абонента в телефонную книгу***\n')
            user_lastname = input('Введите *Фамилию: ').upper()
            user_firstname = input('Введите Имя: ').upper()
            user_firstname = input('Введите номер *Телефона: ')
            new_data = add_user(user_lastname, user_number, user_firstname)
            print('Абонент добавлен!')
            write_txt(filename, phone_book + new_data) #добавить в словарь новый словарь и записать в книгу
            time.sleep(3)

        elif choice==5: # изменить номер абонента
            last_name = input('Введите фамилию: ').upper()
            last_name = input('Введите новый номер: ').upper()

            new_data =change_number(filename, phone_book, last_name, new_number) #возвращает запись в temp.txt
            print(find_by_number(phone_book,number))

        elif choice==6: 
            user_data=input('new data ')
            add_user(phone_book,user_data)
            write_txt('semenar_8\phonebook.txt',phone_book) 


        choice=show_menu()


print(work_with_phonebook())