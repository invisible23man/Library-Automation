from Tkinter import *  
import tkFont
from PIL import Image, ImageTk
#import studentlogin

shome=Tk()
myFont= tkFont.Font(family = 'Helvetica', size = 12, weight = "bold")
myFont1= tkFont.Font(family = 'Comic Sans MS', size = 14, weight = "bold")
shome.attributes("-fullscreen", True)

screen_width = shome.winfo_screenwidth()
screen_height = shome.winfo_screenheight()

#############......Button function.......#########
def placeholder():
    print'a'
    
#############################################

#############.....MENU BAR.....##############
 
menubar = Menu(shome)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Admin Login", command=placeholder)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=shome.destroy)
menubar.add_cascade(label="Admin", menu=filemenu)


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="How-To", command=placeholder)
helpmenu.add_command(label="Contact Us", command=placeholder)
helpmenu.add_separator()
helpmenu.add_command(label="About", command=placeholder)
menubar.add_cascade(label="Help", menu=helpmenu)

reportmenu=Menu(menubar,tearoff=0)
reportmenu.add_command(label="Report", command=placeholder)
menubar.add_cascade(label="Report",menu=reportmenu)

shome.config(menu=menubar)

###############################################

####################  TOP FRAME  ###########################
logo_height=int(screen_height/4)
logo_width=int(logo_height*200/223)
topframe=Frame(shome,width=screen_width,height=logo_height,bg="red")
#frame1.place(x=220,y=0)
imglogo = Image.open("cet.jpg")
#print logo_width,logo_height
logoimg = imglogo.resize((logo_width, logo_height), Image.ANTIALIAS)
renderl = ImageTk.PhotoImage(logoimg)
imgl=Label(topframe,image=renderl)
imgl.place(x=0,y=0)

imghead = Image.open("head1.jpg")
#print logo_width,logo_height
headimg = imghead.resize((screen_width-logo_width, logo_height), Image.ANTIALIAS)
renderh = ImageTk.PhotoImage(headimg)
imgh=Label(topframe,image=renderh)
imgh.place(x=logo_width,y=0)

topframe.place(x=0,y=0)

#################################################################

###########   Bottom Frame    ############################
bgimg_height=int(screen_height-logo_height)
bgimg_width=int(screen_width)
bottomframe=Frame(shome,width=bgimg_width,height=bgimg_height,bg="white")
imgbg = Image.open("bg2.jpg")
#print logo_width,logo_height
bgimg = imgbg.resize((bgimg_width, bgimg_height), Image.ANTIALIAS)
renderbg = ImageTk.PhotoImage(bgimg)
imgbg=Label(bottomframe,image=renderbg)
imgbg.place(x=0,y=0)

bottomframe.place(x=0,y=logo_height)
#########################################################

###############   Left Pane    ##################

leftframe=Frame(shome,width=300,height=40)
LF = Label(leftframe,text="Student Login",bg='black',fg='white',font=myFont1)# height=2, width=30)
LF.pack()

leftframe.place(x=5,y=logo_height+5)
##################################################

'''
############    Bottom Most    #################

bgimgb_height=int(.25*logo_height)
bgimgb_width=int(screen_width)
bottombframe=Frame(shome,width=bgimgb_width,height=bgimgb_height,bg="white")
imgbgb = Image.open("bg.jpg")
#print logo_width,logo_height
bgimgb = imgbgb.resize((bgimgb_width, bgimgb_height), Image.ANTIALIAS)
renderbgb = ImageTk.PhotoImage(bgimgb)
imgbgb=Label(bottombframe,image=renderbgb)
#imgbgb.place(x=0,y=0)

T = Text(bottombframe)# height=2, width=30)
T.place(relx=.5,rely=.5)
T.insert(END, "College Of Engineering Trivandrum")

bottombframe.place(x=0,y=screen_height-.35*logo_height)
#################################################
'''
##################       button       ########################


buttonsize=100
                
scanID = Button(bottomframe, text='Scan Student ID Card', font=myFont, relief='raised',command=placeholder, bg='bisque2')
#item = Tkinter.Button(root,
 ##               text=color,
   #             width=20,
    #            height=10,
     #           relief='raised',
      #          borderwidth=5,
       #         bg=color
        #    )

originalid = Image.open('barcodescan.jpg')
originalid = originalid.resize((buttonsize,buttonsize), Image.ANTIALIAS)
ph_imid = ImageTk.PhotoImage(originalid)

scanID.config(image=ph_imid)
#scanButton.grid(row=0,column=2)
scanID.place(relx=0.3, rely=0.5, anchor=CENTER)




scanface = Button(bottomframe, text='Scan face', font=myFont, relief='raised',command=placeholder, bg='bisque2')


originalface = Image.open('facerecog.jpg')
originalface = originalface.resize((buttonsize,buttonsize), Image.ANTIALIAS)
ph_imface = ImageTk.PhotoImage(originalface)

scanface.config(image=ph_imface)
#scanButton.grid(row=0,column=2)
scanface.place(relx=0.45, rely=0.5, anchor=CENTER)



scanpass = Button(bottomframe, text='Scan pass', font=myFont, relief='raised',command=placeholder, bg='bisque2')


originalpass = Image.open('pass.jpg')
originalpass = originalpass.resize((buttonsize,buttonsize), Image.ANTIALIAS)
ph_impass = ImageTk.PhotoImage(originalpass)

scanpass.config(image=ph_impass)
#scanButton.grid(row=0,column=2)
scanpass.place(relx=0.6, rely=0.5, anchor=CENTER)

################################################


shome.mainloop()
