import tkinter as tk

#this is the main app/frame
root=tk.Tk()

#define the menu elements
menu_label=tk.Label(text='Mushroom Farm Tracker')
menu_add=tk.Button(text='Add/Update Cultures')
menu_about=tk.Button(text='About Data')
menu_notes=tk.Button(text='Take New Notes')

# label=tk.Label(text='Name')
# entry= tk.Entry()

#pack the menu elements
menu_label.pack()
menu_add.pack()
menu_about.pack()
menu_notes.pack()


# label.pack()
# entry.pack()



root.mainloop()