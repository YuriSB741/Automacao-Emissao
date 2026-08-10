import selenium
import tkinter as tk
from tkinter import messagebox

def emitir_estadual(iapp, main_window):
    nome = iapp.nome_entry.get()
    sexo = iapp.sexo_box.get()
    cpf = iapp.cpf_entry.get()
    mae = iapp.mae_entry.get()
    pai = iapp.pai_entry.get()
    nascimento = iapp.nasc_entry.get()
    nacionalidade = iapp.nacionalidade_entry.get()
    estadocivil = iapp.estadocivil_entry.get()
    endereco = iapp.endereco_entry.get()

    campos = {
        "Nome": nome,
        "Sexo": sexo,
        "CPF": cpf,
        "Mãe": mae,
        "Pai": pai,
        "Nascimento": nascimento, 
        "Nacionalidade": nacionalidade,
        "Estado Civil": estadocivil,
        "Endereço": endereco
    }

    faltando = [campo for campo, valor in campos.items() if not valor.strip()]

    if faltando:
        messagebox.showerror("Campos Obrigatórios", f"Preencha {', '.join(faltando)}", parent=main_window)
        return


 

    