import selenium
import tkinter as tk
from tkinter import messagebox

def emitir_estadual(iapp):
    nome = iapp.nome_entry.get()
    sexo = iapp.sexo_box.get()
    cpf = iapp.cpf_entry.get()
    mae = iapp.mae_entry.get()
    pai = iapp.pai_entry.get()
    nascimento = iapp.nasc_entry.get()
    nacionalidade = iapp.nacionalidade_entry.get()
    estadocivil = iapp.estadocivil_entry.get()
    endereco = iapp.endereco_entry.get()

    verificacao = [nome, sexo, cpf, mae, pai, nascimento, nacionalidade, estadocivil, endereco]

    for i in verificacao:
        if i == "":
            break

# Achar formas mais simples de realizar essa verificação
            

    