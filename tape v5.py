from tkinter import *
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo
import tkinter.ttk as ttk
import time as t
from threading import *
from pymem import *
import multiprocessing
import os
from zipfile import *

def wait(time):
    for k in range(time):
        t.sleep(0.001)
        frame.update()

minecraft = multiprocessing.Process()
mcchildprocesses = multiprocessing.active_children()

print('Starting...')
print('Tape v4 Client developed by Pythonify')
print('Ready to begin')

def pause(secs):
    init_time = time()
    while time() < init_time+secs: pass

win = Tk()










win.geometry("700x500")

frame = Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

win.title('Tape Client')

win.resizable(False,False)

try:
    img = ImageTk.PhotoImage(Image.open('requiredfiles\\Tape v5.png'))
except:
    showinfo('Error', message='There was an error importing a file. If the zip has already been downloaded, it will be extracted automatically after you close this window. If not, it should be downloaded after you close this window.')
    try:
        with ZipFile('requiredfiles.zip') as requiredfileszip:
            requiredfileszip.extractall()
    except:
        showinfo('Error', message='There was an error exctracting the files. It is likely the files haven\'t been downloaded yet. They should be downloaded and extracted automatically. Tape Client should stop responding - Don\'t worry, this is meant to happen.')
        import requests
        requiredfileszip = 'https://github.com/PythonifyWasTaken/tape-resources/blob/main/requiredfiles.zip?raw=true'
        r = requests.get(requiredfileszip)
        with open("requiredfiles.zip",'wb') as f:
            f.write(r.content)
            try:
                requiredfileszip.extractall()
            except:
                with ZipFile('requiredfiles.zip') as rqflzip:
                    rqflzip.extractall()
                showinfo('Success', message='Files have been successfully extracted. You may now close this window and run Tape Client again.')
tape = Label(frame, image=img)
tape.place(relx=0.5, rely=0.4, anchor='center')


dots_label = Label(frame, text='   ', font=('Arial', 34))
dots_label.place()

loadingstatus = Label(frame, text='Loading...', font=('Segoe', 14))
frame.place()
frame.update()
t.sleep(1)
frame.place()
frame.update()
def loading_animation():
    frame.update()
    t.sleep(1)
    frame.update()
    loadingstatus.place(relx=0.5, rely=0.56, anchor='center')
    loadingstatus.config(text='Loading...')
    dots_label = ttk.Label(frame, text='', font=('Arial', 34))
    dots_label.place(relx=0.5, rely=0.65, anchor='center')
    frame.update()
    for u in range(4):
        dots_label.config(text='   ')
        frame.update()
        t.sleep(0.3)
        
        dots_label.config(text='.  ')
        frame.update()
        t.sleep(0.3)
        
        dots_label.config(text='.. ')
        frame.update()
        t.sleep(0.3)
        
        dots_label.config(text='...')
        frame.update()
        t.sleep(0.3)
loading_animation()


def update_tape():
    for x in range(1000):
        t.sleep(0.001)
        frame.update()
    for r in range(000):
        t.sleep(0.001)
        frame.update()
        
def move_tape():
    loadingstatus.destroy()
    dots_label.destroy()
    update_tape()
    for i in range(8):
        delaytime = 0.02
        tape.place(relx=0.5, rely=0.4-i/100, anchor='center')
        frame.update()
        t.sleep(delaytime)
        delaytime += 0.01
    tape.pack(pady=10)

move_tape()





progress = ttk.Progressbar(frame, orient = HORIZONTAL,
              length = 450, mode = 'determinate')

def bar():
    progress['value'] += 1

def autoprogress():
    for e in range(100):
        bar()
        pause(0.1)

from time import time

from tkinter.messagebox import showinfo

progress.pack(pady = 10)

s = ttk.Style()
s.configure('mcfont', font=('minecraft'))





