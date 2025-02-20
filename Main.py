import os
from subprocess import call
from tkinter import messagebox
import sys
import tkinter as tk
from tkinter import ttk


class HOTEL_MANAGEMENT:
    # Definindo as cores como variáveis de classe
    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#ffffff'
    _ana1color = '#ffffff'
    _ana2color = '#ffffff'

    # Definindo as fontes 
    font14 = ('Segoe UI', 15, 'bold')
    font16 = ('Swis 721 BlkCn', 40, 'bold')
    font9 = ('Segoe UI', 9, 'bold')

    def __init__(self):
        root = tk.Tk()
        root.geometry("963x600+540+110")
        root.title("Projeto Sistema :")
        
        # Cor de fundo do root
        root.configure(background="#f0f0f0")  # Cor neutra de fundo (cinza claro)
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")

        # Configurando formulário inicial
        self.Frame1 = tk.Frame(root, relief=tk.GROOVE, borderwidth=4)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        self.Frame1.configure(background="#f0f0f0")  # Cinza claro
        self.Frame1.configure(highlightbackground="#d9d9d9", highlightcolor="black", width=925)

        # Ícone da janela
        root.wm_iconbitmap(r"C:\Users\Jonias Silva\Documents\Tkinter_pool\icones\home_icon.ico")
        
        # Mensagem de boas-vindas
        self.Message6 = tk.Message(self.Frame1)
        self.Message6.place(relx=0.00, rely=0.00, relheight=0.15, relwidth=1.00)
        self.Message6.configure(background="#b3e5fc")  # Azul fundo
        self.Message6.configure(font=self.font16)  
        self.Message6.configure(foreground="#1a237e")  # Azul escuro para o texto
        self.Message6.configure(highlightbackground="#d9d9d9")
        self.Message6.configure(highlightcolor="black")
        self.Message6.configure(text=''' Sistema Hotel - Seja Bem-vindo ''')
        self.Message6.configure(width=880)

        # Botões com cor padrão azul
        button_bg_color = "#4CAF50"  # Azul claro padrão
        button_fg_color = "#ffffff"  # Texto branco nos botões

        # Botão 1 (Entrada)
        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.17, rely=0.17, height=90, width=566)
        self.Button2.configure(activebackground="#d9d9d9")  
        self.Button2.configure(activeforeground="#000000") 
        self.Button2.configure(font=self.font14)  
        self.Button2.configure(background=button_bg_color)
        self.Button2.configure(foreground=button_fg_color)
        self.Button2.configure(disabledforeground="#bfbfbf")
        self.Button2.configure(pady="0")
        self.Button2.configure(text=''' 1 - ENTRADA ''')
        self.Button2.configure(width=566)

        # Botão 2 (Mostrar lista de hóspedes)
        self.Button3 = tk.Button(self.Frame1)
        self.Button3.place(relx=0.17, rely=0.33, height=90, width=566)
        self.Button3.configure(activebackground="#d9d9d9")  
        self.Button3.configure(activeforeground="#000000")  
        self.Button3.configure(font=self.font14)  
        self.Button3.configure(background=button_bg_color)
        self.Button3.configure(foreground=button_fg_color)
        self.Button3.configure(disabledforeground="#bfbfbf")
        self.Button3.configure(pady="0")
        self.Button3.configure(text=''' 2 - Mostrar Lista de Hospedes ''')
        self.Button3.configure(width=566)

        # Botão 3 (Saída)
        self.Button4 = tk.Button(self.Frame1)
        self.Button4.place(relx=0.17, rely=0.49, height=90, width=566)
        self.Button4.configure(activebackground="#d9d9d9")  
        self.Button4.configure(activeforeground="#000000") 
        self.Button4.configure(font=self.font14) 
        self.Button4.configure(background=button_bg_color)
        self.Button4.configure(foreground=button_fg_color)
        self.Button4.configure(disabledforeground="#bfbfbf")
        self.Button4.configure(pady="0")
        self.Button4.configure(text=''' 3 - Saida ''')
        self.Button4.configure(width=566)

        # Botão 4 (Informações do hóspede)
        self.Button5 = tk.Button(self.Frame1)
        self.Button5.place(relx=0.17, rely=0.65, height=90, width=566)
        self.Button5.configure(activebackground="#d9d9d9")  
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(font=self.font14)  
        self.Button5.configure(background=button_bg_color)
        self.Button5.configure(foreground=button_fg_color)
        self.Button5.configure(disabledforeground="#bfbfbf")
        self.Button5.configure(pady="0")
        self.Button5.configure(text=''' 4 - Informações do Hospede ''')
        self.Button5.configure(width=566)

        # Botão 5 (Fechar o sistema)
        self.Button6 = tk.Button(self.Frame1)
        self.Button6.place(relx=0.17, rely=0.80, height=90, width=566)
        self.Button6.configure(activebackground="#d9d9d9")  
        self.Button6.configure(activeforeground="#000000") 
        self.Button6.configure(font=self.font14) 
        self.Button6.configure(background=button_bg_color)
        self.Button6.configure(foreground=button_fg_color)
        self.Button6.configure(disabledforeground="#bfbfbf")
        self.Button6.configure(pady="0")
        self.Button6.configure(text=''' 4 - Fechar o sistema ''')
        self.Button6.configure(width=566)
        self.Button6.configure(command=root.destroy)

        # Rodando o loop principal
        root.mainloop()


if __name__ == '__main__':
    GUEST = HOTEL_MANAGEMENT()
