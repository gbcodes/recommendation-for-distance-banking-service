from tkinter import *
from dbo import *
from tkinter import messagebox



def yur_is_clicked(event):
    print('y')
    person['text'] = 'Yur.xlsx'
    user['text'] = 'Юр. лицо'

    window = Toplevel()
    window.geometry('900x600')

    type_label = Label(window, text="На все вопросы отвечать либо 'да', либо 'нет'", font='Montserrat 15', fg='#FF0000').pack()

    scrolling = Scrollbar(window)
    scrolling.pack(side=RIGHT, fill=Y)

    service_label = Label(window, text="Важен ли вам уровень безопасности? ", font='Montserrat 12').pack(fill=X)
    entry_service = Entry(window, font='Montserrat 10')
    entry_service.pack()
    # service_label.place(x=135, y=270)
    # entry_service.place(x=900, y=270)

    intb_label = Label(window, text='Нужен ли вам интернет банкинг?', font = 'Montserrat 12').pack(fill=X)
    entry_intb = Entry(window, font = 'Montserrat 10')
    entry_intb.pack()
    # intb_label.place(x = 135, y= 330)
    # entry_intb.place(x=900, y= 330)

    inb_label = Label(window, text='Важна ли вам низкая цена за подключение интернет банкинга? ',
                      font='Montserrat 12').pack()
    entry_inb = Entry(window, font='Montserrat 10')
    entry_inb.pack()

    isp_label = Label(window, text='Важна ли вам низкая цена за обслуживание интернатом банкингом? ',
                      font='Montserrat 12').pack()
    isp_entry = Entry(window, font='Montserrat 10')
    isp_entry.pack()


    clib_label = Label(window, text='Нужен ли вам банк клиент?', font='Montserrat 12').pack()
    entry_clib = Entry(window, font='Montserrat 10')
    entry_clib.pack()
    # clib_label.place(x=135, y=390)
    # entry_clib.place(x=900, y=390)

    prb_label = Label(window, text='Важна ли вам низкая цена на подключение банка клиента? ',
                      font='Montserrat 12').pack()
    prb_entry = Entry(window, font='Montserrat 10')
    prb_entry.pack()

    isb_label = Label(window, text='Важна ли вам низкая цена за обслуживание? ', font='Montserrat 12').pack()
    isb_entry = Entry(window, font='Montserrat 10')
    isb_entry.pack()

    mob_label = Label(window, text='Нужен ли вам мобильный банк?', font='Montserrat 12').pack()
    entry_mob = Entry(window, font='Montserrat 10')
    entry_mob.pack()
    # mob_label.place(x=135, y=450)
    # entry_mob.place(x=900, y=450)

    cred_label = Label(window, text='Важна ли вам ставка по кредиту?', font='Montserrat 12').pack()
    cred_entry = Entry(window, font='Montserrat 10')
    cred_entry.pack()
    # cred_entry.place(x=900, y=510)
    # cred_label.place(x=135, y=510)

    int_label = Label(window, text='Важно ли вам удобство интерфейса?', font='Montserrat 12').pack()
    int_entry = Entry(window, font='Montserrat 10')
    int_entry.pack()
    # int_label.place(x=135, y=570)
    # int_entry.place(x=900, y=570)

    show_result_button = Button(window, text="Показать\nрезультат", width=10, height=2,
                                bg="blue", fg="white", font="Montserrat 10")
    show_result_button.place(x=390, y=500)

    result = Label(window, font="Montserrat 10",fg='#FF0000')
    result.place(x=230, y=550)

    def output(event):

        client = person['text']

        data = pd.read_excel(client)
        res = yuri(data, entry_service.get().lower().strip(), entry_intb.get().lower().strip(), entry_clib.get().lower().strip(),
                   entry_mob.get().lower().strip(), cred_entry.get().lower().strip(), int_entry.get().lower().strip(),
                   entry_inb.get().lower().strip(), isp_entry.get().lower().strip(),
                   prb_entry.get().lower().strip(), isb_entry.get().lower().strip())

        result['text'] = res

    show_result_button.bind('<Button-1>', output)