def operation():
    label.config(text='Initializing...')
    if progress['value'] <= 100:
        label.config(text='Initializing...')
        if toggle_verbose == 'True':
            verbosetext()
        else:
            pass
        for r in range(100):
            bar()
            progress.update()
            label.config(text='Preparing ' + str(progress['value']) + '%')
            t.sleep(0.01)
        label.config(text='Files checked. Beginning injection process...')
        t.sleep(2)
        label.config(text='Injecting...')
        progress.stop()
    else:
        pass

ismcrunning = 'true'

def minecraftisrunning():
    try:
        minecraftcheck = Pymem('javaw.exe')
        minecraftcheck
        ismcrunning = 'true'
        ismcrunning
        return True
    except:
        label.config(text='Minecraft must be running.')
        ismcrunning = 'false'
        return False

def inject_dlls():
    progress.step(1)
    progress.update()
    os.system('requiredfiles\\Injector.exe --process-name javaw.exe --inject dll0.dll')
    print('injecting dll0...')
    t.sleep(0.6)
    print('Finding javaw.exe process...')
    for y in range(4):
        progress.step(1)
        progress.update()
        t.sleep(0.02)
    t.sleep(0.1)
    print('Success.')
    print('Attaching to process...')
    progress.step(3)
    progress.update()
    t.sleep(0.2)
    print('Injecting dll0.dll')
    print('Running command')
    t.sleep(0.01)
    print('Connecting minecraft clients...')
    t.sleep(0.01)
    print('Connected to Lunar')
    t.sleep(0.1)
    print('Connected to vanilla')
    print('Connected to feather')
    print('connected to javaw.exe')
    print('Successfully injected dll0.dll')
    progress['value'] = 10
    os.system('requiredfiles\\Injector.exe --process-name javaw.exe --inject dll1.dll')
    print('injecting dll1...')
    
    t.sleep(0.6)
    print('Finding javaw.exe process...')
    for y in range(4):
        progress.step(1)
        progress.update()
        t.sleep(0.02)
    t.sleep(0.1)
    print('Success.')
    print('Attaching to process...')
    t.sleep(0.2)
    print('Injecting dll1.dll')
    print('Running commands')
    t.sleep(0.01)
    print('Connecting minecraft clients...')
    t.sleep(0.01)
    print('Connected to Lunar')
    t.sleep(0.1)
    print('Connected to vanilla')
    print('Connected to feather')
    print('connected to javaw.exe')
    print('Successfully injected dll1.dll')
    os.system('requiredfiles\\Injector.exe --process-name javaw.exe --inject dll2.dll')
    print('injecting dll2...')
    t.sleep(0.6)
    print('Finding javaw.exe process...')
    for y in range(4):
        progress.step(1)
        progress.update()
        t.sleep(0.02)
    t.sleep(0.1)
    print('Success.')
    print('Attaching to process...')
    t.sleep(0.2)
    print('Injecting dll2.dll')
    print('Running commands')
    t.sleep(0.01)
    print('Connecting minecraft clients...')
    t.sleep(0.01)
    print('Connected to Lunar')
    t.sleep(0.1)
    print('Connected to vanilla')
    print('Connected to feather')
    print('connected to javaw.exe')
    print('Successfully injected dll2.dll')
    os.system('requiredfiles\\Injector.exe --process-name javaw.exe --inject dll3.dll')
    print('injecting dll3...')
    t.sleep(0.6)
    print('Finding javaw.exe process...')
    for y in range(4):
        progress.step(1)
        progress.update()
        t.sleep(0.02)
    t.sleep(0.1)
    print('Success.')
    print('Attaching to process...')
    t.sleep(0.2)
    print('Injecting dll3.dll')
    print('Running commands')
    t.sleep(0.01)
    print('Connecting minecraft clients...')
    t.sleep(0.01)
    print('Connected to Lunar')
    t.sleep(0.1)
    print('Connected to vanilla')
    print('Connected to feather')
    print('connected to javaw.exe')
    print('Successfully injected dll3.dll')
    os.system('requiredfiles\\Injector.exe --process-name javaw.exe --inject dll4.dll')
    print('injecting dll4...')
    t.sleep(0.6)
    print('Finding javaw.exe process...')
    for y in range(4):
        progress.step(1)
        progress.update()
        t.sleep(0.02)
    t.sleep(0.1)
    print('Success.')
    print('Attaching to process...')
    t.sleep(0.2)
    print('Injecting dll4.dll')
    print('Running commands')
    t.sleep(0.01)
    print('Connecting minecraft clients...')
    t.sleep(0.01)
    print('Connected to Lunar')
    t.sleep(0.1)
    print('Connected to vanilla')
    print('Connected to feather')
    print('connected to javaw.exe')
    print('Successfully injected dll4.dll')
    os.system('requiredfiles\\Injector.exe --process-name javaw.exe --inject dll5.dll')
    print('injecting dll5...')
    t.sleep(0.6)
    print('Finding javaw.exe process...')
    for y in range(4):
        progress.step(1)
        progress.update()
        t.sleep(0.02)
    t.sleep(0.1)
    print('Success.')
    print('Attaching to process...')
    t.sleep(0.2)
    print('Injecting dll5.dll')
    print('Running commands')
    t.sleep(0.01)
    print('Connecting minecraft clients...')
    t.sleep(0.01)
    print('Connected to Lunar')
    t.sleep(0.1)
    print('Connected to vanilla')
    print('Connected to feather')
    print('connected to javaw.exe')
    print('Successfully injected dll5.dll')
    os.system('requiredfiles\\Injector.exe --process-name javaw.exe --inject dll6.dll')
    print('injecting dll6...')
    t.sleep(0.6)
    print('Finding javaw.exe process...')
    for y in range(4):
        progress.step(1)
        progress.update()
        t.sleep(0.02)
    t.sleep(0.1)
    print('Success.')
    print('Attaching to process...')
    t.sleep(0.2)
    print('Injecting dll6.dll')
    print('Running commands')
    t.sleep(0.01)
    print('Connecting minecraft clients...')
    t.sleep(0.01)
    print('Connected to Lunar')
    t.sleep(0.1)
    print('Connected to vanilla')
    print('Connected to feather')
    print('connected to javaw.exe')
    print('Successfully injected dll6.dll')
    os.system('requiredfiles\\Injector.exe --process-name javaw.exe --inject NullDLL64.dll')
    print('injecting NullDLL64...')
    t.sleep(0.6)
    print('Finding javaw.exe process...')
    for y in range(4):
        progress.step(1)
        progress.update()
        t.sleep(0.02)
    print(progress['value'])
    t.sleep(0.1)
    print('Success.')
    print('Attaching to process...')
    t.sleep(0.2)
    print('Injecting NullDLL64.dll')
    print('Running commands')
    t.sleep(0.01)
    print('Connecting minecraft clients...')
    t.sleep(0.01)
    print('Connected to Lunar')
    t.sleep(0.1)
    print('Connected to vanilla')
    print('Connected to feather')
    print('connected to javaw.exe')
    print('Successfully injected NullDLL64.dll')
    import random
    for y in range(62):
        progress.step(1)
        progress.update()
        t.sleep(0.05)
    label.config(text='Injection complete. You may now close this window.')

def injection():
        if minecraftisrunning():
            operation()
            inject_dlls()
        else:
            label.config(text='Minecraft must be running')
            
label = Label(frame, text = "Waiting to start", font = "Segoe")  
label.pack()
        
def closewindow():
    exit()

closebutton = ttk.Button(frame, text='Exit', command=closewindow)
closebutton.pack(pady=10)

toggle_verbose = 'False'

injectbutton = ttk.Button(frame, text = 'Inject', command = injection).pack(pady = 0)

mainloop()

frame.mainloop()

win.mainloop()
