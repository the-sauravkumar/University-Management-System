from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox
import tkinter.font as font

global Submit_btn
global Submit_btn_button
global Refresh_btn_button
global final_choice

root = Tk()
root.title("Image Verification Captcha")
root.geometry("613x800")
root.configure(bg="white")

# Defining variables for bridge module
# =========================================

notaBot = IntVar()
sub_btn = IntVar()
bridgeVar1 = IntVar()
bridgeVar2 = IntVar()
bridgeVar3 = IntVar()
bridgeVar4 = IntVar()
roadVar1 = IntVar()
roadVar2 = IntVar()
roadVar3 = IntVar()
roadVar4 = IntVar()
roadVar5 = IntVar()

# --------------------------------------------------------------------------------------------------


# Defining variables for cat module
# ==========================================

catVar1 = IntVar()
catVar2 = IntVar()
catVar3 = IntVar()
catVar4 = IntVar()
calfVar1 = IntVar()
calfVar2 = IntVar()
dogVar1 = IntVar()
dogVar2 = IntVar()
dogVar3 = IntVar()

# ===========================================

# FUNCTION TO VERIFY CORRECTNESS OF BUTTON SELECTED IN BRIDGE MODULE

def displaybridge():
    
    if (bridgeVar1.get() == 1) & (bridgeVar2.get() == 1) & (bridgeVar3.get() == 1) & (bridgeVar4.get() == 1) & (roadVar1.get() == 0) & (
            roadVar2.get() == 0) & (roadVar3.get() == 0) & (roadVar4.get() == 0) & (roadVar5.get() == 0)|((catVar1.get() == 1) & (catVar2.get() == 1) & (catVar3.get() == 1) & (catVar4.get() == 1) & (dogVar1.get() == 0) & (dogVar2.get() == 0) & (dogVar3.get() == 0) & (calfVar1.get() == 0) & (calfVar2.get() == 0)):
        
        
        tkinter.messagebox.showinfo(title="Captcha", message="Verified!")
        
# -=-=-=-=-=-=-=-=-=-=-=-=-=- IF BLOCK ENDS -=-=-=-=-=-=-=-=-=-=

    elif ((bridgeVar1.get() == 0) | (bridgeVar2.get() == 0) | (bridgeVar3.get() == 0) | (bridgeVar4.get() == 0)  | (catVar1.get() == 0) | (catVar2.get() == 0) | (catVar3.get() == 0) | (catVar4.get() == 0))& ((
            roadVar1.get() == 0) & (roadVar2.get() == 0) & (roadVar3.get() == 0) & (roadVar4.get() == 0) & (roadVar5.get() == 0) & ((calfVar1.get() == 0) & (calfVar2.get() == 0) & (dogVar1.get() == 0) & (dogVar2.get() == 0)& (dogVar3.get() == 0))):
        
        tkinter.messagebox.showinfo(
            title="Caution", message="Please select remaining images")
        
# -=-=-=-=-=-=-=-=-=-=-=-=-=- ELIF BLOCK ENDS -=-=-=-=-=-=-=-=-=-=
    else:
        
        tkinter.messagebox.showinfo(title="Captcha", message="Try Again")
        # For Brige Module
        # -------------------------------------------
        
        bridgeVar1.set(0)
        bridge1_label_chk_btn.configure(bg="white")
        bridgeVar2.set(0)
        bridge2_label_chk_btn.configure(bg="white")
        bridgeVar3.set(0)
        bridge3_label_chk_btn.configure(bg="white")
        bridgeVar4.set(0)
        bridge4_label_chk_btn.configure(bg="white")
        roadVar1.set(0)
        road1_label_chk_btn.configure(bg="white")
        roadVar2.set(0)
        road2_label_chk_btn.configure(bg="white")
        roadVar3.set(0)
        road3_label_chk_btn.configure(bg="white")
        roadVar4.set(0)
        road4_label_chk_btn.configure(bg="white")
        roadVar5.set(0)
        road5_label_chk_btn.configure(bg="white")
        
        # For Animal Module
        # ------------------------------------
        
        catVar1.set(0)
        cat1_label_chk_btn.configure(bg="white")
        catVar2.set(0)
        cat2_label_chk_btn.configure(bg="white")
        catVar3.set(0)
        cat3_label_chk_btn.configure(bg="white")
        catVar4.set(0)
        cat4_label_chk_btn.configure(bg="white")
        calfVar1.set(0)
        calf1_label_chk_btn.configure(bg="white")
        calfVar2.set(0)
        calf2_label_chk_btn.configure(bg="white")
        dogVar1.set(0)
        dog1_label_chk_btn.configure(bg="white")
        dogVar2.set(0)
        dog2_label_chk_btn.configure(bg="white")
        dogVar3.set(0)
        dog3_label_chk_btn.configure(bg="white")
    
    # -=-=-=-=-=-=-=-=-=-=-=-=-=- ELSE BLOCK ENDS -=-=-=-=-=-=-=-=-=-=

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------

