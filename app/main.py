
import time
from blessed import Terminal
#INSTANCIA PARA PODER TRABAJAR CON BLESSED
t= Terminal() 
class Task:
    def __init__(self, todos):
        self.todos= todos
        
    def input_todo(self):
        """
        METHOD:
            PASA LA ENTRADA DEL INPUT AL ARRAY
        """
        create_task= input('Add a task to do: ')
        return create_task
        #self.todos.append(create_task)
        #return self.todos
    
    def remove_task(self): #NO FUNCIONA CORRECTAMENTE
        """
        -ADD AT THE V1.1
        remote a task method
        """
        #time.sleep(5)
        """
        funciona, prodria agregar un inp
        -para eliminar un index en especifico
        """
        if not self.todos: # comprueba si no hay task antes de borrar
            print('no hay por borrar')
            return self.todos
        
        #print('Removing a task....')
        #time.sleep(1)
        removed_task= self.todos.pop()
        #print(t.clear_eol, end=" ")
        #print(f'item removed {removed_task}')
        #return self.todos
        #return removed_task
    
    def view(self):
        """
        add view
        """
        bg= f'{t.home}{t.on_maroon2}{t.clear}'
        bn= t.black_on_orchid1(t.center(t.bold("Add a taks or write ':q' to exit ")))
        return bg + bn
    
    def corrector_bg(self):
        """
        -Corrige el error del input y rellena el background
        """
        func_c= f'{t.on_maroon2}'
        return func_c


def main():
    todos= []
    # SE CREA LA VENTANA CON EL FONDO Y SE LIMPIA Y AGREGA EL BANNER
    print(f'{t.home}{t.on_maroon2}{t.clear}')
    print(t.black_on_orchid1(t.center(t.bold("Add a taks or write ':q' to exit"))))
    """
    -v1.0 IS WORKING (CREATE TASK AND BREAK THE LOOP)
    -V1.1 UNDEFINED (ADD RM METHOD, ADD INSERT METHOD, ?)
    -V1.2 IS WORKING (FASTAPI, SQLITE, STREAMLIT)
    
    """
    # CREA EL LOOP PARA LA CONDICIONAL DEL INPUT, Y PARA SALIR DE EL
    #with t.cbreak():
    while True:
            
            # CORRIGE EL ERROR Y LLENA EL FONDO
            print(f'{t.on_maroon2}')
            add_todo= (input('Add a todo: '))

            # CONDICIONAL PARA SALIR
            if add_todo.lower() == ':q':
                break
            else:
                # CONDICION PARA CREAR LA LISTA
                #todos.append(f'{t.underline(add_todo.capitalize())}')
                todos.append(f'{t.underline(add_todo.capitalize())}')
                # CLEAN THE WIEW
                print(f'{t.on_maroon2}{t.home}{t.clear}')
                # RETURN THE MAIN MASSAGE Y SE FIJA
                print(t.on_orchid1(t.center(t.bold("Add a task or write ':q' to exit"))))
                # CLEAN THE WIEW y CORRIGE EL ERROR DEL FONDO
                print(f'{t.on_maroon2}')
                for i, todo in enumerate(todos, start=1):
                    print(f'{i}. {todo}')

    print(t.underline('Exit.'))
    print(t.clear)

def test():
    #print(t.clear)
    print(f'{t.home}{t.on_mediumorchid1}{t.clear}')
    print(t.black_on_red(t.center("write some text(or write 'q' to stop")))
    with t.cbreak():
         while True:
            val= t.inkey()
            print(f'You press: {val}')
            if val == 'q':
                print(t.clear)
                break
            else:
                print('are u sure to follow?')

def clases():
    todos= []
    version_v1= Task(todos)
    banner= version_v1.view()
    """
    -INIT BANNER
    """
    print(banner)
      
    """
    -INIT CONDITIONAL
    """
    while True:
        fill_bg= version_v1.corrector_bg()
        print(fill_bg)
        #test_inp= input('-Add a task to do: ')
        ip= version_v1.input_todo()
        # ADD CONDITIONAL TO BREAK THE  LOOP
        #if test_inp == ':q':
        if ip.lower() == ':q':
            break
        #elif ip.lower() == ':rm':
        #    rmove= version_v1.remove_task() >>>>>>  ARREGLAR PARA LA V1.1 RM METHOD
        #    print(t.clear, t.normal)

            #-ADD CONDITIONAL TO START THE INPUT TO MAKE TASK
        else:
            #todos.append(f'{test_inp.capitalize()}')
            todos.append(f'{t.on_maroon2}{t.underline(ip.capitalize())}{t.on_maroon2}')
            
            print(banner)
            print(fill_bg)
            for i, todo in enumerate(todos, start=1):
                print(f'{i}. {todo}')
    print("  ")
    print('Exit...')
    print("  ")
    #time.sleep(5)
    #print(f'{t.normal} + {t.clear}')

    
if __name__=='__main__':
    #main()
    #test()
    clases()

# EXAMPLES >>>>>>>>>>
#print(t.bold('Test')) # bold text
#print(t.bold_red_on_bright_green('test')) # background green
#with t.cbreak():
#        inp= t.inkey() # CAPTURA EL INPUT SI DAR ENTER
#        print(f'input test: {inp}')    

