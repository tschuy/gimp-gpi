from gpi import installer, web
import Tkinter as tk
import ttk
import tkMessageBox


class Package:
    def __init__(self, package):
        self.package = package

    def __str__(self):
        return self.package['name']

# set up main window
root = tk.Tk()
master = tk.Frame(root, name='master')
master.pack(fill=tk.BOTH)

root.title('GIMP Plugin Installer')
nb = ttk.Notebook(master, name='nb')
nb.pack(fill=tk.BOTH, padx=2, pady=3)

# set up installable list
weblist_frame = tk.Frame(nb)
scrollbar = tk.Scrollbar(weblist_frame)
listbox = tk.Listbox(weblist_frame)

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.pack(side=tk.LEFT, fill=tk.Y)

scrollbar['command'] = listbox.yview
listbox['yscrollcommand'] = scrollbar.set

packages = web.get_packages()

for item in packages:
    item = Package(item)
    listbox.insert(tk.END, item)

weblist_frame.pack()

def installCallback():
    print "installCallback"
    sel = listbox.curselection()
    if len(sel) != 1:
        tkMessageBox.showwarning(
            "",
            "Select a package to install"
        )
        return
    print listbox.get(sel[0])

button_frame = tk.Frame(weblist_frame)
button = tk.Button(button_frame, text="Install", command=installCallback)

button.pack()
button_frame.pack(side=tk.TOP)

nb.add(weblist_frame, text="Available Packages")

# set up currently installed list
locallist_frame = tk.Frame(nb)
local_scrollbar = tk.Scrollbar(locallist_frame)
local_listbox = tk.Listbox(locallist_frame)

local_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

local_scrollbar['command'] = local_listbox.yview
local_listbox['yscrollcommand'] = local_scrollbar.set

local_packages = installer.currently_installed()

for item in local_packages:
    item = Package(item)
    local_listbox.insert(tk.END, item)

local_listbox.pack(side=tk.LEFT, fill=tk.Y)
locallist_frame.pack()

def uninstallCallback():
    print "installCallback"
    sel = local_listbox.curselection()
    if len(sel) != 1:
        tkMessageBox.showwarning(
            "",
            "Select a package to install"
        )
        return
    print listbox.get(sel[0])

uninstall_button_frame = tk.Frame(nb)
uninstall_button = tk.Button(uninstall_button_frame, text="Remove", command=uninstallCallback)

uninstall_button.pack()
uninstall_button_frame.pack(side=tk.TOP)

nb.add(locallist_frame, text="Currently Installed")


master.mainloop()


# def installCallback(evt):
#     print listbox.curselection()
#
# button = tk.Button(button_frame, text ="Install", command=installCallback)
