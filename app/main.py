
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
        create_task= input('add a taesk to do: ')
        self.todos.append(create_task)
        return self.todos
    

    def remove_task(self):
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
        
        print('Removing a task....')
        time.sleep(3)
        removed_task= self.todos.pop()
        print(f'item removed {removed_task}')
        return self.todos


    def view(self):
        """
        add view
        """
        bg= f'{t.home}{t.on_maroon2}{t.clear}'
        ms= t.black_on_orchid1(t.center(t.bold("Add a taks or write ':q' to exit")))
        return bg + ms
    


def main():
    todos= []
    print(f'{t.home}{t.on_maroon2}{t.clear}')
    print(t.black_on_orchid1(t.center(t.bold("Add a taks or write ':q' to exit"))))
    """
    -v1.0 IS WORKING (CREATE TASK AND BREAK THE LOOP)
    -V1.1 UNDEFINED (ADD RM METHOD, ADD INSERT METHOD, ?)
    -V1.2 IS WORKING (FASTAPI, SQLITE, STREAMLIT)
    
    """

    #with t.cbreak():
    while True:
            # CORRIGE EL ERROR Y LLENA EL FONDO
            print(f'{t.on_maroon2}')
            add_todo= input('Add a todo: ')

            # CONDICIONAL PARA SALIR
            if add_todo.lower() == ':q':
                break
            else:
                # CONDICION PARA CREAR LA LISTA
                todos.append(f'{add_todo.capitalize()}')
                # CLEAN THE WIEW
                print(f'{t.on_maroon2}{t.home}{t.clear}')
                # RETURN THE MAIN MASSAGE Y SE FIJA
                print(t.on_orchid1(t.center(t.bold("Add a task or write ':q' to exit"))))
                # CLEAN THE WIEW y CORRIGE EL ERROR DEL FONDO
                print(f'{t.on_maroon2}')
                for i, todo in enumerate(todos, start=1):
                    print(f'{i}. {todo}')

    print('Exit.')
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


def example_class():

    # VARIABLE A PASAR    
    todos= []

    # INSTANCIA DE LA CLASS
    exam= Task(todos)
    cleaner= exam.view()
    text_input= exam.input_todo()
    #rm= exam.remove_task()
    print(cleaner)
    print(text_input)

    while True:
        print(f'{t.on_maroon2}')
        add_todo= input('Add a todo: ')

        if add_todo.lower() == ':q':
            break
        else:
            todos.append(f'{add_todo.capitalize()}')
            #todos.append(f'{add_todo.capitalize()}')
            # CLEAN THE WIEW
            print(f'{t.on_maroon2}{t.home}{t.clear}')
            print(t.on_orchid1(t.center(t.bold("Add a task or write ':q' to exit"))))

            # RETURN THE MAIN MASSAGE
            print(f'{t.on_maroon2}')
            for i, todo in enumerate(todos, start=1):
                print(f'{i}. {todo}')

def clases():
    todos= []
    version_v1= Task(todos)
    banner= version_v1.view()
    print(banner)
    #print(np_test)

    


    
    
if __name__=='__main__':
    main()
    #test()
    #example_class()
    #clases()

#def examples():C
    """
    EXAMPLES
    """
#print(t.bold('Test')) # bold text
#print(t.bold_red_on_bright_green('test')) # background green
#with t.cbreak():
#        inp= t.inkey() # CAPTURA EL INPUT SI DAR ENTER
#        print(f'input test: {inp}')    
#examples()