# FUNCTION TO CHECK CORRECTNESS OF BUTTON SELECTED IN ANIMALS MODULE

def displaycat():
    
    if (catVar1.get() == 1) & (catVar2.get() == 1) & (catVar3.get() == 1) & (catVar4.get() == 1) & (dogVar1.get() == 0) & (dogVar2.get() == 0) & (dogVar3.get() == 0) & (calfVar1.get() == 0) & (calfVar2.get() == 0):
        
        tkinter.messagebox.showinfo(title="Captcha", message="Verified!")
    
# -=-=-=-=-=-=-=-=-=-=-=-=-=- IF BLOCK ENDS -=-=-=-=-=-=-=-=-=-=
        
        
    elif ((catVar1.get() == 0) | (catVar2.get() == 0) | (catVar3.get() == 0) | (catVar4.get() == 0)) & ((
                calfVar1.get() == 0) & (calfVar2.get() == 0) & (dogVar1.get() == 0) & (dogVar2.get() == 0)):
        
        
        tkinter.messagebox.showinfo(
            title="Caution", message="Please select remaining images")
        
    # -=-=-=-=-=-=-=-=-=-=-=-=-=- ELIF BLOCK ENDS -=-=-=-=-=-=-=-=-=-=
        
        

    else:
        tkinter.messagebox.showinfo(title="Captcha", message="Try Again")
        
        
      # -=-=-=-=-=-=-=-=-=-=-=-=-=- ELSE BLOCK ENDS -=-=-=-=-=-=-=-=-=-=
      
# Function to trigger displayCat()
def itsCatTime():
    if(Refresh_btn_button == 1):
        displaycat()
# ------------------------------------------------------------------------------------------------------------


        # ----------------------------------------------------- Submit Button --------------------------------------
#   Including the image of submit button
submit = Image.open("D:/Projects/Projects/Human Verification Captcha/SUBMIT.png")
submit_photo1 = ImageTk.PhotoImage(submit)

# Resizing the btn

resized = submit.resize((140, 80), Image.ANTIALIAS)
submit = ImageTk.PhotoImage(file="D:/Projects/Projects/Human Verification Captcha/SUBMIT.png")
submit_pic1 = ImageTk.PhotoImage(resized)

# ---------------------------------------------------------------------------------------------------------


# ------------------------------ FUNCTION OF SUBMIT BUTTON -------------------------------

Submit_btn_button = Button(root, image=submit_pic1, borderwidth = 0, bg = "white", command=lambda:(displaybridge(), itsCatTime()))

# ------------------------------------- REFRESH BUTTON ---------------------------------------------------

#   Including the Refresh of submit button

#refresh = Image.open("D:/refresh.png")
#refresh_photo1 = ImageTk.PhotoImage(refresh)

# Resizing the btn

#resized = refresh.resize((120, 180), Image.ANTIALIAS)
#refresh = ImageTk.PhotoImage(file="D:/refresh.png")
#refresh_pic1 = ImageTk.PhotoImage(resized)

# --------------------------------------------------------------------------------------------------------


Refresh_btn_button = Button(root, text="Refresh")


def bdgVar1():
    return bridgeVar1.set(1)


def bdgVar2():
    return bridgeVar2.set(1)


