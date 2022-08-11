import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import uuid


root = Tk()
root.title('Scoolbook')

class Students:
    def __init__(self):
        self.students_window = Toplevel()
        self.students_window.title('Список школьников')

        self.students_buttons_frm = Frame(self.students_window)
        self.students_buttons_frm.grid(row=0, column=1, sticky=N)

        add_student = Button(self.students_buttons_frm, text=f'Добавить\nшкольника', width=8, 
                                command=lambda: self.add_student_click())
        add_student.grid(row=0, column=0, sticky=N)

        delete_student = Button(self.students_buttons_frm, text=f'Удалить\nшкольника', width=8, 
                                command=lambda: delete_contact(self.students_tree, self.students_tree_columns, self.student_path, 'student_id'))
        delete_student.grid(row=1, column=0, sticky=N)

        self.student_path = '/Users/nikolaishpagin/Desktop/GeekBrains/Programmer_1st_quarter/Python/Seminar_8/SchoolBook_tkinter/students.json'
        self.class_path = '/Users/nikolaishpagin/Desktop/GeekBrains/Programmer_1st_quarter/Python/Seminar_8/SchoolBook_tkinter/classes.json'

        # Students Table        
        self.students_tree_columns = ('student_id', 'Имя', 'Фамилия', 'Моб.', 'Email', 'Год рождения', 'Класс')
        self.students_tree = ttk.Treeview(self.students_window, columns=self.students_tree_columns, show='headings')
        for i in self.students_tree_columns:
            self.students_tree.heading(i, text=i, anchor='center')
            self.students_tree.column(i, width=100, anchor='center')
        self.students_tree.grid(row=0, column=0, sticky='nsew')
        self.students_tree['displaycolumns'] = ('Имя', 'Фамилия', 'Моб.', 'Email', 'Год рождения', 'Класс')
        

        refresh(self.students_tree, self.student_path, self.students_tree_columns)

    def add_student_click(self):
        self.add_student_window = Toplevel()
        self.add_student_window.title('Добавить школьника')

        self.perosonal_info_frm = Frame(self.add_student_window, name='personal', padx=5, pady=5, borderwidth=5)
        self.perosonal_info_frm.grid(row=0, column=0)

        self.student_name_lbl = Label(self.perosonal_info_frm, text='Имя', width=10, anchor=W)
        self.student_name_lbl.grid(row=0, column=0, sticky=N)
        self.student_name_entry = Entry(self.perosonal_info_frm, width=20, borderwidth=3)
        self.student_name_entry.grid(row=0, column=1)

        self.student_surname_lbl = Label(self.perosonal_info_frm, text='Фамилия', width=10, anchor=W)
        self.student_surname_lbl.grid(row=1, column=0, sticky=N)
        self.student_surname_entry = Entry(self.perosonal_info_frm, width=20, borderwidth=3)
        self.student_surname_entry.grid(row=1, column=1)

        self.student_mob_lbl = Label(self.perosonal_info_frm, text='Моб.', width=10, anchor=W)
        self.student_mob_lbl.grid(row=2, column=0, sticky=N)
        self.student_mob_entry = Entry(self.perosonal_info_frm, width=20, borderwidth=3)
        self.student_mob_entry.grid(row=2, column=1)

        self.student_email_lbl = Label(self.perosonal_info_frm, text='Email', width=10, anchor=W)
        self.student_email_lbl.grid(row=3, column=0, sticky=N)
        self.student_email_entry = Entry(self.perosonal_info_frm, width=20, borderwidth=3)
        self.student_email_entry.grid(row=3, column=1)

        self.student_birthyear_lbl = Label(self.perosonal_info_frm, text='Год рождения', width=10, anchor=W)
        self.student_birthyear_lbl.grid(row=4, column=0, sticky=N)
        self.student_birthyear_entry = Entry(self.perosonal_info_frm, width=20, borderwidth=3)
        self.student_birthyear_entry.grid(row=4, column=1)

        self.school_info_frm = Frame(self.add_student_window, name='school', padx=5, pady=5)
        self.school_info_frm.grid(row=1, column=0)

        self.student_class_lbl = Label(self.school_info_frm, text='Класс', width=10, anchor=W)
        self.student_class_lbl.grid(row=0, column=0, sticky=N)
        
        self.class_item = StringVar()
        class_list = get_information(self.class_path)
        items_list = list(i['Класс'] + ' ' + i['Буква'] for i in class_list)
        self.class_item.set(items_list[0])
        class_items_drop = OptionMenu(self.school_info_frm, self.class_item, *items_list)
        class_items_drop.grid(row=0, column=1, sticky=NSEW)

        # Save Button
        self.save_student_btn = Button(self.add_student_window, text='Добавить', command=lambda: self.save_student_btn_click(self.add_student_window), justify='center')
        self.save_student_btn.grid(row=2, column=0, columnspan=2, sticky=N)

    def save_student_btn_click(self, window):
        self.student_id = uuid.uuid4()
        new_contact = {
            'student_id': str(self.student_id),
            'Имя': self.student_name_entry.get(),
            'Фамилия': self.student_surname_entry.get(),
            'Моб.': self.student_mob_entry.get(),
            'Email': self.student_email_entry.get(),
            'Год рождения': self.student_birthyear_entry.get(),
            'Класс': self.class_item.get()
        }
        if (self.student_name_entry.get() == '' and self.student_surname_entry.get()) == '':
            self.popup_null_saved()
            self.repeat()
        else:
            students = get_information(self.student_path)
            with open(self.student_path, 'w') as file:
                students.append(new_contact)
                json.dump(students, file, indent=4, ensure_ascii=False)
            window.destroy()
            refresh(self.students_tree, self.student_path, self.students_tree_columns)
            self.popup_saved()

    def popup_null_saved(self):
        messagebox.showwarning(title='Ошибка', message='Не заполнено имя и/или фамилия ученика')

    def popup_saved(self):
        messagebox.showinfo(title='Новый учитель добавлен!', message='Новый ученик добавлен!')

