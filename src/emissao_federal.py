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

class Emissao_federal:

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

    def verificacao_campos(self):
        self.campos = {
            "CPF": self.cpf,
            "Nascimento": self.nascimento
        }
        self.faltando = [campo for campo, valor in self.campos.items() if not valor.strip()]
        if self.faltando:
            messagebox.showerror("Campos Obrigatórios", f"Preencha os campos faltantes: {', '.join(self.faltando)}", parent=self.main_window)
            return False
        self.selecionar_pasta()
        return bool(self.caminho)
        
    def selecionar_pasta(self):
        self.caminho = filedialog.askdirectory(title="Selecione uma pasta", parent=self.main_window)

    def emitir_federal(self, iapp, main_window):
        iapp.botao_emitir_federal.config(state=tk.DISABLED)
        self.main_window = main_window
        self.caminho = ""

        self.cpf = iapp.cpf2_entry.get()
        self.nascimento = iapp.nasc2_entry.get()
        self.tipo_certidao = iapp.certidao_box.get()

        if not self.verificacao_campos():
            iapp.botao_emitir_federal.config(state=tk.NORMAL)
            return

        download_dir = self.caminho
        os.makedirs(download_dir, exist_ok=True)
        arquivos_antes = set(os.listdir(download_dir))

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
        try:
            driver.get("https://www2.trf4.jus.br/trf4/processos/certidao/index.php")

            driver.find_element(By.XPATH, "/html/body/div[1]/section/div[7]/div/form/div/div[1]/input").send_keys(self.cpf)

            driver.find_element(By.XPATH, "/html/body/div[1]/section/div[7]/div/form/div/div[2]/input").send_keys(self.nascimento)

            if self.tipo_certidao == iapp.tipos_certidoes[0]:
                driver.find_element(By.XPATH, "/html/body/div[1]/section/div[7]/div/form/fieldset/b/input[1]").click()
            elif self.tipo_certidao == iapp.tipos_certidoes[1]:
                driver.find_element(By.XPATH, "/html/body/div[1]/section/div[7]/div/form/fieldset/b/input[2]").click()
            elif self.tipo_certidao == iapp.tipos_certidoes[2]:
                driver.find_element(By.XPATH, "/html/body/div[1]/section/div[7]/div/form/fieldset/b/input[3]").click()

            arquivo_pdf = self.aguardar_download(download_dir, arquivos_antes)
            print(f"PDF baixado com sucesso: {arquivo_pdf}")
        finally:
            driver.quit()
            iapp.botao_emitir_federal.config(state=tk.NORMAL)


         