def bdgVar3():
    return bridgeVar3.set(1)


def bdgVar4():
    return bridgeVar4.set(1)


def rdgVar1():
    return roadVar1.set(1)


def rdgVar2():
    return roadVar2.set(1)


def rdgVar3():
    return roadVar3.set(1)


def rdgVar4():
    return roadVar4.set(1)


def rdgVar5():
    return roadVar5.set(1)


def enable():
    if (notaBot.get() == 0):
        chk_btn.config(root, state=DISABLED)
    elif (notaBot.get() == 1):
        Submit_btn.config(root, state=ACTIVE)


# ======================================================================
# ======================================================================


def clicked_bridge1():
    bridge1_label_chk_btn.configure(bg="yellow")


def clicked_bridge2():
    bridge2_label_chk_btn.configure(bg="yellow")


def clicked_bridge3():
    bridge3_label_chk_btn.configure(bg="yellow")


def clicked_bridge4():
    bridge4_label_chk_btn.configure(bg="yellow")


def clicked_road1():
    road1_label_chk_btn.configure(bg="black")


def clicked_road2():
    road2_label_chk_btn.configure(bg="black")


def clicked_road3():
    road3_label_chk_btn.configure(bg="black")


def clicked_road4():
    road4_label_chk_btn.configure(bg="black")


def clicked_road5():
    road5_label_chk_btn.configure(bg="black")


""" First Module for Bridge Verification
   Grid and Label has been used to achieve recaptcha like interface"""
   


#   Including the images

bridge1 = Image.open(
    "D:/Projects/Projects/Human Verification Captcha/IMAGES/nature/bridge1.jpeg")
photo1 = ImageTk.PhotoImage(bridge1)

# Resizing

resized = bridge1.resize((200, 200), Image.ANTIALIAS)
bridge1 = ImageTk.PhotoImage(
    file="D:/Projects/Projects/Human Verification Captcha/IMAGES/nature/bridge1.jpeg")
new_pic1 = ImageTk.PhotoImage(resized)


#   Including the images

bridge2 = Image.open(
    "D:/Projects/Projects/Human Verification Captcha/IMAGES/nature/bridge2.jpg")
photo2 = ImageTk.PhotoImage(bridge2)
# Resizing

resized = bridge2.resize((200, 200), Image.ANTIALIAS)
bridge2 = ImageTk.PhotoImage(
    file="D:/Projects/Projects/Human Verification Captcha/IMAGES/nature/bridge2.jpg")
new_pic2 = ImageTk.PhotoImage(resized)

#   Including the images

bridge3 = Image.open(
    "D:/Projects/Projects/Human Verification Captcha/IMAGES/nature/bridge3.jpg")
photo3 = ImageTk.PhotoImage(bridge3)

# Resizing

resized = bridge3.resize((200, 200), Image.ANTIALIAS)
bridge3 = ImageTk.PhotoImage(
    file="D:/Projects/Projects/Human Verification Captcha/IMAGES/nature/bridge3.jpg")
new_pic3 = ImageTk.PhotoImage(resized)


#  Including the images

bridge4 = Image.open(
    "D:/Projects/Projects/Human Verification Captcha/IMAGES/nature/bridge4.jpeg")
photo4 = ImageTk.PhotoImage(bridge4)

# Resizing

resized = bridge4.resize((200, 200), Image.ANTIALIAS)
bridge4 = ImageTk.PhotoImage(
    file="D:/Projects/Projects/Human Verification Captcha/IMAGES/nature/bridge4.jpeg")
new_pic4 = ImageTk.PhotoImage(resized)

########################################################

"""Pictures of Roads are included using below command 
    for bridge verification module"""

#   Including the road images

road1 = Image.open(
    "D:/Projects/Projects/Human Verification Captcha/IMAGES/nature/road1.jpeg")
road_photo1 = ImageTk.PhotoImage(road1)

# Resizing

resized = road1.resize((200, 200), Image.ANTIALIAS)
road1 = ImageTk.PhotoImage(
    file="D:/Projects/Projects/Human Verification Captcha/IMAGES/nature/road1.jpeg")
