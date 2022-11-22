from tkinter import *

janela = Tk()
janela.title('Calculadora')

#VARIAVEIS GLOBAIS
vl1 = 0.0
vl2 = 0.0
ope = ''
res = 0.0
status = 'inicio'


# FUNÇÕES

def inserir(valor):
    global vl1, vl2, ope, res, status

    if status == 'inicio':

        if valor == '0' or valor == '1' or valor == '2' or valor == '3' or valor == '4' or valor == '5' or valor == '6' or valor == '7' or valor == '8' or valor == '9':
            # INSERIR VALOR NA TELA
            visor['state'] = 'normal'
            visor.insert(END, valor)
            visor['state'] = 'disabled'

        elif valor != 'c' and valor != '=':
            vl1 = round(float(visor.get()), 2)
            vl2 = vl1
            res = vl1
            ope = valor
            status = 'meio'

            visor['state'] = 'normal'
            visor.insert(END, valor)
            visor['state'] = 'disabled'

        elif valor == 'c':
            vl1 = 0
            vl2 = 0
            ope = ''
            res = 0
            status = 'inicio'

            visor['state'] = 'normal'
            visor.delete(0, END)
            visor['state'] = 'disabled'

    elif status == 'meio':

        if valor == '0' or valor == '1' or valor == '2' or valor == '3' or valor == '4' or valor == '5' or valor == '6' or valor == '7' or valor == '8' or valor == '9':
            # INSERIR VALOR NA TELA
            visor['state'] = 'normal'
            visor.insert(END, valor)
            visor['state'] = 'disabled'

        elif valor == '=':

            try:
                vl2 = round(float(visor.get().split(ope)[-1]),2)
            except:
                vl2 = round(float(visor.get().split(ope)[0]),2)

            if ope == '+':
                res = round(vl1 + vl2, 2)

            if ope == '-':
                res = round(vl1 - vl2, 2)

            if ope == '*':
                res = round(vl1 * vl2, 2)

            if ope == '/':
                res = round(vl1 / vl2, 2)

            vl1 = res
            vl2 = vl1
            status = 'fim'

            visor['state'] = 'normal'
            visor.delete(0, END)
            visor.insert(END, str(res))
            visor['state'] = 'disabled'

        elif valor == 'c':
            vl1 = 0
            vl2 = 0
            ope = ''
            res = 0
            status = 'inicio'

            visor['state'] = 'normal'
            visor.delete(0, END)
            visor['state'] = 'disabled'

        else:
            try:
                vl2 = round(float(visor.get().split(ope)[-1]), 2)

                if ope == '+':
                    res = round(vl1 + vl2, 2)

                if ope == '-':
                    res = round(vl1 - vl2, 2)

                if ope == '*':
                    res = round(vl1 * vl2, 2)

                if ope == '/':
                    res = round(vl1 / vl2, 2)

                ope = valor
                vl1 = res

            except:
                vl2 = round(float(visor.get().split(ope)[0]), 2)

                if ope == valor:
                    if ope == '+':
                        res = round(vl1 + vl2, 2)

                    if ope == '-':
                        res = round(vl1 - vl2, 2)

                    if ope == '*':
                        res = round(vl1 * vl2, 2)

                    if ope == '/':
                        res = round(vl1 / vl2, 2)

                    vl1 = res

            visor['state'] = 'normal'
            visor.delete(0, END)
            visor.insert(END, str(res)+ope)
            visor['state'] = 'disabled'

    elif status == 'fim':

        if valor == '0' or valor == '1' or valor == '2' or valor == '3' or valor == '4' or valor == '5' or valor == '6' or valor == '7' or valor == '8' or valor == '9':

            status = 'inicio'
            vl1 = 0
            vl2 = 0
            ope = ''
            res = 0

            visor['state'] = 'normal'
            visor.delete(0, END)
            visor.insert(END, valor)
            visor['state'] = 'disabled'

        elif valor == 'c':
            vl1 = 0
            vl2 = 0
            ope = ''
            res = 0
            status = 'inicio'

            visor['state'] = 'normal'
            visor.delete(0, END)
            visor['state'] = 'disabled'

        else:
            vl1 = round(float(visor.get()), 2)
            vl2 = vl1
            res = vl1
            ope = valor
            status = 'meio'

            visor['state'] = 'normal'
            visor.insert(END, valor)
            visor['state'] = 'disabled'



