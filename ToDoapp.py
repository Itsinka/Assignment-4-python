import tkinter as tk
from tkinter import filedialog

def create_task():
    task_title = task_entry.get()
    task_deadline = deadline_entry.get() #Функция для создания новой задачи. Она извлекает текст из виджетов ввода task_entry (название задачи) и deadline_entry (дедлайн), проверяет, что оба поля не пусты, и затем добавляет новую задачу в виджет списка task_list
    if task_title and task_deadline:
        task_list.insert(tk.END, f"{task_title} (Deadline: {task_deadline})")
        task_entry.delete(0, tk.END)
        deadline_entry.delete(0, tk.END)

def open_task():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            task_text = file.read()
            task_list.insert(tk.END, task_text)

def save_task():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            tasks = task_list.get(0, tk.END)
            for task in tasks:
                file.write(task + "\n")

app = tk.Tk()
app.title("To-Do App with Deadlines") #Создание основного окна приложения

# Создание меню
menu = tk.Menu(app)
app.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New Task", command=create_task)
file_menu.add_command(label="Open Task", command=open_task)
file_menu.add_command(label="Save Tasks", command=save_task)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=app.quit)

# Создание виджетов для ввода задач и дедлайнов
task_entry_label = tk.Label(app, text="Task Title:")
task_entry_label.pack()
task_entry = tk.Entry(app)
task_entry.pack()

deadline_entry_label = tk.Label(app, text="Deadline:")
deadline_entry_label.pack()
deadline_entry = tk.Entry(app)
deadline_entry.pack()

# Создание списка (Listbox) для отображения задач
task_list = tk.Listbox(app)
task_list.pack()

app.mainloop()

