from tkinter import *
import sqlite3

# creating a root widget (window)
root = Tk()
root.title('DB GUI')
root.iconbitmap('..\\..\\misc\\tech.ico')  # add user defined icon
root.geometry('400x400')

# enter DB details
f_name_lbl = Label(root, text='First Name')  # Label
f_name_lbl.grid(row=0, column=0, padx=10)
f_name = Entry(root, width=30)  # Input box
f_name.grid(row=0, column=1)

l_name_lbl = Label(root, text='Last Name')  # Label
l_name_lbl.grid(row=1, column=0)
l_name = Entry(root, width=30)  # Input box
l_name.grid(row=1, column=1)

address_lbl = Label(root, text='Address')  # Label
address_lbl.grid(row=2, column=0)
address = Entry(root, width=30)  # Input box
address.grid(row=2, column=1)

city_lbl = Label(root, text='City')  # Label
city_lbl.grid(row=3, column=0)
city = Entry(root, width=30)  # Input box
city.grid(row=3, column=1)

state_lbl = Label(root, text='State')  # Label
state_lbl.grid(row=4, column=0)
state = Entry(root, width=30)  # Input box
state.grid(row=4, column=1)

zipcode_lbl = Label(root, text='Zipcode')  # Label
zipcode_lbl.grid(row=5, column=0)
zipcode = Entry(root, width=30)  # Input box
zipcode.grid(row=5, column=1)

def submit():
    # database
    conn = sqlite3.connect('address_book.db')

    # create cursor
    c = conn.cursor()

    # add details to table
    c.execute('INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)',
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })

    # commit changes to db
    conn.commit()

    # close connection
    conn.close()

    # empty the input fields
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


def query():
    # database
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    # query the database
    c.execute('SELECT *, oid FROM addresses')  # oid is the SQLite3 Primary key
    records = c.fetchall()

    # loop the results
    print_records = ''
    for record in records:
        print_records = f'First name: {record[0]} \n' \
                        f'Last name: {record[1]} \n' \
                        f'Address: {record[2]} \n' \
                        f'City: {record[3]} \n' \
                        f'State: {record[4]} \n' \
                        f'Zip Code: {record[5]}'

    qry_lbl = Label(root, text=print_records)
    qry_lbl.grid(row=8, column=0, columnspan=2, sticky='w')

    # commit changes to db
    conn.commit()

    # close connection
    conn.close()


# create submit button
sub_btn = Button(root, text='Add Record', command=submit)
sub_btn.grid(row=6, column=0, columnspan=2, pady=2, padx=10, ipadx=100)

# create a query button
qry_btn = Button(root, text='Show Records', command=query)
qry_btn.grid(row=7, column=0, columnspan=2, padx=8, ipadx=100)

# create a mainloop to run the root widget
root.mainloop()