road_pic1 = ImageTk.PhotoImage(resized)

#   Including the road images

road2 = Image.open(
    "D:/Projects/Projects/Human Verification Captcha/IMAGES/nature/road2.jpeg")
road_photo2 = ImageTk.PhotoImage(road2)

# Resizing

resized = road2.resize((200, 200), Image.ANTIALIAS)
road2 = ImageTk.PhotoImage(
    file="D:/Projects/Projects/Human Verification Captcha/IMAGES/nature/road2.jpeg")
road_pic2 = ImageTk.PhotoImage(resized)


#   Including the road images

road3 = Image.open(
    "D:/Projects/Projects/Human Verification Captcha/IMAGES/nature/road3.jpg")
road_photo3 = ImageTk.PhotoImage(road3)

# Resizing

resized = road3.resize((200, 200), Image.ANTIALIAS)
road3 = ImageTk.PhotoImage(
    file="D:/Projects/Projects/Human Verification Captcha/IMAGES/nature/road3.jpg")
road_pic3 = ImageTk.PhotoImage(resized)


#   Including the road images

road4 = Image.open(
    "D:/Projects/Projects/Human Verification Captcha/IMAGES/nature/road4.jpg")
road_photo4 = ImageTk.PhotoImage(road4)

# Resizing

resized = road4.resize((200, 200), Image.ANTIALIAS)
road4 = ImageTk.PhotoImage(
    file="D:/Projects/Projects/Human Verification Captcha/IMAGES/nature/road4.jpg")
road_pic4 = ImageTk.PhotoImage(resized)

#   Including the road images

road5 = Image.open(
    "D:/Projects/Projects/Human Verification Captcha/IMAGES/nature/road5.jpg")
road_photo5 = ImageTk.PhotoImage(road5)

# Resizing

resized = road5.resize((200, 200), Image.ANTIALIAS)
road5 = ImageTk.PhotoImage(
    file="D:/Projects/Projects/Human Verification Captcha/IMAGES/nature/road5.jpg")
road_pic5 = ImageTk.PhotoImage(resized)


# --------------------------------------------------------------------------------------------------------

# ================================================================================
# ==========================================================================================

# using Buttons for Bridge Module

bridge1_label_chk_btn = Button(
    root, image=new_pic1, command=lambda: (bdgVar1(), clicked_bridge1()))
bridge1_label_chk_btn.grid_forget()


road1_label_chk_btn = Button(
    root, image=road_pic1, command=lambda: (rdgVar1(), clicked_road1()))
road1_label_chk_btn.grid_forget()


bridge2_label_chk_btn = Button(
    root, image=new_pic2, command=lambda: (bdgVar2(), clicked_bridge2()))
bridge2_label_chk_btn.grid_forget()


road2_label_chk_btn = Button(
    root, image=road_pic2, command=lambda: (rdgVar2(), clicked_road2()))
road2_label_chk_btn.grid_forget()


bridge3_label_chk_btn = Button(
    root, image=new_pic3, command=lambda: (bdgVar3(), clicked_bridge3()))
bridge3_label_chk_btn.grid_forget()


road3_label_chk_btn = Button(
    root, image=road_pic3, command=lambda: (rdgVar3(), clicked_road3()))
road3_label_chk_btn.grid_forget()


bridge4_label_chk_btn = Button(
    root, image=new_pic4, command=lambda: (bdgVar4(), clicked_bridge4()))
bridge4_label_chk_btn.grid_forget()


road4_label_chk_btn = Button(
    root, image=road_pic4, command=lambda: (rdgVar4(), clicked_road4()))
road4_label_chk_btn.grid_forget()


road5_label_chk_btn = Button(
    root, image=road_pic5, command=lambda: (rdgVar5(), clicked_road5()))
road5_label_chk_btn.grid_forget()


