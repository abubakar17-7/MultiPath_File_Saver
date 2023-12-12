import tkinter as tk, webbrowser, sys, os
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import shutil

############################################################################
##                                                                        ##
##                             RESOURCE PATH                              ##
##                                                                        ##
############################################################################

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

############################################################################
##                                                                        ##
##                                COMPLETE                                ##
##                                                                        ##
############################################################################

def Complete():
    
    for widgets in Body_Frame.winfo_children():
        widgets.destroy()
        
    ############################################################################
    ##                                                                        ##
    ############################################################################

    Content_Frame = tk.Frame(Body_Frame)
    Content_Frame.pack(expand = 1, fill = "both", side = "left")
    
    scrollbar = tk.Scrollbar(Content_Frame)

    tree = ttk.Treeview(Content_Frame, height = 18, column = ("c1", "c2"), show = "headings", yscrollcommand = scrollbar.set)
    
    scrollbar.pack(side = "right", fill = "y")

    tree.column("#1", anchor = tk.CENTER, width = 672)

    tree.heading("#1", text = "USER")

    tree.column("#2", anchor = tk.CENTER, width = 672)

    tree.heading("#2", text = "STATUS")

    tree.pack()

    scrollbar.config(command = tree.yview)
    
    for folder in List[0]:
        if folder in List[1]:
            status = "Successful"
        elif folder in List[2]:
            status = "Unsuccessful"
        enter = (folder, status)
        tree.insert("", tk.END, values = enter)
  
    ttk.Button(Content_Frame, text="RETURN TO MAIN", command = Main).pack(pady=10)

############################################################################
##                                                                        ##
##                                SAVE FILE                               ##
##                                                                        ##
############################################################################

def SaveFile(file_path):
    
    [widget.destroy() for widget in Body_Frame.winfo_children()]

    users_directories = ["//192.168.0.211/LocalUser/cso1312/FOR AMCS",
                         "//192.168.0.211/LocalUser/cso1313/FOR AMCS",
                         "//192.168.0.211/LocalUser/cso1314/FOR AMCS",
                         "//192.168.0.211/LocalUser/cso1315/FOR AMCS",
                         "//192.168.0.211/LocalUser/cso1316/FOR AMCS",
                         "//192.168.0.211/LocalUser/cso1317/FOR AMCS",
                         "//192.168.0.211/LocalUser/cso1321/FOR AMCS",
                         "//192.168.0.211/LocalUser/cso1322/FOR AMCS",
                         "//192.168.0.211/LocalUser/cso1323/FOR AMCS",
                         "//192.168.0.211/LocalUser/cso1324/FOR AMCS",
                         "//192.168.0.211/LocalUser/cso1325/FOR AMCS",
                         "//192.168.0.211/LocalUser/cso1326/FOR AMCS"
                         ]
    
    def save_to_multiple_users(file_path):
        for user_directory in users_directories:
            reciever = user_directory[26:33]
            List[0].append(reciever)
            message.config(text = f"Saving File in {reciever}")
            # Construct the destination path for each user
            destination_path = f"{user_directory}/{file_path.split('/')[-1]}"
            try:
                # Copy the file to the user's directory
                shutil.copy(file_path, destination_path)
                List[1].append(reciever)

            except Exception as e:
                tk.messagebox.showinfo("Success", f"Error Occurs {e}")
                List[2].append(reciever)

        Complete()

    tk.Label(Body_Frame, text="SAVING FILES", font="Helvetica 14 bold").pack(pady=10)

    message = tk.Label(Body_Frame, text="", font="Helvetica 10")
    message.pack()

    # 
    global List      
    List = [[], [], []]
    save_to_multiple_users(file_path)

############################################################################
##                                                                        ##
##                               CHOOSE FILE                              ##
##                                                                        ##
############################################################################

def chooseFile():
    
    # define a function to upload a file
    def upload():
        
        global file_path
        file_path = filedialog.askopenfilename()
        
        if file_path:
            file.config(text="Selected File: " + file_path)
        
        return
    
    # define a function to go to the next step
    def next_func():
        
        try:
        
            if not file_path:
                tk.messagebox.showerror("Error", "No File Selected - Please Upload File")
                return
                    
            SaveFile(file_path)

        except:
            tk.messagebox.showerror("Error", "No File Uploaded - Please Upload File")
            return

    # create a label for the upload file section
    tk.Label(Body_Frame, text="UPLOAD FILE", font="Helvetica 14 bold").pack(pady=10)

    # create a button to choose a file
    ttk.Button(Body_Frame, text="Choose File", command=upload).pack(pady=10)

    # create a label to display the filename
    file = tk.Label(Body_Frame, text="No File Selected", font="Helvetica 10")
    file.pack()

    # create a button to go to the next step
    ttk.Button(Body_Frame, text="NEXT", command=next_func).pack(pady=10)

############################################################################
##                                                                        ##
##                                   MAIN                                 ##
##                                                                        ##
############################################################################

def Main():
    
    # This line uses list comprehension to destroy all the widgets inside the Body_Frame
    # This ensures that any previous widgets are removed before new ones are added
    [widget.destroy() for widget in Body_Frame.winfo_children()]
    
    global file_path
    file_path = None

    # call the Choose_File function
    chooseFile()

##############################################################################
##                                                                          ##
##                                Frame                                     ##
##                                                                          ##
##############################################################################

w = tk.Tk()
w.title("FILE NAME REDEAR")
w.geometry("%dx%d" % (w.winfo_screenwidth(), w.winfo_screenheight()))
w.state("zoomed")
w.iconbitmap(resource_path('assets\\icon.ico'))

global Header_Frame
Header_Frame = tk.Frame(w)
Header_Frame.pack(side = "top")

global header_img
header_img = ImageTk.PhotoImage(Image.open(resource_path("assets\\header.png")))
tk.Label(Header_Frame, image = header_img, width=w.winfo_screenwidth()).pack()

global Body_Frame
Body_Frame = tk.Frame(w)
Body_Frame.pack(expand = 1, fill = "both")

def open_link(event=None):
    webbrowser.open_new(r"https://www.linkedin.com/in/muhammad-abu-bakar-a32b9528a")

link_label = ttk.Label(w, text = "Designed By M.Abu-Bakar", font = "Helvetica 8")
link_label.pack(padx = 10, pady = 10, side="right")
link_label.configure(foreground="#114333", cursor="hand2")
link_label.bind("<Button-1>", open_link)

Main()

w.mainloop()