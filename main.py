# Import the following module
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os
from time import sleep

import pyautogui

from pynput import keyboard

from tkinter import *




i = 0
listimg = []
email = ''
password = ''
listmail = []
lber = None






def screenshot():
    global i
    global listimg
    myScreenshot = pyautogui.screenshot()
    url = 'C:\\Users\\DatPham\\Desktop\\screenshot_' + str(i) + '.png'
    listimg += [url]

    print(url)
    myScreenshot.save(url)
    i = i + 1

def sendmail(email,password,listmailto):
    global listimg

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()

    smtp.login(email, password)

    def message(subject="Python Notification",
                text="", img=None,
                attachment=None):
        
        # build message contents
        msg = MIMEMultipart()
        
        # Add Subject
        msg['Subject'] = subject
        
        # Add text contents
        msg.attach(MIMEText(text))

        # Check if we have anything
        # given in the img parameter
        if img is not None:
            
            # Check whether we have the lists of images or not!
            if type(img) is not list:
                
                # if it isn't a list, make it one
                img = [img]

            # Now iterate through our list
            for one_img in img:
                
                # read the image binary data
                img_data = open(one_img, 'rb').read()
                # Attach the image data to MIMEMultipart
                # using MIMEImage, we add the given filename use os.basename
                msg.attach(MIMEImage(img_data, name=os.path.basename(one_img)))

        # We do the same for
        # attachments as we did for images
        if attachment is not None:
            
            # Check whether we have the
            # lists of attachments or not!
            if type(attachment) is not list:
                
                # if it isn't a list, make it one
                attachment = [attachment]

            for one_attachment in attachment:

                with open(one_attachment, 'rb') as f:
                    
                    # Read in the attachment
                    # using MIMEApplication
                    file = MIMEApplication(
                        f.read(),
                        name=os.path.basename(one_attachment)
                    )
                file['Content-Disposition'] = f'attachment;\
                filename="{os.path.basename(one_attachment)}"'
                
                # At last, Add the attachment to our message object
                msg.attach(file)
        return msg


    # Call the message function
    msg = message("Good!", "Hi there!", listimg)

    # Make a list of emails, where you wanna send mail
    # to = listmailto
    # to = ["linhngam001@gmail.com","XYZ@gmail.com", "insaaf@gmail.com"]


    # Provide some data to the sendmail function!
    smtp.sendmail(from_addr=email,
                to_addrs=listmailto, msg=msg.as_string())

    # Finally, don't forget to close the connection
    smtp.quit()


def on_press(key):
    global email
    global password
    global listmail
    global i
    if key == keyboard.Key.esc:
        return False  # stop listener
    if key == keyboard.Key.insert:
        screenshot()
        
    if key == keyboard.Key.delete:
        print("Sending...")
        if isinstance(listmail,list) == False:
            listmail = [listmail]
        # sendmail("vandatpro003@gmail.com", "accclone03",["linhngam001@gmail.com"])
        sendmail(str(email),str(password),listmail)
        i = 0
        print("Success !!!")





def x():
    print(val1.get(),val2.get(),val21.get())
    global email
    global password
    global listmail
    global i
    global lber
    if lber:
        lber.destroy()        
        lber = None
    
    email = val1.get()
    password = val2.get()
    listmail = val21.get()

    try:
        listener = keyboard.Listener(on_press=on_press)
        listener.start()  # start to listen on a separate thread
        listener.join()  # remove if main thread is polling self.keys
    except Exception as e:
        lber = Label(erF,text = e)
        lber.pack(ipadx=20,ipady=20,side='top')
        i = 0

master = Tk()
f1 = Frame(master)
f2 = Frame(master)
f21 = Frame(master)
f3 = Frame(master)
erF = Frame(master)

f1.pack()
f2.pack()
f21.pack()
erF.pack()
f3.pack()
Label(f1,text = 'Email : ').pack(ipadx=20,ipady=20,side='left')
val1 = Entry(f1)
val1.pack(padx=20,pady=20,side='left')
Label(f2,text = 'Password : ').pack(ipadx=20,ipady=20,side='left')
val2 = Entry(f2)
val2.pack(padx=20,pady=20,side='left')
Label(f21,text = 'Destination : ').pack(ipadx=20,ipady=20,side='left')
val21 = Entry(f21)
val21.pack(padx=20,pady=20,side='left')
b1 = Button(f3,text = 'Start', command = x)
b1.pack(padx=20,side='bottom',pady=20)

mainloop()


