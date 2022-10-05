from tkinter import *
from tkinter import messagebox
def newTask():
    task = my_entry.get()
    if task !="":
        lb.insert(END,task)
        my_entry.delete(0,"end")
    else:
        messagebox.showwarning("warning", "Пожалуйста, введите задачу")

#Удаление задачи
def deleteTask():
    lb.delete(ANCHOR)
#Создадим окно
wc = Tk()
wc.geometry('500x450+500+200')
wc.title("Список задач")
wc.config(bg="#223441")
wc.resizable(width=False, height=False)
#Создание рамки
frame = Frame(wc)
frame.pack(pady=10)
#Добавление списка
lb = Listbox(frame, width=25, height=8, font=("Times",18), bd=0, fg= "#464646",
             highlightthickness=0, selectbackground="#a6a6a6", activestyle="none")
lb.pack(side=LEFT, fill=BOTH)
#Добавление фиктивных данных
task_list = ['Eat apple',
    'drink water',
    'go gym',
    'write software',
    'write documentation',
    'take a nap',
    'Learn something',
    'paint canvas']
for item in task_list:
    lb.insert(END, item)
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)
#Назначение полосы прокрутки
lb.config(yscrollcommand=sb.set)
#Полоска двигается в вертикальном направлении
sb.config(command=lb.yview)
#Добавление окна ввода
my_entry = Entry(wc, font=('times', 24))
my_entry.pack(pady=20)
#Добавляем рамку для кнопок
button_frame = Frame(wc)
button_frame.pack(pady=20)
#Добавление кнопок
add_Task_btn = Button(button_frame, text="Добавить задачу",font=('times 14'),
                      bg="#c5f776", padx=10, pady=10, command=newTask)
add_Task_btn.pack(fill=BOTH, expand=True, side=LEFT)
del_Task_btn = Button(button_frame, text="Удалить задачу", font=('times 14'),
                      bg='#ff8b61',padx=20,pady=10,command=deleteTask)
del_Task_btn.pack(fill=BOTH, expand=True, side=LEFT)
#Добавление задачи
#Обновление окна
wc.mainloop()