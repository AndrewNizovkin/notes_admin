
import datetime

class Note:
    '''
    This class encapsulates notes with id, title, body and date
    '''
    count_notes = 0
    def __init__(self, title, body):
        self.__title = title
        self.__body = body
        Note.count_notes += 1
        self.__id = Note.count_notes
        self.__update = datetime.datetime.now()
    
    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_body(self):
        return self.__body

    def set_title(self, title):
        self.__title = title
    
    def set_body(self, body):
        self.__body = body

        
    def print_note(self):
        print('id: {0:3} | update: {1} | title: {2:.15} | body: {3:.15}'.format(self.__id, self.__update.strftime("%y-%m-%d %H:%M:%S"), self.__title, self.__body))

class NotesAdministrator:
    '''
    This class provides methods for administering a collection of notes
    '''
    def __init__(self):
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
                print("Запись в файл")
            elif user_choice == 3:
                print("Чтение из файл")
            elif user_choice == 4:
                print("Редактировать заметку")
            elif user_choice == 5:
                index = int(input("Введите id заметки--> "))
                self.__remove_note(index)
            elif user_choice == 6:
                self.add_note()
            elif user_choice == 7:
                self.change_sort_order()
            elif user_choice == 8:
                self.load_demo()
            user_choice = self.main_menu()

    

    def load_demo(self):
        '''
        Loads test (Note) instances to self.notes
        '''
        self.notes.clear()
        for i in range(10):
            title = ('Заметка №{0}'.format(i))
            body = ('Тело заметки №{}'.format(i))
            note = Note(title, body)
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
            for x in self.notes:
                x.print_note()

    def save_file(self):
        '''
        Writes self.notes to ./notes.json

        '''
        pass

    def read_file(self):
        '''
        Read ./notes.json to self.notes
        '''
        pass

    def add_note(self):
        '''
        Adds (Note)note to self.notes
        '''
        title = input("Введите текст заголовка--> ")
        body = input("Введите текст заметки--> ")
        note = Note(title, body)
        self.notes.append(note)

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
        

    def main_menu(self):
        '''
        Returns user chois
        '''
        print("-"*62) 
        print('Количество записей: {0}'.format(len(self.notes)))
        if self.sort_order == 0:
            print('Порядок сортировки: В порядке добавления')
        elif self.sort_order == 1:
                print('Порядок сортировки: По дате последнего изменения')
        print("-"*62)
        return int(input('[0] Выход            [1] Показать все        [2] Запись в файл\n' + 
                     '[3] Чтение из файла  [4] Редактировать       [5] Удалить\n' + 
                     '[6] Добавить заметку [7] Порядок сортировки  [8] Загрузить демо\n--> '))
    
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