import datetime
import os

class Note:
    '''
    This class encapsulates notes with id, title, body and date
    '''
    def __init__(self, id, title, body):
        self.__id = id
        self.__title = title
        self.__body = body
        self.__update = datetime.datetime.now()

    '''
    Gets self.__id
    '''
    def get_id(self):
        return self.__id

    '''
    Gets self.__update
    '''
    def get_update(self):
        return self.__update

    '''
    Gets self.__title
    '''
    def get_title(self):
        return self.__title

    '''
    Gets self.__body
    '''
    def get_body(self):
        return self.__body

    '''
    Sets self.__date
    '''
    def set_update(self, date):
        self.__update = date

    '''
    Sets self.__title
    '''
    def set_title(self, title):
        self.__title = title
    
    '''
    Sets self.__body
    '''
    def set_body(self, body):
        self.__body = body

    def print_note(self):
        '''
        Prints note
        '''
        print('  --{2}--\n{3}\nid:{0:2} update:{1}'.format(self.__id, self.__update.strftime("%y-%m-%d %H:%M:%S"), self.__title, self.__body))
        print('-'*30)

class NotesAdministrator:
    '''
    This class provides methods for administering a collection of notes
    '''
    def __init__(self):
        self.__work_dir = os.getcwd()
        self.__file_notes = ("{0}\\notes.csv".format(self.__work_dir))
        self.__notes = list()
        self.__sort_order = 0
        self.__SEPARATOR = "-"*63 
        
    def run_admin(self):
        '''
        Manages the list of notes
        '''
        user_choice = self.__main_menu()
        while user_choice != 0:
            if user_choice == 1:
                self.__print_all()
            elif user_choice == 2:
                self.__save_file()
            elif user_choice == 3:
                self.__read_file()
            elif user_choice == 4:
                index = self.__int_input("Введите id заметки--> ")
                self.__edit_note(index)
            elif user_choice == 5:
                index = self.__int_input("Введите id заметки--> ")
                self.__remove_note(index)
            elif user_choice == 6:
                self.__add_note()
            elif user_choice == 7:
                self.__change_sort_order()
            elif user_choice == 8:
                self.__load_demo()
            user_choice = self.__main_menu()
            print('\n')

    def __int_input(self, message):
        '''
        Checks input
        '''
        my_input = input(message)
        if my_input.isdigit():
            return int(my_input)
        else:
            print("Введите целое число!")
            return self.__int_input(message)

    def __load_demo(self):
        '''
        Loads test (Note) instances to self.__notes
        '''
        self.__notes.clear()
        for i in range(0, 10):
            id = self.__get_new_id()
            title = ('Заметка №{0}'.format(i + 1))
            body = ('Тело заметки №{}'.format(i + 1))
            note = Note(id, title, body)
            self.__notes.append(note)

    def __remove_note(self, id):
        '''
        Removes self.__notes[id]
        '''
        index = self.__get_index(id)
        if index == -1:
            print("Записи с таким id нет в списке")
        else:
            print("Удалена заметка:")
            self.__notes.pop(index).print_note()

    def __print_all(self):
        '''
        Prints to console all notes from self.__notes with self.__sort_order
        '''
        if self.__sort_order == 0:
            self.__notes.sort(key=lambda x: x.get_id())
        elif self.__sort_order == 1:
            self.__notes.sort(key=lambda x: x.get_update())
        for x in self.__notes:
            x.print_note()

    def __save_file(self):
        '''
        Writes self.__notes to ./notes.csv
        '''
        file_notes = open(self.__file_notes, 'w', encoding='utf-8')
        for note in self.__notes:
            file_notes.write('{0};{1};{2};{3}\n'.format(note.get_id(), note.get_update(), note.get_title(), note.get_body()))
        file_notes.close()
        print("Запись в файл:\n{0}".format(self.__file_notes))
        
    def __read_file(self):
        '''
        Read ./notes.csv to self.__notes
        '''
        if os.path.exists(self.__file_notes):
            self.__notes.clear()
            file_notes = open(self.__file_notes, 'r')
            line = file_notes.readline().rstrip()
            while len(line) != 0:
                array =  line.split(';')
                id = int(array[0])
                title = array[2]
                body = array[3]
                note = Note(id, title, body)
                update = datetime.datetime.strptime(array[1], '%Y-%m-%d %H:%M:%S.%f')
                note.set_update(update)
                self.__notes.append(note)
                line = file_notes.readline().rstrip()
            file_notes.close()
        else:
            print("Файл {0} не существует".format(self.__file_notes))

    def __add_note(self):
        '''
        Adds (Note)note to self.__notes
        '''
        id = self.__get_new_id()
        title = input("Введите текст заголовка--> ")
        body = input("Введите текст заметки--> ")
        note = Note(id, title, body)
        self.__notes.append(note)

    def __get_new_id(self):
        '''
        Gets new unique id for self.__notes
        '''
        if len(self.__notes) > 0:
            #list_id = [x.get_id() for x in self.__notes]
            return max([x.get_id() for x in self.__notes]) +1
        return 1

    def __get_index(self, id):
        '''
        Return index with self.__notes[index] == id
        '''
        index = -1
        if len(self.__notes) > 0:
            for i in range(len(self.__notes)):
                if (self.__notes[i].get_id() == id):
                    index = i
                    #break
        return index

    def __edit_note(self, id):
        '''
        Changes self.__notes.get__id == id
        '''
        index = self.__get_index(id)
        if index == -1:
            print("Записи с таким id нет в списке")
        else:
            edit_choice = self.__edit_menu(index)
            while edit_choice != 0:
                if edit_choice == 1:
                    title = input("Введите новый заголовок:\n--> ")
                    self.__notes[index].set_title(title)
                elif edit_choice == 2:
                    body = input("Введите текст новой заметки:\n--> ")
                    self.__notes[index].set_body(body)
                edit_choice = self.__edit_menu(index)
            self.__notes[index].set_update(datetime.datetime.now())

    def __edit_menu(self, index):
        '''
        Returns user choice edit note
        '''
        print("[ ] id: {0}".format(self.__notes[index].get_id()))
        print("[1] title: {}".format(self.__notes[index].get_title()))
        print("[2] body: {}".format(self.__notes[index].get_body()))
        return self.__int_input("[0] Выход в главное меню\n--> ")

    def __main_menu(self):
        '''
        Returns user chois from main menu
        '''
        #print('\n')
        print('Количество записей: {0}'.format(len(self.__notes)))
        if self.__sort_order == 0:
            print('Порядок сортировки: В порядке добавления')
        elif self.__sort_order == 1:
                print('Порядок сортировки: По дате последнего изменения')
        print(self.__SEPARATOR)
        return self.__int_input('[0] Выход            [1] Показать все        [2] Запись в файл\n' + 
                     '[3] Чтение из файла  [4] Редактировать       [5] Удалить\n' + 
                     '[6] Добавить заметку [7] Порядок сортировки  [8] Загрузить демо\n{0}\n--> '.format(self.__SEPARATOR))
    
    def __change_sort_order(self):
        '''
        Sets sort_order
        '''
        sort_choice = self.__int_input('Выберите порядок сортировки:\n[0] В порядке добавления\n' +
        '[1] По дате последнего изменения\n-->')
        self.__sort_order = sort_choice

'''
main
'''
admin = NotesAdministrator()
admin.run_admin()