def key1():
    if (notaBot.get() == 1):

        tkinter.messagebox.showinfo(
            title="captcha", message="Select all the bridges")
        bridge1_label_chk_btn.grid(row=0, column=0)
        bridge2_label_chk_btn.grid(row=0, column=2)
        bridge3_label_chk_btn.grid(row=1, column=1)
        bridge4_label_chk_btn.grid(row=2, column=0)
        road1_label_chk_btn.grid(row=0, column=1)
        road2_label_chk_btn.grid(row=1, column=0)
        road3_label_chk_btn.grid(row=1, column=2)
        road4_label_chk_btn.grid(row=2, column=1)
        road5_label_chk_btn.grid(row=2, column=2)
        Submit_btn_button.grid(row=4, column=1)
        
        Refresh_btn_button.grid(row=4, column=0)

    elif (notaBot.get() == 0):

        bridge1_label_chk_btn.grid_forget()
        bridge2_label_chk_btn.grid_forget()
        bridge3_label_chk_btn.grid_forget()
        bridge4_label_chk_btn.grid_forget()
        road1_label_chk_btn.grid_forget()
        road2_label_chk_btn.grid_forget()
        road3_label_chk_btn.grid_forget()
        road4_label_chk_btn.grid_forget()
        road5_label_chk_btn.grid_forget()
        Submit_btn_button.grid_forget()
        Refresh_btn_button.grid_forget()


#  ------------------------------------------------------------------
# =======================================================================
# ========================================= MODULE 2 =========================
# =================================================================================
# ===================================================================================





def ctVar1():
    return catVar1.set(1)


def ctVar2():
    return catVar2.set(1)


def ctVar3():
    return catVar3.set(1)


def ctVar4():
    return catVar4.set(1)


def cfVar1():
    return calfVar1.set(1)


def cfVar2():
    return calfVar2.set(1)


def doVar1():
    return dogVar1.set(1)


def doVar2():
    return dogVar2.set(1)


def doVar3():
    return dogVar3.set(1)


def clicked_dog1():
    dog1_label_chk_btn.configure(bg="black")


def clicked_dog2():
    dog2_label_chk_btn.configure(bg="black")


def clicked_dog3():
    dog3_label_chk_btn.configure(bg="black")


def clicked_calf1():
     calf1_label_chk_btn.configure(bg="black")


def clicked_calf2():
    calf2_label_chk_btn.configure(bg="black")


def clicked_cat1():
    cat1_label_chk_btn.configure(bg="yellow")


def clicked_cat2():
    cat2_label_chk_btn.configure(bg="yellow")


def clicked_cat3():
    cat3_label_chk_btn.configure(bg="yellow")


def clicked_cat4():
    cat4_label_chk_btn.configure(bg="yellow")

# =======================================================================================
# ========================================================================================
# =========================================================================================
# ==========================================================================================


""" First Module for Bridge Verification
   Grid and Label has been used to achieve recaptcha like interface"""


def display():
    if (bridgeVar1.get() == 1) & (bridgeVar2.get() == 1) & (bridgeVar3.get() == 1) & (bridgeVar4.get() == 1) & (roadVar1.get() == 0) & (
            roadVar2.get() == 0) & (roadVar3.get() == 0) & (roadVar4.get() == 0) & (roadVar5.get() == 0):
        tkinter.messagebox.showinfo(title="Captcha", message="Verified!")

    elif ((bridgeVar1.get() == 0) | (bridgeVar2.get() == 0) | (bridgeVar3.get() == 0) | (bridgeVar4.get() == 0)) & ((
            roadVar2.get() == 0) & (roadVar3.get() == 0) & (roadVar4.get() == 0) & (roadVar5.get() == 0)):
        tkinter.messagebox.showinfo(
            title="Caution", message="Please select remaining images")

    else:
        tkinter.messagebox.showinfo(title="Captcha", message="Try Again")


# ======================================
#   Including the images of Animals
# ======================================

cat1 = Image.open(
    "D:/Projects/Projects/Human Verification Captcha/IMAGES/animal/cat1.jpeg")
cat_photo1 = ImageTk.PhotoImage(cat1)

# Resizing

resized = cat1.resize((200, 200), Image.ANTIALIAS)
cat1 = ImageTk.PhotoImage(
    file="D:/Projects/Projects/Human Verification Captcha/IMAGES/animal/cat1.jpeg")
cat_pic1 = ImageTk.PhotoImage(resized)

#   Including the images

