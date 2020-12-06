from os import system

class List():

    def __init__(self):
        self.list = []
        tasks = open('/Users/Mamo/python/todolist/reminders.txt', 'r')
        for line in tasks:
            self.list.append(line.strip())
        tasks.close()
        if self.list != []:
            print('Unfinished tasks:')
            for i in range(len(self.list)):
                print(f'{i + 1}: {self.list[i]}')
        self.UI()

    def add(self):
        self.list.append(input('Your task: ')) 
        self.UI()

    def remove(self):
        for i in range(len(self.list)):
            print(f'{i + 1}: {self.list[i]}')
        index = input('Index: ')
        if 1 <= int(index) <= len(self.list) and self.list != []:
            self.list.pop(int(index) - 1)
        elif index.lower() in {'q', 'quit'}:
            exit()
        else:
            print('Your input is not valid!')
            self.remove()
        self.UI()

    def UI(self):
        cmd = input('Command: ') 
        if cmd not in {'a', 'r', 'p', 'q', 'c'}:
            self.UI()
        elif cmd == 'a':
            self.add()
        elif cmd == 'r':
            self.remove()
        elif cmd == 'q':
            self.rewrite()
            exit()
        elif cmd == 'p':
            self.printCurrent()
        elif cmd == 'c':
            system('clear')
            self.rewrite()
            self.UI()
        self.rewrite()
    
    def printCurrent(self):
        print('Current tasks:')
        for i in range(len(self.list)):
            print(f'{i + 1}: {self.list[i]}')
        self.UI()

    def rewrite(self):
        new_tasks = open('/Users/Mamo/python/todolist/reminders.txt', 'w')
        for task in self.list:
            new_tasks.write(task + '\n')
        new_tasks.close()

todo = List()
