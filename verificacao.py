import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import tkinter as tk
from tkinter import messagebox

class Emissao:
    def emitir_estadual(self, iapp, main_window):
        self.nome = iapp.nome_entry.get().upper()
        self.sexo = iapp.sexo_box.get()
        self.cpf = iapp.cpf_entry.get()
        self.mae = iapp.mae_entry.get().upper()
        self.pai = iapp.pai_entry.get().upper()
        self.nascimento = iapp.nasc_entry.get()
        self.nacionalidade = iapp.nacionalidade_entry.get().capitalize()
        self.estadocivil = iapp.estadocivil_entry.get()
        self.rg = iapp.rg_entry.get()
        self.orgao_expedidor = iapp.orgao_entry.get().upper()
        self.uf = iapp.uf_entry.get().upper()
        self.endereco = iapp.endereco_entry.get().upper()

        campos = {
            "Nome": self.nome,
            "Sexo": self.sexo,
            "CPF": self.cpf,
            "Mãe": self.mae,
            "Pai": self.pai,
            "Nascimento": self.nascimento, 
            "Nacionalidade": self.nacionalidade,
            "Estado Civil": self.estadocivil,
            "RG" : self.rg,
            "Órgão Expedidor" : self.orgao_expedidor,
            "UF" : self.uf,
            "Endereço": self.endereco
        }

        faltando = [campo for campo, valor in campos.items() if not valor.strip()]

        if faltando:
            messagebox.showerror("Campos Obrigatórios", f"Preencha os campos faltantes: {', '.join(faltando)}", parent=main_window)
            return

        download_dir = os.path.join(os.getcwd(), "Downloads")
        os.makedirs(download_dir, exist_ok=True)

        chrome_options = Options()
        prefs = {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True,
            "safebrowsing.enabled": True
        }
        chrome_options.add_experimental_option("prefs", prefs)
        
        driver = webdriver.Chrome(options=chrome_options)
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

        # Escreve o nome no site
        driver.find_element(By.XPATH, "/html/body/div[1]/form/div[4]/input").send_keys(self.nome)
        # Escolhe o sexo
        if self.sexo == "Feminino":    
            select_entry_sexo = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/form/div[5]/select")))
            select = Select(select_entry_sexo)
            select.select_by_value("F")
        # Escreve o cpf no site
        driver.find_element(By.XPATH, "/html/body/div[1]/form/div[6]/input").send_keys(self.cpf)
        # Escreve o nome da mãe
        driver.find_element(By.XPATH, "/html/body/div[1]/form/div[8]/input").send_keys(self.mae)
        # Escreve o nome do pai
        driver.find_element(By.XPATH, "/html/body/div[1]/form/div[9]/input").send_keys(self.pai)
        # Escreve a data de nascimento
        driver.find_element(By.XPATH, "/html/body/div[1]/form/div[10]/input").send_keys(self.nascimento)
        # Escolhe a nacionalidade
        nacionalidade_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/form/div[11]/select")))
        select_nac = Select(nacionalidade_element)
        select_nac.select_by_visible_text(self.nacionalidade)
        # Escolhe o estado civil
        estadocivil_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "estadoCivil")))
        select_est = Select(estadocivil_element)
        select_est.select_by_visible_text(self.estadocivil)
        # Escreve o RG
        driver.find_element(By.ID, "rg").send_keys(self.rg)
        # Escreve o órgão expedidor
        driver.find_element(By.ID, "orgaoExpedidor").send_keys(self.orgao_expedidor)
        # Escolhe o UF
        uf_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/form/div[13]/select")))
        select_uf = Select(uf_element)
        select_uf.select_by_visible_text(self.uf)
        # Escreve o endereço
        driver.find_element(By.ID, "endereco").send_keys(self.endereco)
        # Apertar em emissão
        driver.find_element(By.XPATH, "/html/body/div[1]/form/div[15]/input").click()
        
