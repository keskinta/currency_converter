import tkinter
from tkinter import *
import tkinter as tk
import requests

THEMECOLOUR='#E6F4F1'
BOX_COLOUR='#FFFFFF'
LABEL_COLOUR='#333333'
INPUT_COLOUR='#666666'
BUTTON_COLOUR='#28A745'

EXCHANGE_RATE_KEY='8QaArRaQuBm91YOy69ROYUdLJNbaoANn'
EXCHANGE_RATE_API='https://api.apilayer.com/exchangerates_data/convert?'





class FrontPage:
    def __init__(self,currencies):
        self.window=Tk()
        self.currency_list=currencies
        self.window.title('Convert Currencies')
        self.window.geometry("500x300")
        self.window.config(background=THEMECOLOUR)
        self.logo=Label(text='Currency Convert',foreground=LABEL_COLOUR,background=THEMECOLOUR,font=('Arial',29))
        self.logo.place(x=130,y=20)

    # ------output canvas------

        self.box=tkinter.Canvas(background=BOX_COLOUR,height=70,width=300)
        self.box_text=self.box.create_text(150, 35, text='', font=("Helvetica", 20))
        self.box.place(x=100,y=80)


    # currency list from API
        currency_options=self.currency_list

    # getting the variable from users choice
        clicked=StringVar()

        clicked.set('Choose your Currency')

        second_clicked=StringVar()

        second_clicked.set('Choose your Currency')

    # first drowdown
        dropdown_menu=OptionMenu(self.window,clicked,*currency_options,)
        dropdown_menu.place(x=70,y=180)

    # Equals sign

        equals_sign=Label(self.window,text='=',font=('Arial',29),background=THEMECOLOUR,highlightthickness=0)
        equals_sign.place(x=240,y=170)

    # 2nd dropdown
        dropdown_two_menu = OptionMenu(self.window, second_clicked, *currency_options, )
        dropdown_two_menu.place(x=270, y=180)

    # user input amount of exchange
        input_text=Label(text=f'Please Enter the amount',background=THEMECOLOUR,highlightthickness=0)
        input_text.place(x=170, y=220)

        input_amount=Entry()
        input_amount.place(x=150, y=250)

    # function to exchange currency with apilayer.api
        def get_currency_1():
            self.box.delete(self.box_text)
            PARAMS = {
                'apikey':'8QaArRaQuBm91YOy69ROYUdLJNbaoANn',
                'from':clicked.get()[0:3],
                'to':second_clicked.get()[0:3],
                'amount':int(input_amount.get())
            }

            result=requests.get(url=EXCHANGE_RATE_API,params=PARAMS)
            outcome=str(round(result.json()['result'],2))
            self.box_text=self.box.create_text(150, 35, text=f'{outcome} {second_clicked.get()[0:3]}', font=("Helvetica", 20))

    # convert button with function command
        get_button = Button(text='Convert', command=get_currency_1)
        get_button.place(x=279, y=253)
        self.window.mainloop()