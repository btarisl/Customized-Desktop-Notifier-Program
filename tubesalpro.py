from time import sleep
from tkinter import *
from tkinter import ttk
import datetime

penghitungeksekusi = 0

print('\n')
print('Selamat datang di Aplikasi INGAT! by Btarisalwa')
print('-------------------------------------------------')
print('Aplikasi akan terus berjalan hingga user menginginkan berhenti')
print('Aplikasi ini akan memunculkan pengingat selama interval yang telah ditentukan')
print('-------------')
try:
    remind_time = int(input('Masukkan durasi interval notifikasi (dalam detik): '))
    judul = input('Masukkan judul program notifikasi: ')
    pesan = input('Masukkan teks notifikasi: ')
    # snooze_time = 3
except ValueError:
    print('Value yang dimasukkan salah.')    
print('\n\nTerimakasih! Anda akan mendapatkan notifikasi pertama dalam {0} detik'.format(remind_time))
print('\n\n')
print('Aplikasi dimulai....')

def ReminderWindow(judul, pesan):
    global root
    print('Eksekusi', penghitungeksekusi)
    win = Toplevel()
    win.withdraw()
    win.update_idletasks()
    x = (win.winfo_screenwidth() - win.winfo_reqwidth()) / 2
    y = (win.winfo_screenheight() - win.winfo_reqheight()) / 2
    win.geometry("+%d+%d" % (x, y))
    win.deiconify()
    win.title(judul)
    pesan1=pesan
    pesan2='Pesan akan muncul setiap {0} detik'.format(remind_time)
    pesan3 = 'Apakah anda ingin diingatkan kembali?'
    ttk.Label(win, text=pesan1).grid(column=1, row=0)
    ttk.Label(win, text=pesan2).grid(column=1, row=1)
    ttk.Label(win, text=pesan3).grid(column=1, row=2)
    yes_btn = ttk.Button(win, text='YA', command=lambda: action(win, True))
    yes_btn.grid(column=0,row=3)
    ttk.Button(win, text='TIDAK', command=lambda: action(win, False)).grid(column=2, row=3)
    yes_btn.focus()
    win.lift()
    win.attributes('-topmost', True)

def catatWaktu():
    now = datetime.datetime.now()
    mulaiwaktu = now.strftime("%H:%M:%S")
    with open("log.txt", 'a') as f:
        f.write(f"Anda telah {judul} pada jam {now}\n")
    return 0

def action(win, more):
    global penghitungeksekusi
    global root
    if more==True:
        print(f'Notifikasi akan muncul lagi dalam {remind_time} detik')
    else:
        print('Notifikasi akan diberhentikan')
    if more:
        catatWaktu()
        win.destroy()
        sleep(remind_time)
        penghitungeksekusi = penghitungeksekusi + 1
        ReminderWindow(judul, pesan)
    else:
        catatWaktu()
        win.destroy()
        root.destroy()

root = Tk()
root.withdraw()
penghitungeksekusi = 1
ReminderWindow(judul, pesan)   
root.mainloop()
print('Terimakasih sudah menggunakan Aplikasi Notifikasi ini! See you next time! ^^')

