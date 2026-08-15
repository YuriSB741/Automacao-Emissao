from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import tkinter as tk
from tkinter import messagebox
import time


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

    driver = webdriver.Chrome()
    driver.get("https://www.tjrs.jus.br/novo/processos-e-servicos/servicos-processuais/emissao-de-antecedentes-e-certidoes/")

    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "iframe"))
        )
    driver.switch_to.frame(iframe)

    select_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "tipoDocumento"))
        )
    select = Select(select_element)
    select.select_by_value("3")




 

    