class Teachers:
    def __init__(self):
        self.teachers_window = Toplevel()
        self.teachers_window.title('Список учителей')

        self.teachers_buttons_frm = Frame(self.teachers_window)
        self.teachers_buttons_frm.grid(row=0, column=1, sticky=N)

        add_teacher = Button(self.teachers_buttons_frm, text=f'Добавить\nучителя', width=8, 
                            command=lambda: self.add_teacher_click())
        add_teacher.grid(row=0, column=0, sticky=N)


        delete_student = Button(self.teachers_buttons_frm, text=f'Удалить\nучителя', width=8, 
                                command=lambda: delete_contact(self.teachers_tree, self.teachers_tree_columns, self.teachers_path, 'teacher_id'))
        delete_student.grid(row=1, column=0, sticky=N)

        self.teachers_path = '/Users/nikolaishpagin/Desktop/GeekBrains/Programmer_1st_quarter/Python/Seminar_8/SchoolBook_tkinter/teachers.json'
        self.class_path = '/Users/nikolaishpagin/Desktop/GeekBrains/Programmer_1st_quarter/Python/Seminar_8/SchoolBook_tkinter/classes.json'

        # Teachers Table
        self.teachers_tree_columns = ('teacher_id', 'Фамилия', 'Имя', 'Отчество', 'Моб.', 'Email', 'Год рождения', 'Предмет', 'Классный руководитель')
        self.teachers_tree = ttk.Treeview(self.teachers_window, columns=self.teachers_tree_columns, show='headings')
        for i in self.teachers_tree_columns:
            self.teachers_tree.heading(i, text=i, anchor='center')
            self.teachers_tree.column(i, width=100, anchor='center')
        self.teachers_tree.grid(row=0, column=0, sticky='nsew')
        self.teachers_tree['displaycolumns'] = ('Фамилия', 'Имя', 'Отчество', 'Моб.', 'Email', 'Год рождения', 'Предмет', 'Классный руководитель')

        refresh(self.teachers_tree, self.teachers_path, self.teachers_tree_columns)

    def add_teacher_click(self):
        self.add_teacher_window = Toplevel()
        self.add_teacher_window.title('Добавить учителя')

        self.perosonal_info_frm = Frame(self.add_teacher_window, name='personal', padx=5, pady=5, border=2, borderwidth=2)
        self.perosonal_info_frm.grid(row=0, column=0)

        self.teacher_surname_lbl = Label(self.perosonal_info_frm, text='Фамилия', width=10, anchor=W)
        self.teacher_surname_lbl.grid(row=0, column=0, sticky=N)
        self.teacher_surname_entry = Entry(self.perosonal_info_frm, width=20, borderwidth=3)
        self.teacher_surname_entry.grid(row=0, column=1)

        self.teacher_name_lbl = Label(self.perosonal_info_frm, text='Имя', width=10, anchor=W)
        self.teacher_name_lbl.grid(row=1, column=0, sticky=N)
        self.teacher_name_entry = Entry(self.perosonal_info_frm, width=20, borderwidth=3)
        self.teacher_name_entry.grid(row=1, column=1)

        self.teacher_midname_lbl = Label(self.perosonal_info_frm, text='Отчество', width=10, anchor=W)
        self.teacher_midname_lbl.grid(row=2, column=0, sticky=N)
        self.teacher_midname_entry = Entry(self.perosonal_info_frm, width=20, borderwidth=3)
        self.teacher_midname_entry.grid(row=2, column=1)

        self.teacher_mob_lbl = Label(self.perosonal_info_frm, text='Моб.', width=10, anchor=W)
        self.teacher_mob_lbl.grid(row=3, column=0, sticky=N)
        self.teacher_mob_entry = Entry(self.perosonal_info_frm, width=20, borderwidth=3)
        self.teacher_mob_entry.grid(row=3, column=1)

        self.teacher_email_lbl = Label(self.perosonal_info_frm, text='Email', width=10, anchor=W)
        self.teacher_email_lbl.grid(row=4, column=0, sticky=N)
        self.teacher_email_entry = Entry(self.perosonal_info_frm, width=20, borderwidth=3)
        self.teacher_email_entry.grid(row=4, column=1)

        self.teacher_birthyear_lbl = Label(self.perosonal_info_frm, text='Год рождения', width=10, anchor=W)
        self.teacher_birthyear_lbl.grid(row=5, column=0, sticky=N)
        self.teacher_birthyear_entry = Entry(self.perosonal_info_frm, width=20, borderwidth=3)
        self.teacher_birthyear_entry.grid(row=5, column=1)

        self.school_info_frm = Frame(self.add_teacher_window, name='professional', padx=5, pady=5)
        self.school_info_frm.grid(row=1, column=0)

        self.teacher_subject_lbl = Label(self.school_info_frm, text='Предмет', width=10, anchor=W)
        self.teacher_subject_lbl.grid(row=0, column=0, sticky=N)
        self.teacher_subject_entry = Entry(self.school_info_frm, width=20, borderwidth=3)
        self.teacher_subject_entry.grid(row=0, column=1)

        # Save Button
        self.save_teacher_btn = Button(self.add_teacher_window, text='Добавить', command=lambda: self.save_teacher_btn_click(self.add_teacher_window), justify='center')
        self.save_teacher_btn.grid(row=5, column=0, columnspan=2, sticky=N)

    def save_teacher_btn_click(self, window):
        teachers = get_information(self.teachers_path)
        self.teacher_id = uuid.uuid4()
        new_contact = {
            'teacher_id': str(self.teacher_id),
            'Имя': self.teacher_name_entry.get(),
            'Фамилия': self.teacher_surname_entry.get(),
            'Отчество': self.teacher_midname_entry.get(),
            'Моб.': self.teacher_mob_entry.get(),
            'Email': self.teacher_email_entry.get(),
            'Год рождения': self.teacher_birthyear_entry.get(),
            'Предмет': self.teacher_subject_entry.get(),
            'Классный руководитель': []
        }
        if (self.teacher_name_entry.get() == '' and self.teacher_surname_entry.get()) == '' and self.teacher_midname_entry.get() == '':
            Teachers.popup_null_saved()
            # self.repeat()
        else:
            teachers = get_information(self.teachers_path)
            with open(self.teachers_path, 'w') as file:
                teachers.append(new_contact)
                json.dump(teachers, file, indent=4, ensure_ascii=False)
            window.destroy()
            refresh(self.teachers_tree, self.teachers_path, self.teachers_tree_columns)
            Teachers.popup_saved()

    def popup_null_saved():
        messagebox.showwarning(title='Ошибка', message='Не заполнено имя или фамилия учителя')

    def popup_saved():
        messagebox.showinfo(title='Новый учитель добавлен!', message='Новый учитель добавлен!')