cat2 = Image.open(
    "D:/Projects/Projects/Human Verification Captcha/IMAGES/animal/cat2.jpeg")
cat_photo2 = ImageTk.PhotoImage(cat2)

# Resizing

resized = cat2.resize((200, 200), Image.ANTIALIAS)
cat2 = ImageTk.PhotoImage(
    file="D:/Projects/Projects/Human Verification Captcha/IMAGES/animal/cat2.jpeg")
cat_pic2 = ImageTk.PhotoImage(resized)

#   Including the images

cat3 = Image.open(
    "D:/Projects/Projects/Human Verification Captcha/IMAGES/animal/cat3.jpg")
cat_photo3 = ImageTk.PhotoImage(cat3)

# Resizing

resized = cat3.resize((200, 200), Image.ANTIALIAS)
cat3 = ImageTk.PhotoImage(
    file="D:/Projects/Projects/Human Verification Captcha/IMAGES/animal/cat3.jpg")
cat_pic3 = ImageTk.PhotoImage(resized)


#  Including the images

cat4 = Image.open(
    "D:/Projects/Projects/Human Verification Captcha/IMAGES/animal/cat4.jpeg")
cat_photo4 = ImageTk.PhotoImage(cat4)

# Resizing

resized = cat4.resize((200, 200), Image.ANTIALIAS)
cat4 = ImageTk.PhotoImage(
    file="D:/Projects/Projects/Human Verification Captcha/IMAGES/animal/cat4.jpeg")
cat_pic4 = ImageTk.PhotoImage(resized)

########################################################

"""Pictures of Other animals are included using below command 
    for verification module"""

#   Including the animals images

calf1 = Image.open(
    "D:/Projects/Projects/Human Verification Captcha/IMAGES/animal/calf1.jpeg")
calf_photo1 = ImageTk.PhotoImage(calf1)

# Resizing

resized = calf1.resize((200, 200), Image.ANTIALIAS)
calf1 = ImageTk.PhotoImage(
    file="D:/Projects/Projects/Human Verification Captcha/IMAGES/animal/calf1.jpeg")
calf_pic1 = ImageTk.PhotoImage(resized)

#   Including the animals images

calf2 = Image.open(
    "D:/Projects/Projects/Human Verification Captcha/IMAGES/animal/calf2.jpeg")
calf_photo2 = ImageTk.PhotoImage(calf2)

# Resizing

resized = calf2.resize((200, 200), Image.ANTIALIAS)
calf2 = ImageTk.PhotoImage(
    file="D:/Projects/Projects/Human Verification Captcha/IMAGES/animal/calf2.jpeg")
calf_pic2 = ImageTk.PhotoImage(resized)


#   Including the animals images

dog1 = Image.open(
    "D:/Projects/Projects/Human Verification Captcha/IMAGES/animal/dog1.jpeg")
dog_photo1 = ImageTk.PhotoImage(dog1)

# Resizing

resized = dog1.resize((200, 200), Image.ANTIALIAS)
dog1 = ImageTk.PhotoImage(
    file="D:/Projects/Projects/Human Verification Captcha/IMAGES/animal/dog1.jpeg")
dog_pic1 = ImageTk.PhotoImage(resized)


#   Including the animals images

dog2 = Image.open(
    "D:/Projects/Projects/Human Verification Captcha/IMAGES/animal/dog2.jpeg")
dog_photo2 = ImageTk.PhotoImage(dog2)

# Resizing

resized = dog2.resize((200, 200), Image.ANTIALIAS)
dog2 = ImageTk.PhotoImage(
    file="D:/Projects/Projects/Human Verification Captcha/IMAGES/animal/dog2.jpeg")
dog_pic2 = ImageTk.PhotoImage(resized)

#   Including the animals images

dog3 = Image.open(
    "D:/Projects/Projects/Human Verification Captcha/IMAGES/animal/dog3.jpeg")
dog_photo3 = ImageTk.PhotoImage(dog3)

# Resizing

resized = dog3.resize((200, 200), Image.ANTIALIAS)
dog3 = ImageTk.PhotoImage(
    file="D:/Projects/Projects/Human Verification Captcha/IMAGES/animal/dog3.jpeg")
