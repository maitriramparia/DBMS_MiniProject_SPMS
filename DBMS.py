from tkinter import *
import mysql.connector
from tkinter import messagebox

# MySQL Database Connection
conn = mysql.connector.connect(
    user='root',
    password='pass@123',
    host='localhost',
    database='maitri_s026'
)

cursor = conn.cursor()


class First:

    def __init__(self, root):
        self.f = Frame(root, height=400, width=500)
        self.f.pack()

        self.l1 = Label(self.f, text='s_id:')
        self.l2 = Label(self.f, text='s_name:')
        self.l3 = Label(self.f, text='s_gender:')
        self.l4 = Label(self.f, text='s_contact:')
        self.l5 = Label(self.f, text='m_id:')
        self.l6 = Label(self.f, text='s_age:')

        self.e1 = Entry(self.f, width=18)
        self.e2 = Entry(self.f, width=18)
        self.e3 = Entry(self.f, width=18)
        self.e4 = Entry(self.f, width=18)
        self.e5 = Entry(self.f, width=18)
        self.e6 = Entry(self.f, width=18)

        # Buttons
        self.b1 = Button(
            self.f, text="Insert", command=self.insert
        )

        self.b2 = Button(
            self.f, text="Delete", command=self.delete
        )

        self.b3 = Button(
            self.f, text="Update", command=self.update
        )

        # Labels and Entry Fields
        self.l1.place(x=50, y=30)
        self.e1.place(x=200, y=30)

        self.l2.place(x=50, y=60)
        self.e2.place(x=200, y=60)

        self.l3.place(x=50, y=90)
        self.e3.place(x=200, y=90)

        self.l4.place(x=50, y=120)
        self.e4.place(x=200, y=120)

        self.l5.place(x=50, y=150)
        self.e5.place(x=200, y=150)

        self.l6.place(x=50, y=180)
        self.e6.place(x=200, y=180)

        # Buttons Placement
        self.b1.place(x=100, y=230)
        self.b2.place(x=200, y=230)
        self.b3.place(x=300, y=230)

    # Function to Insert Student
    def insert(self):
        try:
            s_id = int(self.e1.get())
            s_name = self.e2.get()
            s_gender = self.e3.get()
            s_contact = int(self.e4.get())
            m_id = int(self.e5.get())
            s_age = int(self.e6.get())

            if not s_name.strip() or not s_gender.strip():
                messagebox.showerror(
                    "Input Error",
                    "Name and gender cannot be empty."
                )
                return

            sql = """
                INSERT INTO student
                (s_id, s_name, s_gender, s_contact, m_id, s_age)
                VALUES (%s, %s, %s, %s, %s, %s)
            """

            values = (
                s_id, s_name, s_gender,
                s_contact, m_id, s_age
            )

            cursor.execute(sql, values)
            conn.commit()

            messagebox.showinfo(
                "Success",
                "Student inserted successfully!"
            )

            self.clear()

        except ValueError:
            messagebox.showerror(
                "Input Error",
                "Enter valid numbers for ID, contact, m_id and age."
            )

        except mysql.connector.Error as err:
            conn.rollback()
            messagebox.showerror("Database Error", str(err))

    # Function to Delete Student
    def delete(self):
        try:
            s_id = int(self.e1.get())

            answer = messagebox.askyesno(
                "Confirm Delete",
                "Are you sure you want to delete this student?"
            )

            if not answer:
                return

            sql = "DELETE FROM student WHERE s_id = %s"
            cursor.execute(sql, (s_id,))
            conn.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo(
                    "Success",
                    "Student deleted successfully!"
                )
                self.clear()
            else:
                messagebox.showinfo(
                    "Not Found",
                    "Student ID does not exist."
                )

        except ValueError:
            messagebox.showerror(
                "Input Error",
                "Enter a valid student ID."
            )

        except mysql.connector.Error as err:
            conn.rollback()
            messagebox.showerror("Database Error", str(err))

    # Function to Update Student
    def update(self):
        try:
            s_id = int(self.e1.get())
            s_name = self.e2.get()
            s_gender = self.e3.get()
            s_contact = int(self.e4.get())
            m_id = int(self.e5.get())
            s_age = int(self.e6.get())

            if not s_name.strip() or not s_gender.strip():
                messagebox.showerror(
                    "Input Error",
                    "Name and gender cannot be empty."
                )
                return

            sql = """
                UPDATE student
                SET s_name = %s,
                    s_gender = %s,
                    s_contact = %s,
                    m_id = %s,
                    s_age = %s
                WHERE s_id = %s
            """

            values = (
                s_name, s_gender, s_contact,
                m_id, s_age, s_id
            )

            cursor.execute(sql, values)
            conn.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo(
                    "Success",
                    "Student updated successfully!"
                )
                self.clear()
            else:
                messagebox.showinfo(
                    "Not Found",
                    "Student ID not found or no changes were made."
                )

        except ValueError:
            messagebox.showerror(
                "Input Error",
                "Enter valid numbers for ID, contact, m_id and age."
            )

        except mysql.connector.Error as err:
            conn.rollback()
            messagebox.showerror("Database Error", str(err))

    # Function to Clear All Fields
    def clear(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
        self.e5.delete(0, END)
        self.e6.delete(0, END)


# Main Program
root = Tk()
root.title("Student Registration Form")
root.geometry("500x350")

obj = First(root)


# Close database connection when window closes
def close_app():
    cursor.close()
    conn.close()
    root.destroy()


root.protocol("WM_DELETE_WINDOW", close_app)

root.mainloop()