def fiz_is_clicked(event):
    print('f')
    person['text'] = 'Fiz.xlsx'
    user['text'] = 'Физ. лицо'

    window = Tk()
    window.geometry('900x600')

    type_label = Label(window, text="На все вопросы отвечать либо 'да', либо 'нет'", font='Montserrat 15',
                       fg='#FF0000').pack()

    service_label = Label(window, text="Важен ли вам уровень безопасности? ", font='Montserrat 10').pack()
    entry_service = Entry(window, font='Montserrat 8')
    entry_service.pack()
    # service_label.place(x=135, y=270)
    # entry_service.place(x=900, y=270)

    sms_label = Label(window, text='Нужен ли вам sms банкинг?', font='Montserrat 10').pack()
    entry_sms = Entry(window, font='Montserrat 8')
    entry_sms.pack()
    # sms_label.place(x=135, y=330)
    # entry_sms.place(x=900, y=330)

    smp_label = Label(window, text ='Важна ли вам низкая цена за смс банкинг? ', font='Montserrat 10').pack()
    smp_entry = Entry(window, font='Montserrat 8')
    smp_entry.pack()

    intb_label = Label(window, text='Нужен ли вам интернет банкинг?', font='Montserrat 10').pack()
    entry_intb = Entry(window, font='Montserrat 8')
    entry_intb.pack()
    # intb_label.place(x=135, y=390)
    # entry_intb.place(x=900, y=390)

    inb_label = Label(window, text='Важна ли вам низкая цена за подключение интернет банкинга? ',
                      font='Montserrat 10').pack()
    entry_inb = Entry(window, font='Montserrat 8')
    entry_inb.pack()

    isp_label = Label(window, text='Важна ли вам низкая цена за обслуживание интернатом банкингом? ',
                      font='Montserrat 10').pack()
    isp_entry = Entry(window, font='Montserrat 8')
    isp_entry.pack()

    mob_label = Label(window, text='Нужен ли вам мобильный банк?', font='Montserrat 10').pack()
    entry_mob = Entry(window, font='Montserrat 8')
    entry_mob.pack()
    # mob_label.place(x=135, y=450)
    # entry_mob.place(x=900, y=450)

    mp_label = Label(window, text='Важна ли вам низкая плата за мобильный банк? ', font='Montserrat 10').pack()
    mp_entry = Entry(window, font='Montserrat 8')
    mp_entry.pack()

    mi_label = Label(window, text='Важна ли вам низкая цена за использование?', font='Montserrat 10').pack()
    mi_entry = Entry(window, font='Montserrat 8')
    mi_entry.pack()

    vklad_label = Label(window, text='Важна ли вам возможность открывать вклад?', font='Montserrat 10').pack()
    vklad_entry = Entry(window, font='Montserrat 8')
    vklad_entry.pack()
    # vklad_entry.place(x=900, y=510)
    # vklad_label.place(x=135, y=510)

    vkp_label = Label(window, text='Важен ли вам высокий процент по вкладу? ', font='Montserrat 10').pack()
    vkp_entry = Entry(window, font='Montserrat 8')
    vkp_entry.pack()

    cred_label = Label(window, text='Важна ли вам возможность брать кредит?', font='Montserrat 10').pack()
    cred_entry = Entry(window, font='Montserrat 8')
    cred_entry.pack()
    # cred_entry.place(x=900, y=570)
    # cred_label.place(x=135, y=570)

    crp_label = Label(window, text='Важен ли вам низкий процент кредитования? ', font='Montserrat 10').pack()
    crp_entry = Entry(window, font='Montserrat 8')
    crp_entry.pack()

    int_label = Label(window, text='Важно ли вам удобство интерфейса?', font='Montserrat 10').pack()
    int_entry = Entry(window, font='Montserrat 8')
    int_entry.pack()

    # int_label.place(x=135, y=630)
    # int_entry.place(x=900, y=630)


    show_result_button = Button(window, text="Показать\nрезультат", width=10, height=2,
                                bg="blue", fg="white", font="Montserrat 10")
    show_result_button.place(x=700, y=300)

    result = Label(window, font="Montserrat 10", fg='#FF0000')
    result.place(x=620, y=370)

    def output(event):
        client = person['text']


        res = fizi(str(entry_service.get().lower().strip()), str(entry_sms.get().lower().strip()), str(entry_intb.get().lower().strip()),
                   str(entry_mob.get().lower().strip()), str(vklad_entry.get().lower().strip()), str(cred_entry.get().lower().strip()),
                   str(int_entry.get().lower().strip()), str(smp_entry.get().lower().strip()), str(entry_inb.get().lower().strip()),
                   str(isp_entry.get().lower().strip()), str(mp_entry.get().lower().strip()), str(mi_entry.get().lower().strip()),
                   str(vkp_entry.get().lower().strip()), str(crp_entry.get().lower().strip()))

        result['text'] = res

    show_result_button.bind('<Button-1>', output)

