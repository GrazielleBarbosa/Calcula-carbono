from tkinter import *
from tkinter import Tk


# Inicio (estrutura do programa)

janela = Tk()

janela.title("Calcular carbono")
janela.geometry("900x750")
janela.configure(bg="white")

# Estrutura parte esquerda

side_esq = Frame(janela, width=650, height=900, bg="#20b2aa")
side_esq.place(x=0, y=30)


# Text input

text_input = Label(side_esq, text="Gasto mensal (Kwh):", anchor=NW, font=("Ivy 10 bold"), bg="#20b2aa", fg="black")
text_input.place(x=15, y=19)

# Input's

input_energia = Entry(side_esq, width=30, justify="left", relief=SOLID)
input_energia.place(x=150, y=20)

# Calculo

def calculo():
    global input_energia
    energia = float(input_energia.get())
    carbono = 0.090
    emissao = (energia * carbono)

    label_emissao['text'] = f"Sua empresa emite um total de {emissao :.3f} Co2 por mês"

    rendimento = 78.3
    placa = (energia / rendimento)

    label_placa['text'] = (
    f"Para redução do carbono será necessário no mínimo {placa :.3f} placas para suprir a energia mensal")

    placaS = ((545 * 6 * (1 - 0.20)) * 30)

    label_placaS['text'] = (f"Cada placa usada neste projeto gera mensalmente: {placaS:.1f} kwh")

    # Credito Carbono

    limite = 1.000
    creditoC = (energia * carbono)

    if (creditoC >= limite):

        label_creditoC['text'] = (
            "Parabéns! Usando energia fotovoltaica voce tem chances de adquirir créditos de carbono!",)
        label_creditoC_resultado['text'] = (
            f"Podem ser adquiridos aproximadamente: {round(creditoC / 1.000, 2)} créditos mensalmente")
    else:
        label_creditoC_resultado['text'] = ("Você não possui créditos de carbono")


# Titulo principal

nav1 = Frame(janela, width=900, height=30, bg="#20b2aa")
nav1.grid(column=0, row=0)

# Texto central

Tcentro = Label(janela, text="Calcule suas Emissões de carbono", anchor=N, font=("Ivy 10 bold"),
                bg="#20b2aa", fg="black")
Tcentro.grid(column=0, row=0)



# Botão calculo

botao_calc = Button(side_esq, width=25, text="Calcular", anchor=CENTER, font=("Ivy 10 bold"), fg="black", bg="white",
                    command=calculo)
botao_calc.place(x=115, y=90)

# Label's

label_emissao = Label(side_esq, text="", anchor=CENTER, font=("Ivy 10 bold"),bg="#20b2aa", fg="black")
label_emissao.place(x=0, y=200)

label_placa = Label(side_esq, text="", anchor=CENTER, font=("Ivy 10 bold"),bg="#20b2aa", fg="black")
label_placa.place(x=0, y=250)

label_placaS = Label(side_esq, text="", anchor=CENTER, font=("Ivy 10 bold"),bg="#20b2aa", fg="black")
label_placaS.place(x=0, y=300)

label_creditoC = Label(side_esq, text="", anchor=CENTER, font=("Ivy 10 bold"),bg="#20b2aa", fg="black")
label_creditoC.place(x=0, y=350)

label_creditoC_resultado = Label(side_esq, text="", anchor=CENTER, font=("Ivy 10 bold"),bg="#20b2aa", fg="black")
label_creditoC_resultado.place(x=0, y=400)


janela.mainloop()
