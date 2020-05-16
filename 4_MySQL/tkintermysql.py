from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont

class StudentDB:
    # DB connection
    conn = 0
    # Cursor used to traverse results
    cursor = 0
    # Stores results of last query
    query = 0
    # Treeview that displays student data
    student_tree = None
    # Treeview header array
    headers = ['ID', 'F Name', 'L Name', 'Email', 'Street', 'City', 'State', 'Zip', 'Phone', 'Birth', 'Sex', 'Lunch']

    def setup_db(self):

        # Setup treeview
        self.student_tree = ttk.Treeview(columns=headers, show="headings")

        try:
            self.conn = mysql.connector.connect(host='localhost', database='students', user='studentadmin', password='TurtleDove')
            self.cursor = conn.cursor()
            # Get all student data for the treeview
            self.query = "SELECT * FROM students"
            self.cursor.execute(query)
            results = cursor.fetchall()
        except mysql.connector.Error as error:
            print("Error :", error)
        # finally:
        #     if(conn.is_connected()):
        #         conn.close()

    def update_treeview(self):
        pass

    def create_treeview(self):
        for col in self.header:
            self.student_tree.heading(col, text=col.title())
            # adjust the column's width to the header string
            self.student_tree.column(col,
                width=tkFont.Font().measure(col.title()))
        # for item in car_list:
        #     self.tree.insert('', 'end', values=item)

    def stud_update(self):
        pass

    def stud_add(self):
        pass

    def stud_delete(self):
        pass

    def __init__(self, root):
        root.title("Student Database")
        root.geometry("900x400")

        self.create_treeview()

        # ---- 1st Row ----
        # Student ID label and entry box
        sid_label = Label(root, text='ID')
        sid_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        # Holds the changing value for ID
        self.sid_entry_value = StringVar(root, value="")
        self.sid_entry = ttk.Entry(root,
                                  textvariable=self.sid_entry_value)
        self.sid_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        # First name label and entry box
        fn_label = Label(root, text='F Name')
        fn_label.grid(row=0, column=2, padx=10, pady=10, sticky=W)
        self.fn_entry_value = StringVar(root, value="")
        self.fn_entry = ttk.Entry(root,
                                  textvariable=self.fn_entry_value)
        self.fn_entry.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        # Last name label and entry box
        ln_label = Label(root, text='L Name')
        ln_label.grid(row=0, column=4, padx=10, pady=10, sticky=W)
        self.ln_entry_value = StringVar(root, value="")
        self.ln_entry = ttk.Entry(root,
                                  textvariable=self.ln_entry_value)
        self.ln_entry.grid(row=0, column=5, padx=10, pady=10, sticky=W)

        # ---- 2nd Row ----
        # email label and entry box
        email_label = Label(root, text='Email')
        email_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.email_entry_value = StringVar(root, value="")
        self.email_entry = ttk.Entry(root,
                                  textvariable=self.email_entry_value)
        self.email_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        # street label and entry box
        street_label = Label(root, text='Street')
        street_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)
        self.street_entry_value = StringVar(root, value="")
        self.street_entry = ttk.Entry(root,
                                  textvariable=self.street_entry_value)
        self.street_entry.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        # city label and entry box
        city_label = Label(root, text='City')
        city_label.grid(row=1, column=4, padx=10, pady=10, sticky=W)
        self.city_entry_value = StringVar(root, value="")
        self.city_entry = ttk.Entry(root,
                                  textvariable=self.city_entry_value)
        self.city_entry.grid(row=1, column=5, padx=10, pady=10, sticky=W)

        # ---- 3rd Row ----
        # state label and entry box
        state_label = Label(root, text='State')
        state_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        self.state_entry_value = StringVar(root, value="")
        self.state_entry = ttk.Entry(root,
                                  textvariable=self.state_entry_value)
        self.state_entry.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        # zip code label and entry box
        zip_label = Label(root, text='Zip')
        zip_label.grid(row=2, column=2, padx=10, pady=10, sticky=W)
        self.zip_entry_value = StringVar(root, value="")
        self.zip_entry = ttk.Entry(root,
                                  textvariable=self.zip_entry_value)
        self.zip_entry.grid(row=2, column=3, padx=10, pady=10, sticky=W)

        # phone label and entry box
        phone_label = Label(root, text='Phone')
        phone_label.grid(row=2, column=4, padx=10, pady=10, sticky=W)
        self.phone_entry_value = StringVar(root, value="")
        self.phone_entry = ttk.Entry(root,
                                  textvariable=self.phone_entry_value)
        self.phone_entry.grid(row=2, column=5, padx=10, pady=10, sticky=W)

        # ---- 4th Row ----
        # Birth date label and entry box
        birth_label = Label(root, text='Birth')
        birth_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)
        self.birth_entry_value = StringVar(root, value="")
        self.birth_entry = ttk.Entry(root,
                                  textvariable=self.birth_entry_value)
        self.birth_entry.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        # Sex label and entry box
        sex_label = Label(root, text='Sex')
        sex_label.grid(row=3, column=2, padx=10, pady=10, sticky=W)
        self.sex_entry_value = StringVar(root, value="")
        self.sex_entry = ttk.Entry(root,
                                  textvariable=self.sex_entry_value)
        self.sex_entry.grid(row=3, column=3, padx=10, pady=10, sticky=W)

        # Lunch label and entry box
        lunch_label = Label(root, text='Lunch')
        lunch_label.grid(row=3, column=4, padx=10, pady=10, sticky=W)
        self.lunch_entry_value = StringVar(root, value="")
        self.lunch_entry = ttk.Entry(root,
                                  textvariable=self.lunch_entry_value)
        self.lunch_entry.grid(row=3, column=5, padx=10, pady=10, sticky=W)

        # ---- 5th Row ----
        self.update_button = ttk.Button(root,
                            text="Update",
                            command=lambda: self.stud_update())
        self.update_button.grid(row=4, column=0,
                                padx=10, pady=10, sticky=W)
        self.add_button = ttk.Button(root,
                            text="Add",
                            command=lambda: self.stud_add())
        self.add_button.grid(row=4, column=2,
                                padx=10, pady=10, sticky=W)
        self.delete_button = ttk.Button(root,
                            text="Delete",
                            command=lambda: self.stud_delete())
        self.delete_button.grid(row=4, column=4,
                                padx=10, pady=10, sticky=W)

        # ----- Treeview Row -----


root = Tk()
stud_db = StudentDB(root)
root.mainloop()