class Classes:
    def __init__(self):
        self.classes_window = Toplevel()
        self.classes_window.title('Список классов')

        self.class_buttons_frm = Frame(self.classes_window)
        self.class_buttons_frm.grid(row=0, column=1, sticky=N)

        add_class = Button(self.class_buttons_frm, text='Добавить класс', width=8, command=self.add_class_click)
        add_class.grid(row=0, column=0, sticky=N)

        delete_class = Button(self.class_buttons_frm, text='Удалить класс', width=8, 
                                command=lambda: delete_contact(self.classes_tree, self.classes_tree_columns, self.class_path, 'class_id'))
        delete_class.grid(row=1, column=0, sticky=N)

        self.class_path = '/Users/nikolaishpagin/Desktop/GeekBrains/Programmer_1st_quarter/Python/Seminar_8/SchoolBook_tkinter/classes.json'
        self.teachers_path = '/Users/nikolaishpagin/Desktop/GeekBrains/Programmer_1st_quarter/Python/Seminar_8/SchoolBook_tkinter/teachers.json'

        # Classes Table
        self.classes_tree_columns = ('class_id', 'Класс', 'Буква', 'Специальность', 'Классный руководитель')
        self.classes_tree = ttk.Treeview(self.classes_window, columns=self.classes_tree_columns, show='headings')
        for i in self.classes_tree_columns:
            self.classes_tree.heading(i, text=i, anchor='center')
            self.classes_tree.column(i, width=100, anchor='center')
        self.classes_tree.grid(row=0, column=0, sticky='nsew')
        self.classes_tree['displaycolumns'] = ('Класс', 'Буква', 'Специальность', 'Классный руководитель')

        refresh(self.classes_tree, self.class_path, self.classes_tree_columns)

    def add_class_click(self):
        self.add_class_window = Toplevel(self.classes_window)
        self.add_class_window.title('Добавить класс')

        self.class_lbl = Label(self.add_class_window, text='Класс')
        self.class_lbl.grid(row=0, column=0, sticky=W)
        self.class_name_entry = Entry(self.add_class_window, width=20, borderwidth=3)
        self.class_name_entry.grid(row=0, column=1)

        self.letter_lbl = Label(self.add_class_window, text='Буква')
        self.letter_lbl.grid(row=1, column=0, sticky=W)
        self.letter_entry = Entry(self.add_class_window, width=20, borderwidth=3)
        self.letter_entry.grid(row=1, column=1)

        self.spec_lbl = Label(self.add_class_window, text='Специальность')
        self.spec_lbl.grid(row=2, column=0, sticky=W)
        self.spec_entry = Entry(self.add_class_window, width=20, borderwidth=3)
        self.spec_entry.grid(row=2, column=1)

        self.spec_lbl = Label(self.add_class_window, text='Классный руководитель')
        self.spec_lbl.grid(row=3, column=0, sticky=W)

        self.teacher_item = StringVar()
        teachers_list = get_information(self.teachers_path)
        items_list = list(i['Фамилия'] + ' ' + i['Имя'] + ' ' + i['Отчество'] for i in teachers_list)
        self.teacher_item.set(items_list[0])
        search__items_drop = OptionMenu(self.add_class_window, self.teacher_item, *items_list)
        search__items_drop.grid(row=3, column=1, sticky=NSEW)

        # Save Button
        self.save_class_btn = Button(self.add_class_window, text='Добавить', command=lambda: self.save_class_btn_click(self.add_class_window), justify='center')
        self.save_class_btn.grid(row=4, column=0, columnspan=2, sticky=N)


    def save_class_btn_click(self, window):
        self.class_id = uuid.uuid4()
        new_contact = {
            'class_id': str(self.class_id),
            'Класс': self.class_name_entry.get(),
            'Буква': self.letter_entry.get(),
            'Специальность': self.spec_entry.get(),
            'Классный руководитель': self.teacher_item.get()
        }
        if any(new_contact) == False:
            Classes.popup_null_saved()
        else:
            classes = get_information(self.class_path)
            teachers = get_information(self.teachers_path)
            with open(self.class_path, 'w') as file:
                classes.append(new_contact)
                json.dump(classes, file, indent=4, ensure_ascii=False)
            refresh(self.classes_tree, self.class_path, self.classes_tree_columns)
            Classes.popup_saved()
        for teacher in teachers:
            if str(teacher['Фамилия'] + ' ' + teacher['Имя'] + ' ' + teacher['Отчество']) == self.teacher_item.get():
                teacher['Классный руководитель'].append([self.class_name_entry.get() + self.letter_entry.get()])
        with open(self.teachers_path, 'w') as file:
            json.dump(teachers, file, indent=4, ensure_ascii=False)
        window.destroy()

    def popup_null_saved():
        messagebox.showwarning(title='Ошибка', message='Не заполнены поля')

    def popup_saved():
        messagebox.showinfo(title='Новый учитель добавлен!', message='Новый класс добавлен!')


