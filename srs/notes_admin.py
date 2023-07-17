
class Note:
    '''
    This class encapsulates notes with id, title, body and date
    '''
    count_notes = 0
    def __init__(self, title, body):
        self.title = title
        self.body = body
        Note.count_notes += 1
        self.id = Note.count_notes
    
    def print_notes(self):
        print('id= {0} title= {1} body= {2}'.format(self.id, self.title, self.body))

class NotesAdministrator:
    '''
    This class provides methods for administering a collection of notes
    '''
    def __init__():
        self.notes = list()
        
    def run_admin():
        '''
        Manages the list of notes
        '''
        pass

    def save_file():
        '''
        Writes self.notes to ./notes.json

        '''
        pass

    def read_file():
        '''
        Read ./notes.json to self.notes
        '''
        pass

    def add_note(note):
        '''
        Adds (Note)note to self.notes
        '''
        pass

    def get_note(index):
        '''
        Return (Note) from self.notes[index]
        '''
        pass


    def main_menu():
        '''
        Returns user chois
        '''
        return 0


#-------------------------------------------------------------
for i in range(10):
    title = ('title{0}'.format(i))
    new_note = Note(title, "test text")
    new_note.print_notes()

# notes1 = Note("Первая запись", "Привет Мир!")
# notes2 = Note("Вторая запись", "Привет Мываыаир!")
# notes1.print_notes()
# notes2.print_notes()
# print(notes1.get_title())