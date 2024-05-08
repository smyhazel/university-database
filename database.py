import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
import sqlite3

class UniversityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("University Database")
        self.root.geometry("400x300")  # Arayüz boyutu
        self.root.configure(bg="#f0f0f0")  # Arayüz arka plan rengi

        # Logoyu eklemek için bir resim dosyası kullanın
        logo_image = PhotoImage(file=r"C:\Users\90553\OneDrive\Resimler\logo.png")  # Logo dosyasının gerçek yoluyla değiştirin

        # Logo görüntüsünü arayüze ekleyin
        logo_label = tk.Label(self.root, image=logo_image, bg="#f0f0f0")
        logo_label.photo = logo_image  # Referansı tutmak önemlidir
        logo_label.pack(pady=10)

        def list_teaches_data(self):
         print("Listing Teaches Data")

        # SQLite veritabanı bağlantısını oluştur
        self.connection = sqlite3.connect("university.db")  # Veritabanı adını güncelleyin

        # Cursor (imleç) oluştur
        self.cursor = self.connection.cursor()

        # Örnek bir sorgu: "teaches" tablosundaki tüm verileri al
        self.cursor.execute("SELECT * FROM teaches")
        rows = self.cursor.fetchall()

        # Verileri ekrana yazdır
        for row in rows:
            print(row)


        # Ana sayfa butonları
        self.create_main_buttons()

    def create_main_buttons(self):
        # Instructor Button
        instructor_button = tk.Button(self.root, text="Instructor", command=self.show_instructor_options, bg="#4CAF50", fg="white")
        instructor_button.place(x=150, y=100)  # Orta hizaya ayarladım

        # Student Button
        student_button = tk.Button(self.root, text="Student", command=self.show_student_options, bg="#2196F3", fg="white")
        student_button.place(x=150, y=140)  # Orta hizaya ayarladım

        # Course Button
        course_button = tk.Button(self.root, text="Course", command=self.show_course_options, bg="#FFC107", fg="white")
        course_button.place(x=150, y=180)  # Orta hizaya ayarladım

        # Teaches Button
        teaches_button = tk.Button(self.root, text="Teaches", command=self.show_teaches_options, bg="#9C27B0", fg="white")
        teaches_button.place(x=150, y=220)  # Orta hizaya ayarladım

    def show_teaches_options(self):
        # Yeni pencere oluştur
        teaches_window = tk.Toplevel(self.root)
        teaches_window.title("Teaches Options")

        # ID Label ve Entry
        id_label = tk.Label(teaches_window, text="ID:")
        id_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        id_entry = tk.Entry(teaches_window)
        id_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Course ID Label ve Entry
        course_id_label = tk.Label(teaches_window, text="Course ID:")
        course_id_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        course_id_entry = tk.Entry(teaches_window)
        course_id_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Semester Label ve Entry
        semester_label = tk.Label(teaches_window, text="Semester:")
        semester_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        semester_entry = tk.Entry(teaches_window)
        semester_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Year Label ve Entry
        year_label = tk.Label(teaches_window, text="Year:")
        year_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        year_entry = tk.Entry(teaches_window)
        year_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Insert Data Button
        insert_button = tk.Button(teaches_window, text="Insert Data", command=lambda: self.insert_teaches_data(id_entry.get(), course_id_entry.get(), semester_entry.get(), year_entry.get()))
        insert_button.grid(row=4, column=0, columnspan=2, pady=5)

        # Delete Data Button
        delete_button = tk.Button(teaches_window, text="Delete Data", command=lambda: self.delete_teaches_data(id_entry.get()))
        delete_button.grid(row=5, column=0, columnspan=2, pady=5)

        # Update Data Button
        update_button = tk.Button(teaches_window, text="Update Data", command=lambda: self.update_teaches_data(id_entry.get(), course_id_entry.get(), semester_entry.get(), year_entry.get()))
        update_button.grid(row=6, column=0, columnspan=2, pady=5)

        # List Data Button
        list_button = tk.Button(teaches_window, text="List Data", command=self.list_teaches_data)
        list_button.grid(row=7, column=0, columnspan=2, pady=5)


    def show_instructor_options(self):
        # Yeni pencere oluştur
        instructor_window = tk.Toplevel(self.root)
        instructor_window.title("Instructor Options")

        # Instructor ID Label ve Entry
        instructor_id_label = tk.Label(instructor_window, text="Instructor ID:")
        instructor_id_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        instructor_id_entry = tk.Entry(instructor_window)
        instructor_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Name Label ve Entry
        name_label = tk.Label(instructor_window, text="Name:")
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        name_entry = tk.Entry(instructor_window)
        name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Dept-name Label ve Entry
        dept_label = tk.Label(instructor_window, text="Dept-name:")
        dept_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        dept_entry = tk.Entry(instructor_window)
        dept_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Salary Label ve Entry
        salary_label = tk.Label(instructor_window, text="Salary:")
        salary_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        salary_entry = tk.Entry(instructor_window)
        salary_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Course ID Label ve Entry
        course_id_label = tk.Label(instructor_window, text="Course ID:")
        course_id_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        course_id_entry = tk.Entry(instructor_window)
        course_id_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # Insert Data Button
        insert_button = tk.Button(instructor_window, text="Insert Data", command=lambda: self.insert_instructor_data(instructor_id_entry.get(), name_entry.get(), dept_entry.get(), salary_entry.get(), course_id_entry.get()))
        insert_button.grid(row=5, column=0, columnspan=2, pady=5)

        # Delete Data Button
        delete_button = tk.Button(instructor_window, text="Delete Data", command=lambda: self.delete_instructor_data(instructor_id_entry.get()))
        delete_button.grid(row=6, column=0, columnspan=2, pady=5)

        # Update Data Button
        update_button = tk.Button(instructor_window, text="Update Data", command=lambda: self.update_instructor_data(instructor_id_entry.get(), name_entry.get(), dept_entry.get(), salary_entry.get(), course_id_entry.get()))
        update_button.grid(row=7, column=0, columnspan=2, pady=5)

        # List Data Button
        list_button = tk.Button(instructor_window, text="List Data", command=self.list_instructor_data)
        list_button.grid(row=8, column=0, columnspan=2, pady=5)

    def show_student_options(self):
        # Yeni pencere oluştur
        student_window = tk.Toplevel(self.root)
        student_window.title("Student Options")

        # ID Label ve Entry
        id_label = tk.Label(student_window, text="ID:")
        id_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        id_entry = tk.Entry(student_window)
        id_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Name Label ve Entry
        name_label = tk.Label(student_window, text="Name:")
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        name_entry = tk.Entry(student_window)
        name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Dept-name Label ve Entry
        dept_label = tk.Label(student_window, text="Dept-name:")
        dept_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        dept_entry = tk.Entry(student_window)
        dept_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Tot-cred Label ve Entry
        tot_cred_label = tk.Label(student_window, text="Tot-cred:")
        tot_cred_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        tot_cred_entry = tk.Entry(student_window)
        tot_cred_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Insert Data Button
        insert_button = tk.Button(student_window, text="Insert Data", command=lambda: self.insert_student_data(id_entry.get(), name_entry.get(), dept_entry.get(), tot_cred_entry.get()))
        insert_button.grid(row=4, column=0, columnspan=2, pady=5)

        # Delete Data Button
                # Delete Data Button
        delete_button = tk.Button(student_window, text="Delete Data", command=lambda: self.delete_student_data(id_entry.get()))
        delete_button.grid(row=5, column=0, columnspan=2, pady=5)

        # Update Data Button
        update_button = tk.Button(student_window, text="Update Data", command=lambda: self.update_student_data(id_entry.get(), name_entry.get(), dept_entry.get(), tot_cred_entry.get()))
        update_button.grid(row=6, column=0, columnspan=2, pady=5)

        # List Data Button
        list_button = tk.Button(student_window, text="List Data", command=self.list_student_data)
        list_button.grid(row=7, column=0, columnspan=2, pady=5)

    def show_course_options(self):
        # Yeni pencere oluştur
        course_window = tk.Toplevel(self.root)
        course_window.title("Course Options")

        # Course ID Label ve Entry
        course_id_label = tk.Label(course_window, text="Course ID:")
        course_id_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        course_id_entry = tk.Entry(course_window)
        course_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Title Label ve Entry
        title_label = tk.Label(course_window, text="Title:")
        title_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        title_entry = tk.Entry(course_window)
        title_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Dept-name Label ve Entry
        dept_label = tk.Label(course_window, text="Dept-name:")
        dept_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        dept_entry = tk.Entry(course_window)
        dept_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Credits Label ve Entry
        credits_label = tk.Label(course_window, text="Credits:")
        credits_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        credits_entry = tk.Entry(course_window)
        credits_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Insert Data Button
        insert_button = tk.Button(course_window, text="Insert Data", command=lambda: self.insert_course_data(course_id_entry.get(), title_entry.get(), dept_entry.get(), credits_entry.get()))
        insert_button.grid(row=4, column=0, columnspan=2, pady=5)

        # Delete Data Button
        delete_button = tk.Button(course_window, text="Delete Data", command=lambda: self.delete_course_data(course_id_entry.get()))
        delete_button.grid(row=5, column=0, columnspan=2, pady=5)

        # Update Data Button
        update_button = tk.Button(course_window, text="Update Data", command=lambda: self.update_course_data(course_id_entry.get(), title_entry.get(), dept_entry.get(), credits_entry.get()))
        update_button.grid(row=6, column=0, columnspan=2, pady=5)

        # List Data Button
        list_button = tk.Button(course_window, text="List Data", command=self.list_course_data)
        list_button.grid(row=7, column=0, columnspan=2, pady=5)

    def insert_teaches_data(self, _id, course_id, semester, year):
        # Use placeholders in the SQL query
        query = "INSERT INTO teaches VALUES (?, ?, 1, ?, ?)"
        
        # Pass values as a tuple to execute method
        self.cursor.execute(query, (_id, course_id, semester, year))
        
        print("Inserting Teaches Data:")
        print("ID:", _id)
        print("Course ID:", course_id)
        print("Semester:", semester)
        print("Year:", year)
        
        # Commit changes to the database
        self.connection.commit()


    def delete_teaches_data(self, _id):
        print("Deleting Teaches Data:")
        print("ID:", _id)

        # Uncomment the following line when you have the actual SQL query
        self.cursor.execute("DELETE FROM teaches WHERE id=?", (_id,))
        self.connection.commit()

    def update_teaches_data(self, _id, course_id, semester, year):
        print("Updating Teaches Data:")
        print("ID:", _id)
        print("Course ID:", course_id)
        print("Semester:", semester)
        print("Year:", year)

        # Uncomment the following line when you have the actual SQL query
        self.cursor.execute("UPDATE teaches SET course_id=?, semester=?, year=? WHERE id=?", (course_id, semester, year, _id))
        self.connection.commit()

    def list_teaches_data(self):
        print("Listing Teaches Data")

        # Uncomment the following line when you have the actual SQL query
        self.cursor.execute("SELECT * FROM teaches")
        rows = self.cursor.fetchall()

        # Create a new window to display the data
        list_window = tk.Toplevel(self.root)
        list_window.title("Teaches Data")

        # Create a treeview to display the data in a table
        tree = ttk.Treeview(list_window)
        tree["columns"] = ("ID", "Course ID", "Semester", "Year")
        tree.heading("ID", text="ID")
        tree.heading("Course ID", text="Course ID")
        tree.heading("Semester", text="Semester")
        tree.heading("Year", text="Year")

        # Insert data into the treeview
        for row in rows:
            tree.insert("", "end", values=row)

        # Pack the treeview to display it
        tree.pack()


    def insert_instructor_data(self, instructor_id, name, dept_name, salary, course_id):
        # Use placeholders in the SQL query
        query = "INSERT INTO instructor VALUES (?, ?, ?, ?)"
        
        # Pass values as a tuple to execute method
        self.cursor.execute(query, (instructor_id, name, dept_name, salary))
        # Burada veritabanına instructor eklemek için gerekli işlemleri yapabilirsiniz
        print("Inserting Instructor Data:")
        print("Instructor ID:", instructor_id)
        print("Name:", name)
        print("Dept-name:", dept_name)
        print("Salary:", salary)
        print("Course ID:", course_id)
        
        # Commit changes to the database
        self.connection.commit()

    def delete_instructor_data(self, instructor_id):
        # Burada veritabanında instructor silme işlemlerini yapabilirsiniz
        self.cursor.execute("DELETE FROM instructor WHERE id=?", (instructor_id,))
        self.connection.commit()
        print("Deleting Instructor Data:")
        print("Instructor ID:", instructor_id)

    def update_instructor_data(self, instructor_id, name, dept_name, salary, course_id):
        # Burada veritabanında instructor güncelleme işlemlerini yapabilirsiniz
        print("Updating Instructor Data:")
        print("Instructor ID:", instructor_id)
        print("Name:", name)
        print("Dept-name:", dept_name)
        print("Salary:", salary)
        print("Course ID:", course_id)
        self.cursor.execute("UPDATE instructor SET name=?, dept_name=?, salary=? WHERE id=?", (name, dept_name, salary, instructor_id))
        self.connection.commit()

    def list_instructor_data(self):
        # Burada veritabanındaki instructor verilerini listeleyebilirsiniz
        print("Listing Instructor Data")
        self.cursor.execute("SELECT * FROM instructor")
        rows = self.cursor.fetchall()

        # Create a new window to display the data
        list_window = tk.Toplevel(self.root)
        list_window.title("Instructor Data")

        # Create a treeview to display the data in a table
        tree = ttk.Treeview(list_window)
        tree["columns"] = ("ID", "Name", "Department", "Salary")
        tree.heading("ID", text="ID")
        tree.heading("Name", text="name")
        tree.heading("Department", text="dept_name")
        tree.heading("Salary", text="salary")

        # Insert data into the treeview
        for row in rows:
            tree.insert("", "end", values=row)

        # Pack the treeview to display it
        tree.pack()


    def insert_student_data(self, id, name, dept_name, tot_cred):
        # Use placeholders in the SQL query
        query = "INSERT INTO student VALUES (?, ?, ?, ?)"
        
        # Pass values as a tuple to execute method
        self.cursor.execute(query, (id, name, dept_name, tot_cred))
        # Burada veritabanına student eklemek için gerekli işlemleri yapabilirsiniz
        print("Inserting Student Data:")
        print("ID:", id)
        print("Name:", name)
        print("Dept-name:", dept_name)
        print("Tot-cred:", tot_cred)
        
        # Commit changes to the database
        self.connection.commit()

    def delete_student_data(self, id):
        # Burada veritabanında student silme işlemlerini yapabilirsiniz
        self.cursor.execute("DELETE FROM student WHERE id=?", (id,))
        self.connection.commit()
        print("Deleting Student Data:")
        print("ID:", id)

    def update_student_data(self, id, name, dept_name, tot_cred):
        self.cursor.execute("UPDATE student SET name=?, dept_name=?, tot_cred=? WHERE id=?", (name, dept_name, tot_cred, id))
        self.connection.commit()
        # Burada veritabanında student güncelleme işlemlerini yapabilirsiniz
        print("Updating Student Data:")
        print("ID:", id)
        print("Name:", name)
        print("Dept-name:", dept_name)
        print("Tot-cred:", tot_cred)

    def list_student_data(self):
        # Burada veritabanındaki student verilerini listeleyebilirsiniz
        print("Listing Student Data")
        self.cursor.execute("SELECT * FROM student")
        rows = self.cursor.fetchall()

        # Create a new window to display the data
        list_window = tk.Toplevel(self.root)
        list_window.title("Student Data")

        # Create a treeview to display the data in a table
        tree = ttk.Treeview(list_window)
        tree["columns"] = ("ID", "Name", "Department", "Total Credit")
        tree.heading("ID", text="ID")
        tree.heading("Name", text="name")
        tree.heading("Department", text="dept_name")
        tree.heading("Total Credit", text="tot_cred")

        # Insert data into the treeview
        for row in rows:
            tree.insert("", "end", values=row)

        # Pack the treeview to display it
        tree.pack()

    def insert_course_data(self, course_id, title, dept_name, credits):
        try:
            credits = int(credits)
        except ValueError:
            # Handle the case where credits is not a valid integer
            print("Invalid value for credits. Please enter a valid integer.")
            return

        query = "INSERT INTO course VALUES (?, ?, ?, ?)"
        
        # Pass values as a tuple to execute method
        self.cursor.execute(query, (course_id, title, dept_name, credits))
        # Burada veritabanına course eklemek için gerekli işlemleri yapabilirsiniz
        print("Inserting Course Data:")
        print("Course ID:", course_id)
        print("Title:", title)
        print("Dept-name:", dept_name)
        print("Credits:", credits)
        # Commit changes to the database
        self.connection.commit()

    def delete_course_data(self, course_id):
        # Burada veritabanında course silme işlemlerini yapabilirsiniz
        self.cursor.execute("DELETE FROM course WHERE id=?", (course_id,))
        self.connection.commit()
        print("Deleting Course Data:")
        print("Course ID:", course_id)

    def update_course_data(self, course_id, title, dept_name, credits):
        self.cursor.execute("UPDATE course SET title=?, dept_name=?, credits=? WHERE id=?", (title, dept_name, credits, course_id))
        self.connection.commit()
        # Burada veritabanında course güncelleme işlemlerini yapabilirsiniz
        print("Updating Course Data:")
        print("Course ID:", course_id)
        print("Title:", title)
        print("Dept-name:", dept_name)
        print("Credits:", credits)

    def list_course_data(self):
        # Burada veritabanındaki course verilerini listeleyebilirsiniz
        print("Listing Course Data")

        self.cursor.execute("SELECT * FROM course")
        rows = self.cursor.fetchall()

        # Create a new window to display the data
        list_window = tk.Toplevel(self.root)
        list_window.title("Course Data")

        # Create a treeview to display the data in a table
        tree = ttk.Treeview(list_window)
        tree["columns"] = ("Course ID", "Course Title", "Department", "Credıts")
        tree.heading("Course ID", text="course_id")
        tree.heading("Course Title", text="title")
        tree.heading("Department", text="dept_name")
        tree.heading("Credits", text="credits")

        # Insert data into the treeview
        for row in rows:
            tree.insert("", "end", values=row)

        # Pack the treeview to display it
        tree.pack()

# Uygulamayı başlatmak için
if __name__ == "__main__":
    root = tk.Tk()
    app = UniversityApp(root)
    root.mainloop()