def get_information(path):
    with open(path, 'r') as file:
        contacts = json.load(file)
    return contacts

def delete_contact(tree, columns, path, id):
    my_item = tree.item(tree.focus())['values']
    contacts = list(get_information(path))
    for i in contacts:
        if str(i[id]) == str(my_item[0]):
            my_ind = contacts.index(i)
            break
    response = messagebox.askyesno(message=f"Вы уверены, что хотите удалить позицию?")
    if response == True:
        with open(path, 'w') as ph_book:
            del contacts[my_ind]
            json.dump(contacts, ph_book, indent=4, ensure_ascii=False)
        refresh(tree, path, columns)
        messagebox.showinfo(title='Удаление', message='Позиция удалена!')

def refresh(tree, path, columns):
    tree.delete(*tree.get_children())
    for contact in get_information(path):
        tree.insert('', END, values=(list(contact[i] for i in columns)))


show_students_btn = Button(root, text='Школьники', width=8, command=Students)
show_students_btn.grid(row=0, column=0)
show_teachers_btn = Button(root, text='Учителя', width=8, command=Teachers)
show_teachers_btn.grid(row=1, column=0)
show_classes_btn = Button(root, text='Классы', width=8, command=Classes)
show_classes_btn.grid(row=2, column=0)

root.mainloop()
