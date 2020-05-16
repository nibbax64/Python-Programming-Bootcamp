from tkinter import *
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
from datetime import datetime

class StudentDB:
    # Used as te headers for the treeview table
    headers = ['ID', 'First Name', 'Last Name', 'Email', 'Street', 'City', 'State', 'Zip', 'Phone', 'Birth', 'Sex', 'Lunch']
    # Sample data used to test the look of the treeview
    student_info = []
    conn = 0
    cursor = 0
    query = 0

    def __init__(self):
        # Will hold all the student data in a treeview table
        self.tree = None
        self.setup_db()
        self.create_widgets()

    def setup_db(self):
        try:
            self.conn = mysql.connector.connect(host='localhost', database='students', user='studentadmin', password='TurtleDove')
        except mysql.connector.Error as error:
            print("Error :", error)

    # Initializes all of the widgets in our app
    def create_widgets(self):
        # ----- ROW 1 -----
        # Create the lable and place it in the upper left hand corner using
        # the grid layout
        sid_label = Label(root, text='ID')
        sid_label.grid(row=0, column=0, padx=5, pady=10, sticky=W)

        # Will hold the values entered into the entry widget
        self.sid_entry_value = StringVar(root, value="")

        # Create the entry widget and assign all values entered
        # into it to the StringVar
        self.sid_entry = ttk.Entry(root,
                                  textvariable=self.sid_entry_value)
        self.sid_entry.grid(row=0, column=1, padx=5, pady=10, sticky=W)

        f_name_label = Label(root, text='First Name')
        f_name_label.grid(row=0, column=2, padx=5, pady=10, sticky=W)
        self.f_name_entry_value = StringVar(root, value="")
        self.f_name_entry = ttk.Entry(root,
                                  textvariable=self.f_name_entry_value)
        self.f_name_entry.grid(row=0, column=3, padx=5, pady=10, sticky=W)

        l_name_label = Label(root, text='Last Name')
        l_name_label.grid(row=0, column=4, padx=5, pady=10, sticky=W)
        self.l_name_entry_value = StringVar(root, value="")
        self.l_name_entry = ttk.Entry(root,
                                  textvariable=self.l_name_entry_value)
        self.l_name_entry.grid(row=0, column=5, padx=5, pady=10, sticky=W)

        email_label = Label(root, text='Email')
        email_label.grid(row=0, column=6, padx=5, pady=10, sticky=W)
        self.email_entry_value = StringVar(root, value="")
        self.email_entry = ttk.Entry(root,
                                  textvariable=self.email_entry_value)
        self.email_entry.grid(row=0, column=7, padx=5, pady=10, sticky=W)

        street_label = Label(root, text='Street')
        street_label.grid(row=0, column=8, padx=5, pady=10, sticky=W)
        self.street_entry_value = StringVar(root, value="")
        self.street_entry = ttk.Entry(root,
                                  textvariable=self.street_entry_value)
        self.street_entry.grid(row=0, column=9, padx=5, pady=10, sticky=W)

        # ----- 2nd ROW -----
        city_label = Label(root, text='City')
        city_label.grid(row=1, column=0, padx=5, pady=10, sticky=W)
        self.city_entry_value = StringVar(root, value="")
        self.city_entry = ttk.Entry(root,
                                  textvariable=self.city_entry_value)
        self.city_entry.grid(row=1, column=1, padx=5, pady=10, sticky=W)

        state_label = Label(root, text='State')
        state_label.grid(row=1, column=2, padx=5, pady=10, sticky=W)
        self.state_entry_value = StringVar(root, value="")
        self.state_entry = ttk.Entry(root,
                                  textvariable=self.state_entry_value)
        self.state_entry.grid(row=1, column=3, padx=5, pady=10, sticky=W)

        zip_label = Label(root, text='Zip Code')
        zip_label.grid(row=1, column=4, padx=5, pady=10, sticky=W)
        self.zip_entry_value = StringVar(root, value="")
        self.zip_entry = ttk.Entry(root,
                                  textvariable=self.zip_entry_value)
        self.zip_entry.grid(row=1, column=5, padx=5, pady=10, sticky=W)

        phone_label = Label(root, text='Phone')
        phone_label.grid(row=1, column=6, padx=5, pady=10, sticky=W)
        self.phone_entry_value = StringVar(root, value="")
        self.phone_entry = ttk.Entry(root,
                                  textvariable=self.phone_entry_value)
        self.phone_entry.grid(row=1, column=7, padx=5, pady=10, sticky=W)

        birth_label = Label(root, text='Birth')
        birth_label.grid(row=1, column=8, padx=5, pady=10, sticky=W)
        self.birth_entry_value = StringVar(root, value="")
        self.birth_entry = ttk.Entry(root,
                                  textvariable=self.birth_entry_value)
        self.birth_entry.grid(row=1, column=9, padx=5, pady=10, sticky=W)

        # ----- 3RD ROW -----
        sex_label = Label(root, text='Sex')
        sex_label.grid(row=2, column=0, padx=5, pady=10, sticky=W)
        self.sex_entry_value = StringVar(root, value="")
        self.sex_entry = ttk.Entry(root,
                                  textvariable=self.sex_entry_value)
        self.sex_entry.grid(row=2, column=1, padx=5, pady=10, sticky=W)

        lunch_label = Label(root, text='Lunch')
        lunch_label.grid(row=2, column=2, padx=5, pady=10, sticky=W)
        self.lunch_entry_value = StringVar(root, value="")
        self.lunch_entry = ttk.Entry(root,
                                  textvariable=self.lunch_entry_value)
        self.lunch_entry.grid(row=2, column=3, padx=5, pady=10, sticky=W)

        # Create the button that will be used in the next video to add
        # student data to the database
        add_button = ttk.Button(root, text='Add Student', command=self.add_student)
        add_button.grid(column=4, row=2, sticky=(W, E))

        update_button = ttk.Button(root, text='Update Student', command=self.update_student)
        update_button.grid(column=5, row=2, sticky=(W, E))

        delete_button = ttk.Button(root, text='Delete Student', command=self.delete_student)
        delete_button.grid(column=6, row=2, sticky=(W, E))

        # ----- TREEVIEW -----
        # Treeviews can be used to display tables of data
        # Define the column names
        self.tree = ttk.Treeview(root, height=15, columns=('ID', 'First Name', 'Last Name', 'Email', 'Street', 'City', 'State', 'Zip', 'Phone', 'Birth', 'Sex', 'Lunch'), selectmode='browse')

        # Place the tree in the remaining space in the grid
        self.tree.grid(row=3, column=0, columnspan=17)
        # Define that we want to show the heading row
        self.tree['show'] = 'headings'

        # Assign the heading and column options
        i = 1
        for col in self.headers:
            num = f'#{i}' # Format string to produce incrementing numbers
            self.tree.heading(num, text=col)
            self.tree.column(num, width=115)
            i += 1

        self.update_table()

    def all_entries_filled(self, sid_required):
        if len(self.f_name_entry_value.get()) == 0 or len(self.l_name_entry_value.get()) == 0 or len(self.email_entry_value.get()) == 0 or len(self.street_entry_value.get()) == 0 or len(self.city_entry_value.get()) == 0 or len(self.state_entry_value.get()) == 0 or len(self.zip_entry_value.get()) == 0 or len(self.phone_entry_value.get()) == 0 or len(self.birth_entry_value.get()) == 0 or len(self.sex_entry_value.get()) == 0 or len(self.lunch_entry_value.get()) == 0:
            return False
        elif sid_required:
            if len(self.sid_entry_value.get()) == 0:
                return False
            else:
                return True
        else:
            return True

    def execute_query(self, result_expected):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(self.query)
            if result_expected:
                self.student_info = self.cursor.fetchall()
            self.conn.commit()
            self.cursor.close()
        except mysql.connector.Error as error:
            print("Error :", error)

    def update_table(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        self.query = "SELECT student_id, first_name, last_name, email, street, city, state, zip, phone, birth_date, sex, lunch_cost FROM students"
        self.execute_query(True)
        i = 1
        for stud_info in self.student_info:
            num = f'#{i}'
            self.tree.insert('', 'end', values=stud_info)
            i += 1

    def add_student(self):
        if(self.conn.is_connected() and not self.all_entries_filled(False)):
            self.popup_msg("Enter All the Student Data")
        else:
            now_time = datetime.now()
            format_date = now_time.strftime('%Y-%m-%d %H:%M:%S')
            f_name = self.f_name_entry_value.get()
            l_name = self.l_name_entry_value.get()
            email = self.email_entry_value.get()
            street = self.street_entry_value.get()
            city = self.city_entry_value.get()
            state = self.state_entry_value.get()
            zip = self.zip_entry_value.get()
            phone = self.phone_entry_value.get()
            birth = self.birth_entry_value.get()
            sex = self.sex_entry_value.get()
            lunch = self.lunch_entry_value.get()

            self.query = f"INSERT INTO students  VALUES(NULL, '{f_name}', '{l_name}', '{email}', '{street}', '{city}', '{state}', '{zip}', '{phone}', '{birth}', '{sex}', '{format_date}', {lunch})"
            self.execute_query(False)
            self.update_table()


    def update_student(self):
        if(self.conn.is_connected() and not self.all_entries_filled(True)):
            self.popup_msg("Enter All the Student Data")
        else:
            sid = self.sid_entry_value.get()
            f_name = self.f_name_entry_value.get()
            l_name = self.l_name_entry_value.get()
            email = self.email_entry_value.get()
            street = self.street_entry_value.get()
            city = self.city_entry_value.get()
            state = self.state_entry_value.get()
            zip = self.zip_entry_value.get()
            phone = self.phone_entry_value.get()
            birth = self.birth_entry_value.get()
            sex = self.sex_entry_value.get()
            lunch = self.lunch_entry_value.get()
            self.query = f"UPDATE students SET first_name = '{f_name}', last_name='{l_name}', email='{email}', street='{street}', city='{city}', state='{state}', zip={zip}, phone='{phone}', birth_date='{birth}', sex='{sex}', lunch_cost={lunch} WHERE student_id={sid}"
            self.execute_query(False)
            self.update_table()

    def delete_student(self):
        if(self.conn.is_connected()):
            if len(self.sid_entry_value.get()) == 0:
                self.popup_msg("Enter A Student ID Number")
            else:
                sid = self.sid_entry_value.get()
                self.query = f"DELETE FROM students WHERE student_id = {sid}"
                self.execute_query(False)
                self.update_table()

    def popup_msg(self, msg):
        popup = Tk()
        popup.geometry("235x85")
        popup.resizable(width=False, height=False)
        popup.wm_title("Enter All Values")
        err_msg = Text(popup, font=("Verdana", 16))
        err_msg.insert(INSERT, msg)
        err_msg.pack()
        ok_but = ttk.Button(popup, text="OK", command=popup.destroy)
        ok_but.place(relx=.5, rely=.8, anchor="center")
        popup.mainloop()

# Create the main window
root = Tk()
# Define the size of the main window
root.geometry("1400x600")
# Add a title to our app
root.title("Student Database")
# Create the studentDB object
student_db = StudentDB()
# Continue running our app until quit is clicked
root.mainloop()
