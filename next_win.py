from tkinter import *
from tkinter import messagebox
import mysql.connector

# MySQL Connection
conn = mysql.connector.connect(
    user='root',
    password='pass@123',
    host='localhost',
    database='Maitri_S026'
)

cursor = conn.cursor()


class Next:
    def __init__(self, root):
        self.f = Frame(root, height=800, width=800)
        self.f.pack(fill=BOTH, expand=True)

        self.b1 = Button(
            self.f,
            text="Show",
            command=self.display
        )
        self.b1.place(x=200, y=20)

        self.result_frame = Frame(self.f)
        self.result_frame.place(x=20, y=70)

    def display(self):
        try:
            # Clear old records
            for widget in self.result_frame.winfo_children():
                widget.destroy()

            print("----------View records-----------")

            cursor.execute("SELECT * FROM student LIMIT 0,10")
            records = cursor.fetchall()

            if not records:
                messagebox.showinfo(
                    "Information",
                    "No records found."
                )
                return

            # Display column headings
            for j, col in enumerate(cursor.column_names):
                Label(
                    self.result_frame,
                    text=col,
                    fg="blue",
                    width=12,
                    relief=GROOVE
                ).grid(row=0, column=j)

            # Display records
            for i, record in enumerate(records, start=1):
                for j, value in enumerate(record):
                    e = Entry(
                        self.result_frame,
                        width=12,
                        fg="green"
                    )
                    e.grid(row=i, column=j)
                    e.insert(END, str(value))
                    e.config(state="readonly")

        except mysql.connector.Error as err:
            messagebox.showerror(
                "Database Error",
                str(err)
            )


root = Tk()
root.title("Welcome To Next Window")
root.geometry("800x500")

obj = Next(root)


def close_app():
    cursor.close()
    conn.close()
    root.destroy()


root.protocol("WM_DELETE_WINDOW", close_app)

root.mainloop()