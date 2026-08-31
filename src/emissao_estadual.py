import os
import json
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk

class Emissao:
    ARQUIVO_JSON = os.path.join(os.path.dirname(__file__), "historico_certidoes.json")

    @staticmethod
    def aguardar_download(download_dir, arquivos_antes, timeout=60):
        limite = time.time() + timeout

        while time.time() < limite:
            arquivos_atuais = set(os.listdir(download_dir))
            arquivos_novos = arquivos_atuais - arquivos_antes
            download_em_andamento = any(
                nome.endswith((".crdownload", ".tmp", ".part"))
                for nome in arquivos_atuais
            )
            pdfs = [
                os.path.join(download_dir, nome)
                for nome in arquivos_novos
                if nome.lower().endswith(".pdf")
            ]

            if pdfs and not download_em_andamento:
                arquivo_pdf = max(pdfs, key=os.path.getmtime)
                tamanho = os.path.getsize(arquivo_pdf)
                time.sleep(1)

                if tamanho > 0 and os.path.getsize(arquivo_pdf) == tamanho:
                    return arquivo_pdf

            time.sleep(0.5)

        raise TimeoutError("O PDF não foi baixado dentro do tempo esperado.")

    def carregar_historico(self):
        if os.path.exists(self.ARQUIVO_JSON):
            with open(self.ARQUIVO_JSON, "r", encoding="utf-8") as f:
                try:
                    dados = json.load(f)
                except json.JSONDecodeError:
                    return []

                if isinstance(dados, dict):
                    return [dados]
                if isinstance(dados, list):
                    return dados
                return []
        return []

    def salvar_json(self):
        dados = {
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
        historico = self.carregar_historico()
        pessoa_existente = None
        for pessoa in historico:
            if pessoa.get("CPF") == self.cpf:
                pessoa_existente = pessoa
                break

        if pessoa_existente:
            pessoa_existente.update(dados)
        else:
            historico.append(dados)

        with open(self.ARQUIVO_JSON, "w", encoding="utf-8") as f:
            json.dump(historico, f, ensure_ascii=False, indent=4)

    def buscar_pessoa(self):
        historico = self.carregar_historico()
        for pessoa in historico:
            if pessoa.get("CPF") == self.cpf:
                return pessoa
        return None

    def selecionar_pasta(self):
        self.caminho = filedialog.askdirectory(title="Selecione uma pasta", parent=self.main_window)

    def verificacao_campos(self):
        self.campos = {
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
        self.faltando = [campo for campo, valor in self.campos.items() if not valor.strip()]
        if self.faltando:
            messagebox.showerror("Campos Obrigatórios", f"Preencha os campos faltantes: {', '.join(self.faltando)}", parent=self.main_window)
            return False
        self.salvar_json()
        self.selecionar_pasta()
        return bool(self.caminho)

    def emitir_estadual(self, iapp, main_window):
        iapp.botao_emitir_estadual.config(state=tk.DISABLED)
        self.main_window = main_window
        self.caminho = ""

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
        
        if not self.verificacao_campos():
            iapp.botao_emitir_estadual.config(state=tk.NORMAL)
            return

        download_dir = self.caminho
        os.makedirs(download_dir, exist_ok=True)
        arquivos_antes = set(os.listdir(download_dir))

        chrome_options = Options()
        prefs = {
            "download.default_directory": os.path.abspath(download_dir),
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True,
            "safebrowsing.enabled": True,
            "safeberowsing.disable_download_protection": True
        }
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--disable_download_protection")
        
        driver = webdriver.Chrome(options=chrome_options)
        try:
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

            driver.find_element(By.XPATH, "/html/body/div[1]/form/div[4]/input").send_keys(self.nome)
            
            if self.sexo == "Feminino":    
                select_entry_sexo = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/form/div[5]/select")))
                select = Select(select_entry_sexo)
                select.select_by_value("F")
           
            driver.find_element(By.XPATH, "/html/body/div[1]/form/div[6]/input").send_keys(self.cpf)
            
            driver.find_element(By.XPATH, "/html/body/div[1]/form/div[8]/input").send_keys(self.mae)
            
            driver.find_element(By.XPATH, "/html/body/div[1]/form/div[9]/input").send_keys(self.pai)
            
            driver.find_element(By.XPATH, "/html/body/div[1]/form/div[10]/input").send_keys(self.nascimento)
            
            nacionalidade_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/form/div[11]/select")))
            select_nac = Select(nacionalidade_element)
            select_nac.select_by_visible_text(self.nacionalidade)
            
            estadocivil_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "estadoCivil")))
            select_est = Select(estadocivil_element)
            select_est.select_by_visible_text(self.estadocivil)
            
            driver.find_element(By.ID, "rg").send_keys(self.rg)
            
            driver.find_element(By.ID, "orgaoExpedidor").send_keys(self.orgao_expedidor)
            
            uf_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/form/div[13]/select")))
            select_uf = Select(uf_element)
            select_uf.select_by_visible_text(self.uf)
            
            driver.find_element(By.ID, "endereco").send_keys(self.endereco)
            
            driver.find_element(By.XPATH, "/html/body/div[1]/form/div[15]/input").click()

            arquivo_pdf = self.aguardar_download(download_dir, arquivos_antes)
            print(f"PDF baixado com sucesso: {arquivo_pdf}")
        finally:
            driver.quit()
            iapp.botao_emitir_estadual.config(state=tk.NORMAL)