def korp_is_clicked(event):
    print('k')
    person['text'] = 'Korp.xlsx'
    user['text'] = 'Корпорация'

    window = Toplevel()
    window.geometry('900x600')

    type_label = Label(window, text="На все вопросы отвечать либо 'да', либо 'нет'", font='Montserrat 15',
                       fg='#FF0000').pack()

    service_label = Label(window, text="Важен ли вам уровень безопасности? ", font='Montserrat 12').pack(fill=X)
    entry_service = Entry(window, font='Montserrat 10')
    entry_service.pack()
    # service_label.place(x=135, y=270)
    # entry_service.place(x=900, y=270)

    intb_label = Label(window, text='Нужен ли вам интернет банкинг?', font='Montserrat 12').pack(fill=X)
    entry_intb = Entry(window, font='Montserrat 10')
    entry_intb.pack()
    # intb_label.place(x = 135, y= 330)
    # entry_intb.place(x=900, y= 330)

    inb_label = Label(window, text = 'Важна ли вам низкая цена за подключение интернет банкинга? ', font='Montserrat 12').pack()
    entry_inb = Entry(window, font='Montserrat 10')
    entry_inb.pack()

    isp_label = Label(window, text='Важна ли вам низкая цена за обслуживание интернатом банкингом? ', font='Montserrat 12').pack()
    isp_entry = Entry(window, font='Montserrat 10')
    isp_entry.pack()


    clib_label = Label(window, text='Нужен ли вам банк клиент?', font='Montserrat 12').pack()
    entry_clib = Entry(window, font='Montserrat 10')
    entry_clib.pack()
    # clib_label.place(x=135, y=390)
    # entry_clib.place(x=900, y=390)

    prb_label = Label(window, text='Важна ли вам низкая цена на подключение банка клиента? ',
                      font='Montserrat 12').pack()
    prb_entry = Entry(window, font='Montserrat 10')
    prb_entry.pack()

    isb_label = Label(window, text='Важна ли вам низкая цена за обслуживание? ', font='Montserrat 12').pack()
    isb_entry = Entry(window, font='Montserrat 10')
    isb_entry.pack()


    int_label = Label(window, text='Важно ли вам удобство интерфейса?', font='Montserrat 12').pack()
    int_entry = Entry(window, font='Montserrat 10')
    int_entry.pack()
    # int_label.place(x=135, y=570)
    # int_entry.place(x=900, y=570)



    show_result_butt = Button(window, text="Показать\nрезультат", width=10, height=2,
                                bg="blue", fg="white", font="Montserrat 10")
    show_result_butt.place(x=395, y=400)

    result = Label(window, font="Montserrat 12",fg='#FF0000')
    result.place(x=180,y=460)

    def outp(event):
        client = person['text']

        data = pd.read_excel(client)
        res = korpi(data, entry_service.get().lower().strip(), entry_intb,entry_inb.get().lower().strip(),
                    isp_entry.get().lower().strip(), prb_entry.get().lower().strip(), isb_entry.get().lower().strip(),
                    entry_clib.get().lower().strip(), int_entry.get().lower().strip())

        result['text'] = res

    show_result_butt.bind('<Button-1>', outp)

file = ''

root = Tk()
root.geometry('900x600')
root.resizable(width=False, height=False)

title = Label(root, text='Брокер ДБО')

title['font'] = 'Montserrat 26 bold'
title.pack(fill=X)


post_title = Label(root, text='Система подбора банка, нужного Вам')
post_title["fg"] = "#1E90FF"
post_title["font"] = 'Montserrat 17 bold'
post_title.pack(fill=X)

#block 1
question = Label(root, text='Пожалуйста, определите себя в одну из категорий')
question["font"] = "Montserrat 20"
question.pack(fill=X)

button1 = Button(root, text='Физ. лицо', width=18, height=2, bg='white', fg='black', font='Montserrat 16')
button1.place(x=20, y=120)

user = Label(root, font='Montserrat 16')
user.place(x=680, y=200)

button2 = Button(root, text='Юр. лицо', width=18, height=2, bg='white', fg='black', font='Montserrat 16')
button2.place(x=310, y=120)

person = Label(root, font='Montserrat 16')

button3 = Button(root, text='Корпорация', width=18, height=2, bg='white', fg='black', font='Montserrat 16')
button3.place(x=600, y=120)

pers = Label(root, font='Montserrat 16')


button1.bind('<Button-1>', fiz_is_clicked)
button2.bind('<Button-1>', yur_is_clicked)
button3.bind('<Button-1>', korp_is_clicked)

from PIL import Image, ImageTk
import os

img = ImageTk.PhotoImage(Image.open("img.png"))
panel = Label(root, image = img)
panel.place(x=35, y=200)




root.mainloop()