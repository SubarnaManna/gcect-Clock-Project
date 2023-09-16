# # App = 
# import customtkinter as ctk

# from tkinter import *
# # import customtkinter as ctk

# root = Tk()

# root.title("none")
# root.geometry("400x200")

# img=PhotoImage(file="Tests/Layouts/Img/gcect_logo.png")

# lab = Label(root,image=img)
# root.mainloop()

# ctk.CTkLabel(root, 
#   text = 'This is a label', 
#   text_font =('Verdana', 17)).pack(side = LEFT, pady = 11)

# img = PhotoImage(file="./gcect_logo.png")
# ctk.CTkButton(root, image = img).pack(side = LEFT)

# root.mainloop()

# window = ctk.CTk()
    
# button_image = ctk.CTkImage(Image.open("gcect_logo.png"), size=(26, 26))
    
# image_button = ctk.CTkButton(master=window, text="Text will be gone if you don't use compound attribute",image=button_image)
# image_button.pack()
    
# window.mainloop()



from tkinter import *
from PIL import Image, ImageTk

root = Tk()

path1 = "M:\\GCECT\\Clock Project\\Clock_Software\\Tests\\Layout_Tests\\logo.png"
path2 = "M:/GCECT/Clock Project/Clock_Software/Tests/Layout_Tests/logo.png"

# image = Image.open('Tests/Layouts_Tests/logo.png')
# image = Image.open(path1)
# image = Image.open(path2)
# image = Image.open('logo.png')

# display = ImageTk.PhotoImage(Image.open(image))

# label = Label(root, image=display)
# label.image = display
# label.pack()


# Create a photoimage object of the image in the path
# image1 = Image.open("<path/image_name>")
image1 = Image.open(path2)
test = ImageTk.PhotoImage(image1)

label1 = Label(image=test)
label1.image = test

# Position image
label1.place(x=0, y=0)

root.mainloop()