import functions
import ttkbootstrap as tb

window = tb.Window(themename="darkly")
window.title("To do app")
window.geometry('550x650')


def add_todo_gui(new_todo):
    list_content = functions.get_todo_list()
    list_content.append(new_todo + '\n')
    functions.set_todo_list(list_content)
    update_list()


def edit_todo(new_todo):
    index_edit = int(index_combo.get())
    print(index_edit)
    list_content = functions.get_todo_list()
    list_content[index_edit] = str(new_todo + '\n')
    functions.set_todo_list(list_content)

    for index, item in enumerate(list_content):
        actual_string = str(index) + ") " + item.strip('\n')

        if index == index_edit:
            print_lbl = tb.Label(list_frame, text=actual_string + (" " * 20), font=("Segoe UI", 10, "italic"),
                                 bootstyle="warning")
            print_lbl.grid(column=0, row=index, pady=5, sticky="w")
        else:
            print_lbl = tb.Label(list_frame, text=actual_string, font=("Segoe UI", 10, "italic"))
            print_lbl.grid(column=0, row=index, pady=5, sticky="w")


def update_list():
    content = functions.get_todo_list()
    for index, item in enumerate(content):
        actual_string = str(index) + ") " + item.strip('\n')
        print_lbl = tb.Label(list_frame, text=actual_string, font=("Segoe UI", 10, "italic"))
        print_lbl.grid(column=0, row=index, pady=5, sticky="w")


def delete_item():
    index = int(index_combo.get())
    print(index)
    list_content = functions.get_todo_list()

    clear_lbl()
    list_content.pop(index)
    print(list_content)
    functions.set_todo_list(list_content)

    update_list()


def clear_lbl():
    content = functions.get_todo_list()
    for index, item in enumerate(content):
        print_lbl = tb.Label(list_frame, text=(" " * 40), font=("Segoe UI", 10, "italic"))
        print_lbl.grid(column=0, row=index, pady=5, sticky="w")


# ---------- Title ---------- #
title_lbl = tb.Label(text="Welcome to the TO DO app", font=("Helvetica", 20, "bold"))
title_lbl.pack(pady=(60, 5))

data_frame = tb.Frame(window)
data_frame.pack()

# ---------- Data Frame ---------- #
style = tb.Style()
style.configure('success.TButton', font=("Segoe UI", 12, 'bold'))

new_todo_entry = tb.Entry(data_frame, width=60)
new_todo_entry.pack(pady=10)

new_todo_btn = tb.Button(data_frame, text="ADD", bootstyle="success",
                         command=lambda: add_todo_gui(new_todo_entry.get()), width=10)
new_todo_btn.pack(padx=10, pady=(0, 10))

index_lbl = tb.Label(data_frame, text="Select the index to modify", font=("Segoe UI", 10, "bold"))
index_lbl.pack(pady=(5, 0))

combo_values = len(functions.get_todo_list())
result = [i for i in range(combo_values)]
index_combo = tb.Combobox(data_frame, bootstyle="primary", width=5, values=result)
index_combo.pack(pady=(5, 5))

# ---------- Button Frame ---------- #
btn_frame = tb.Frame(data_frame)
btn_frame.pack()

edit_btn = tb.Button(btn_frame, text="Edit", bootstyle="outline-info", width=10,
                     command=lambda: edit_todo(new_todo_entry.get()))
edit_btn.pack(padx=10, pady=(0, 10), side='left', fill='both')

delete_btn = tb.Button(btn_frame, text="Complete", bootstyle="outline-danger", width=10,
                       command=lambda: delete_item())
delete_btn.pack(padx=10, pady=(0, 10), side='left', fill='both')

list_frame = tb.Frame(data_frame)
list_frame.pack()

update_list()

window.mainloop()