# VISOR ENTRA COM OS VALORES
visor = Entry(janela, font='Arial 20 bold', bg='#696969', fg='#000000', width=16)
visor.pack()
visor['state'] = 'disabled'

# CRIAR O PAINEL PARA INSERIR OS BOTOES
painel = Frame(janela)

# CRIAR OS BOTÕES

bt_0 = Button(painel, bg='#2F4F4F', bd=0, text='0', font='Arial 18 bold',
              fg='#FFFFF0', width=4, height=1, command=lambda: inserir('0'))

bt_1 = Button(painel, bg='#000000', bd=0, text='1', font='Arial 18 bold',
              fg='#FFFFF0', width=4, height=2, command=lambda: inserir('1'))

bt_2 = Button(painel, bg='#000000', bd=0, text='2', font='Arial 18 bold',
              fg='#FFFFF0', width=4, height=2, command=lambda: inserir('2'))

bt_3 = Button(painel, bg='#000000', bd=0, text='3', font='Arial 18 bold',
              fg='#FFFFF0', width=4, height=2, command=lambda: inserir('3'))

bt_4 = Button(painel, bg='#000000', bd=0, text='4', font='Arial 18 bold',
              fg='#FFFFF0', width=4, height=2, command=lambda: inserir('4'))

bt_5 = Button(painel, bg='#000000', bd=0, text='5', font='Arial 18 bold',
              fg='#FFFFF0', width=4, height=2, command=lambda: inserir('5'))

bt_6 = Button(painel, bg='#000000', bd=0, text='6', font='Arial 18 bold',
              fg='#FFFFF0', width=4, height=2, command=lambda: inserir('6'))

bt_7 = Button(painel, bg='#000000', bd=0, text='7', font='Arial 18 bold',
              fg='#FFFFF0', width=4, height=2, command=lambda: inserir('7'))

bt_8 = Button(painel, bg='#000000', bd=0, text='8', font='Arial 18 bold',
              fg='#FFFFF0', width=4, height=2, command=lambda: inserir('8'))

bt_9 = Button(painel, bg='#000000', bd=0, text='9', font='Arial 18 bold',
              fg='#FFFFF0', width=4, height=2, command=lambda: inserir('9'))

bt_igual = Button(painel, bg='#1C1C1C', bd=0, text='=', font='Arial 18 bold',
                  fg='#FFFFF0', width=4, height=1, command=lambda: inserir('='))

bt_c = Button(painel, bg='#1C1C1C', bd=0, text='C', font='Arial 18 bold',
              fg='#FFFFF0', width=4, height=1, command=lambda: inserir('c'))

bt_menos = Button(painel, bg='#1C1C1C', bd=0, text='-', font='Arial 18 bold',
                  fg='#FFFFF0', width=3, height=1, command=lambda: inserir('-'))

bt_soma = Button(painel, bg='#1C1C1C', bd=0, text='+', font='Arial 18 bold',
                 fg='#FFFFF0', width=3, height=2, command=lambda: inserir('+'))

bt_x = Button(painel, bg='#1C1C1C', bd=0, text='x', font='Arial 18 bold',
              fg='#FFFFF0', width=3, height=2, command=lambda: inserir('*'))

bt_divide = Button(painel, bg='#1C1C1C', bd=0, text='/', font='Arial 18 bold',
                   fg='#FFFFF0', width=3, height=2, command=lambda: inserir('/'))

painel.pack()

# PRIMEIRA FILA
#SETA OS BOTÕES NA TELA
bt_7.grid(row=0, column=0)
bt_8.grid(row=0, column=1)
bt_9.grid(row=0, column=2)
bt_divide.grid(row=0, column=3)

# SEGUNDA FILA

bt_4.grid(row=1, column=0)
bt_5.grid(row=1, column=1)
bt_6.grid(row=1, column=2)
bt_x.grid(row=1, column=3)

# TERCEIRA FILA

bt_1.grid(row=2, column=0)
bt_2.grid(row=2, column=1)
bt_3.grid(row=2, column=2)
bt_soma.grid(row=2, column=3)

# QUARTA FILA

bt_0.grid(row=3, column=0)
bt_igual.grid(row=3, column=1)
bt_c.grid(row=3, column=2)
bt_menos.grid(row=3, column=3)


janela.mainloop()
