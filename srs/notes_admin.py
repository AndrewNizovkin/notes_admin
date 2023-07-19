
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
    
    def get_id(self):
        return self.__id

    def get_update(self):
        return self.__update

    def get_title(self):
        return self.__title

    def get_body(self):
        return self.__body

    def set_update(self, date):
        self.__update = date

    def set_title(self, title):
        self.__title = title
    
    def set_body(self, body):
        self.__body = body

        
    def print_note(self):
        print('id: {0:2}  update: {1}  title: {2}  body: {3}'.format(self.__id, self.__update.strftime("%y-%m-%d %H:%M:%S"), self.__title, self.__body))

class NotesAdministrator:
    '''
    This class provides methods for administering a collection of notes
    '''
    def __init__(self):
        self.__work_dir = os.getcwd()
        self.__file_notes = ("{0}\\notes.csv".format(self.__work_dir))
        self.notes = list()
        self.sort_order = 0
        
    def run_admin(self):
        '''
        Manages the list of notes
        '''
        user_choice = self.main_menu()
        while user_choice != 0:
            if user_choice == 1:
                self.print_all()
            elif user_choice == 2:
                self.__save_file()
            elif user_choice == 3:
                self.__read_file()
            elif user_choice == 4:
                index = int(input("Введите id заметки--> "))
                self.__edit_note(index)
            elif user_choice == 5:
                index = int(input("Введите id заметки--> "))
                self.__remove_note(index)
            elif user_choice == 6:
                self.add_note()
            elif user_choice == 7:
                self.change_sort_order()
            elif user_choice == 8:
                self.__load_demo()
            user_choice = self.main_menu()
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
        Loads test (Note) instances to self.notes
        '''
        self.notes.clear()
        for i in range(0, 10):
            id = self.__get_new_id()
            title = ('Заметка №{0}'.format(i))
            body = ('Тело заметки №{}'.format(i))
            note = Note(id, title, body)
            self.notes.append(note)

    def __remove_note(self, id):
        '''
        Removes self.notes[id]
        '''
        index = self.__get_index(id)
        if index == -1:
            print("Записи с таким id нет в списке")
        else:
            print("Удалена заметка:")
            self.notes.pop(index).print_note()

    def print_all(self):

        '''
        Prints to console all notes from self.notes with self.sort_order
        '''

        if self.sort_order == 0:
            self.notes.sort(key=self.__sort_by_id)
        elif self.sort_order == 1:
            self.notes.sort(key=self.__sort_by_update)
        for x in self.notes:
            x.print_note()

    def __sort_by_id(self, note):
        return note.get_id()

    def __sort_by_update(self, note):
        return note.get_update()

    def __save_file(self):

        '''
        Writes self.notes to ./notes.csv

        '''

        file_notes = open(self.__file_notes, 'w', encoding='utf-8')
        for note in self.notes:
            file_notes.write('{0};{1};{2};{3}\n'.format(note.get_id(), note.get_update(), note.get_title(), note.get_body()))
            
        file_notes.close()
        print("Запись в файл:\n{0}".format(self.__file_notes))

        
    def __read_file(self):

        '''
        Read ./notes.json to self.notes
        '''
        if os.path.exists(self.__file_notes):
            self.notes.clear()
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
                self.notes.append(note)
                line = file_notes.readline().rstrip()
            file_notes.close()
        else:
            print("Файл {0} не существует".format(self.__file_notes))

    def add_note(self):

        '''
        Adds (Note)note to self.notes
        '''

        id = self.__get_new_id()
        title = input("Введите текст заголовка--> ")
        body = input("Введите текст заметки--> ")
        note = Note(id, title, body)
        self.notes.append(note)

    def __get_new_id(self):

        '''
        Gets new unique id for self.notes
        '''
        if len(self.notes) > 0:
            #list_id = [x.get_id() for x in self.notes]
            return max([x.get_id() for x in self.notes]) +1
        return 1

    def __get_index(self, id):

        '''
        Return index with self.notes[index] == id
        '''

        index = -1
        if len(self.notes) > 0:
            for i in range(len(self.notes)):
                if (self.notes[i].get_id() == id):
                    index = i
                    #break
        return index

    def __edit_note(self, id):

        '''
        Changes self.notes.get__id == id

        '''
        index = self.__get_index(id)
        if index == -1:
            print("Записи с таким id нет в списке")
        else:
            edit_choice = self.__edit_menu(index)
            while edit_choice != 0:
                if edit_choice == 1:
                    title = input("Введите новый заголовок:\n--> ")
                    self.notes[index].set_title(title)
                elif edit_choice == 2:
                    body = input("Введите текст новой заметки:\n--> ")
                    self.notes[index].set_body(body)
                edit_choice = self.__edit_menu(index)
            self.notes[index].set_update(datetime.datetime.now())

    def __edit_menu(self, index):

        '''
        Returns user choice edit note

        '''

        print("[ ] id: {0}".format(self.notes[index].get_id()))
        print("[ ] update: {}".format(self.notes[index].get_update()))
        print("[1] title: {}".format(self.notes[index].get_title()))
        print("[2] body: {}".format(self.notes[index].get_body()))
        return int(input("[0] Выход в главное меню\n--> "))

    def main_menu(self):

        '''
        Returns user chois
        '''
        print('\n')
        print("-"*62) 
        print('Количество записей: {0}'.format(len(self.notes)))
        if self.sort_order == 0:
            print('Порядок сортировки: В порядке добавления')
        elif self.sort_order == 1:
                print('Порядок сортировки: По дате последнего изменения')
        print("-"*62)
        return self.__int_input('[0] Выход            [1] Показать все        [2] Запись в файл\n' + 
                     '[3] Чтение из файла  [4] Редактировать       [5] Удалить\n' + 
                     '[6] Добавить заметку [7] Порядок сортировки  [8] Загрузить демо\n--> ')
    
    def change_sort_order(self):

        '''
        Sets sort_order
        '''
        
        sort_choice = int(input('Выберите порядок сортировки:\n[0] В порядке добавления\n' +
        '[1] По дате последнего изменения\n-->'))
        self.sort_order = sort_choice



#-------------------------------------------------------------
admin = NotesAdministrator()
admin.run_admin()
# for i in range(10):
#     title = ('title{0}'.format(i))
#     new_note = Note(title, "test text")
#     new_note.print_notes()

# notes1 = Note("Первая запись", "Привет Мир!")
# notes2 = Note("Вторая запись", "Привет Мываыаир!")
# notes1.print_notes()
# notes2.print_notes()mount /dev/nvme0n1p5 /mntchroot /mnt /bin/bash
# print(notes1.get_title())sudo mount --bind /dev /mnt/dev