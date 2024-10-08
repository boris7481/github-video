import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


def add_task():
  if task.get() !="":
      task_treeview.insert(parent="" , index="end", values=(task.get().replace( " " , "\ "  ) ))
      task_entry.delete(0 , tk.END)
  else:
      print("Bitte einen Task eingeben")

def remove_taks():
    selected_item = task_treeview.selection()
    if selected_item != ():
        task_treeview.delete(selected_item)
    else:
        print("bitte einen Task eingeben")

# Dans la ligne qui a le path de mon dossier j ai eu un pb au niveau de la lectu mais sur Stackoverflow j ai eu la solution
# il fallait juste mettre le peti r devant le nom du path.

def save_file():
    file_name = filedialog.asksaveasfilename(defaultextension=(".txt") , initialdir=r"C:\Users\boris\OneDrive\Desktop\todo-list", title="Datei speicher")
    if file_name:
        file = open( file_name , "w")
        for line in task_treeview.get_children():
            for value in task_treeview.item(line)["values"]:
                file.write( value  + "\n")
        file.close()


def open_file():
    file_name = filedialog.askopenfilename(initialdir=r"C:\Users\boris\OneDrive\Desktop\todo-list" , title= "Dateie öffnen")
    if file_name:
        file = open( file_name , "r")
        for line in file.readlines():
            task_treeview.insert(parent="", index="end", values=(line.replace(" ", "\ ")))
        file.close()


root = tk.Tk()
root.title("Todo_liste")
root.geometry("600x390")
root.columnconfigure(0, weight=1)  # # die erste Spalte hat ein gewicht von 1

task = tk.StringVar()

style = ttk.Style()
style.theme_use("clam")

# Frame
user_input_frame = ttk.Frame(root)
user_input_frame.grid(row=0, column=0, pady=20)
task_frame = ttk.Frame(root)
task_frame.grid(row=1, column=0, pady=10)

# Widget for user_input_frame
task_label = ttk.Label(user_input_frame, text="Task:")
task_label.grid(row=0, column=0)
task_entry = ttk.Entry(user_input_frame, width=60, textvariable=task )
task_entry.grid(row=0, column=1)

add_task_button = ttk.Button(user_input_frame, text="Task hinzufügen", command=add_task)
add_task_button.grid(row=1, column=0, columnspan=2, sticky="EW", pady=2)

# Widget for task_frame

task_treeview = ttk.Treeview(task_frame, selectmode="browse")
task_treeview.grid(row=0, column=0, sticky="EW")

# Spalten definieren und Interagieren
task_treeview.configure(columns=("task"))
# lorsque tu lance l application ici par defaut tu auras la Treevieu column = la premiere colonne
# vu que nous ne voulons pas cette colonne on necrit le code suivant pour l2eliminer

task_treeview.column("#0", width=0, stretch=tk.NO)
task_treeview.heading("task", text="Tasks")  # pour mettre le titre au dessus du button
task_treeview.column("task", width=575)

# Scrollbar für Treeview Widget erzeugen und an task treeview binden

task_treeview_sroll = ttk.Scrollbar(task_frame, orient="vertical", command=task_treeview.yview)
task_treeview_sroll.grid(row=0, column=1, sticky="NS")
task_treeview.configure(yscrollcommand=task_treeview_sroll)

delete_task_button = ttk.Button(task_frame, text="Markierte task entfernen" , command=remove_taks )
delete_task_button.grid(row=1, column=0, columnspan=2, sticky="EW")

# Menü mit Speichermechanismus
application_menu = tk.Menu(root)
root.configure(menu=application_menu)


file_menu = tk.Menu(application_menu) # untermenu
file_menu.add_command(label= "Datei speichern" , command=save_file) # un Menu punkt
file_menu.add_command(label="Datei öffnen" , command=open_file) # un autre Menu Punkt

application_menu.add_cascade(label="Datei" , menu = file_menu)
# tu clich sur Datei pour ouvrir le untermenu de file_name


root.mainloop()
