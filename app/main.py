
import time
from blessed import Terminal
import datetime

""" 
- INSTANCIA PARA PODER TRABAJAR CON BLESSED

"""
t= Terminal()
date_time= datetime.datetime.now()
txtn = t.color_rgb(0, 0, 0)

class Task:
    def __init__(self, todos):
        self.todos= todos
        #self.is_unlocked = False



    def pink_theme(self):
        """
        Creadmos el background y el banner 
        """
        bg= f'{t.home}{txtn}{t.on_maroon2}{t.clear}' # you can change the theme in this line
        bn= t.black_on_orchid1(t.center(t.bold("Add a note or write 'q' to exit ")))
        return bg + bn


    def dark_theme(self): #FUNCIONA
        """
        Creadmos el background y el banner 
        """
        bg= f'{t.home}{txtn}{t.on_color_rgb(000, 000,000)}{t.clear}'
        bn= t.on_color_rgb(79, 124, 130)(t.center(t.bold("Write 'i' to insert a note or 'q' to exit"))) # CODIGO PRUEBa
        return bg + bn
    
    def normal_theme(self): #FUNCIONA;
        bg= f'{t.home}{txtn}{t.on_color_rgb(242, 242, 242)}{t.clear}' 
        bn= t.on_color_rgb(204, 204, 255) + (t.center(t.bold("Add a note or write 'q' to exit "))) 
        return bg + bn 
        
    
    def fill_bg(self):
        """
        -Rellena el background tras agregar una task
        """
        while True:
             with t.cbreak():
                inp = t.inkey()
                if inp == '1':
                    return f'{txtn}{t.on_color_rgb(242, 242, 242)}'
                if inp == '2':
                    return f'{t.on_maroon2}'
                elif inp == '3':
                    return t.on_color_rgb(000, 000,000)
                else:
                    print('')
                    print(f'{t.yellow}{t.bold('You pressed an invalid key: ')}{t.bold(repr(inp))}')
                    print(f'{t.yellow}{t.bold('Try with a valid key again')}')
 

    def input_todo(self):
        """
        METHOD:
            PASA LA ENTRADA DEL INPUT AL ARRAY
        """
        create_task= input(f'Add a note: {t.springgreen('>_ ')}')
        return create_task
    


    def intro(self):
        """
        Menu de inicio
        """
        print(f'{t.home}{txtn}{t.on_color_rgb(0, 0, 0)}{t.clear}')
        print(f'{t.home} + {t.clear} + {t.move_y(t.height // 2)})')

        print(f'{t.on_color_rgb(128, 239, 128)}{t.center('Press "KEY_ENTER" to start ')}')
  

    def display_menu(self): 

        while True:
            with t.cbreak(), t.hidden_cursor():
                inp = t.inkey()
        
                if inp.name == 'KEY_ENTER':
                    return 
                else:
                    print( '  ')
                    print(f'{t.yellow}{t.bold('You pressed an invalid key: ')}{t.bold(repr(inp))}')
                    print(f'{t.yellow}{t.bold('Please press a valid key [ ENTER ]')}')
                    continue  # Reinicia el ciclo para pedir una tecla válida

            
    def select_theme(self): 
        """
        Method to set the color theme
        """
        print(f'{t.home}{txtn}{t.on_color_rgb(0, 0, 0)}{t.clear}')
        print(f'{t.on_color_rgb(128, 239, 128)}{t.center('Press 1 [Normal Mode] ,2 [Pink Mode] or 3 [Dark Mode]')}')
        
        while True:
            with t.cbreak(), t.hidden_cursor():
                inp = t.inkey()
                print(f'DEBUG: {repr(inp)}')

                #time.sleep(2)
                if inp == '1':
                    return self.normal_theme()
                if inp == '2':
                    return self.pink_theme()
                elif inp == '3':
                    return self.dark_theme()
                else:
                    print(  '')
                    print(f'{t.yellow}{t.bold('You pressed an invalid key: ')}{t.bold(repr(inp))}')
                    print(f'{t.yellow}{t.bold('Try with a valid key again')}')
                continue

  
    def manager(self, is_unlocked, notes):
        """
        docstring
        """
        
        theme= self.select_theme()
        bg= self.fill_bg()

        print(theme)
        while True:
            print(bg)
            inp= self.input_todo()
            if inp.lower() == 'q':
                break
            elif inp.lower() == 'i':
                is_unlocked= True
            elif is_unlocked:
                notes.append(inp.capitalize())
                print(theme)
                print(bg)
                for i, note in enumerate(notes, start=1):
                    print(f'{i}. {note}')
            else:
                print(f'{bg}{t.bold('You pressed an invalid key: ')}{bg}{t.bold(repr(inp))}') # FIXED  
                print(f'{bg}{t.bold('Try with a valid key again')}')
        time.sleep(0.1)
        print(bg)
        print(bg)
        print(f'{bg}Session ended...')
        print(bg)
        #print(f'{t.normal} + {t.clear}') # Use this to clear all !
                
        

    def init_app(self, is_unlocked,notes):
        """
    Inicia todos los métodos necesarios para la ejecución de la aplicación.
    
    Parámetros:
        - is_unlocked (bool): Estado de desbloqueo.
        - notes (list): Lista de notas que se manejarán en el proceso.
        """
        
        self.intro()
        self.display_menu()
        self.select_theme()
        self.fill_bg()
        self.manager(is_unlocked, notes)

    
def run():
    
    is_unlocked= False
    todos= []
    version_v1= Task(todos)
    version_v1.init_app(is_unlocked, todos)
    
 


if __name__=='__main__':
    #test()
    run()