dog_pic3 = ImageTk.PhotoImage(resized)

# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================

# using Buttons for Animal Module


cat1_label_chk_btn = Button(
    root, image=cat_pic1, command=lambda: (ctVar1(), clicked_cat1()))
cat1_label_chk_btn.grid_forget()


calf1_label_chk_btn = Button(
    root, image=calf_pic1, command=lambda: (cfVar1(), clicked_calf1()))
calf1_label_chk_btn.grid_forget()


cat2_label_chk_btn = Button(
    root, image=cat_pic2, command=lambda: (ctVar2(), clicked_cat2()))
cat2_label_chk_btn.grid_forget()


cat3_label_chk_btn = Button(
    root, image=cat_pic3, command=lambda: (ctVar3(), clicked_cat3()))
cat3_label_chk_btn.grid_forget()


dog1_label_chk_btn = Button(
    root, image=dog_pic1, command=lambda: (doVar1(), clicked_dog1()))
dog1_label_chk_btn.grid_forget()


calf2_label_chk_btn = Button(
    root, image=calf_pic2, command=lambda: (cfVar2(), clicked_calf2()))
calf2_label_chk_btn.grid_forget()


cat4_label_chk_btn = Button(
    root, image=cat_pic4, command=lambda: (ctVar4(), clicked_cat4()))
cat4_label_chk_btn.grid_forget()


dog2_label_chk_btn = Button(
    root, image=dog_pic2, command=lambda: (doVar2(), clicked_dog2()))
dog2_label_chk_btn.grid_forget()


dog3_label_chk_btn = Button(
    root, image=dog_pic3, command=lambda: (doVar3(), clicked_dog3()))
dog3_label_chk_btn.grid_forget()


# ====================================================================================================
# ====================================================================================================
# ====================================================================================================
# ====================================================================================================
# ====================================================================================================
# ====================================================================================================

def key2():
    if (notaBot.get() == 1):

        tkinter.messagebox.showinfo(
            title="captcha", message="Select all the cats")
        cat1_label_chk_btn.grid(row=0, column=0)
        calf1_label_chk_btn.grid(row=0, column=2)
        cat2_label_chk_btn.grid(row=1, column=1)
        cat3_label_chk_btn.grid(row=2, column=0)
        dog1_label_chk_btn.grid(row=0, column=1)
        calf2_label_chk_btn.grid(row=1, column=0)
        cat4_label_chk_btn.grid(row=1, column=2)
        dog2_label_chk_btn.grid(row=2, column=1)
        dog3_label_chk_btn.grid(row=2, column=2)
        Submit_btn_button.grid(row=4, column=1)
        Refresh_btn_button.grid(row=4, column=0)

    elif (notaBot.get() == 0):

        cat1_label_chk_btn.grid_forget()
        calf1_label_chk_btn.grid_forget()
        cat2_label_chk_btn.grid_forget()
        cat3_label_chk_btn.grid_forget()
        dog1_label_chk_btn.grid_forget()
        calf2_label_chk_btn.grid_forget()
        cat4_label_chk_btn.grid_forget()
        dog2_label_chk_btn.grid_forget()
        dog3_label_chk_btn.grid_forget()
        Submit_btn_button.grid_forget()
        Submit_btn_button.grid_forget()
        Refresh_btn_button.grid_forget()


# -------------------------- 'NOT A ROBOT' BUTTON --------------------------------

chk_btn = Checkbutton(root, text="I am not robot", activebackground="black", activeforeground="white",
                      bg="lightblue", fg = "Navy Blue", bd = 12, variable=notaBot, onvalue=1, offvalue=0, command=key1)
chk_btn.grid(row = 4, column = 2)

chk_btn['font'] = font.Font(family='Product Sans', size = 12)
# ----------------------------------------------------------------------------


# --------------------------------- REFRESH ----------------------------------

Refresh_btn_button = Button(root, command=key2, text = "Refresh", borderwidth=7, bg = "indigo", fg = "white")
Refresh_btn_button['font'] = font.Font(family = "Product Sans")


root.mainloop()
