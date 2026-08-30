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

class Emissao_federal:


    def verificacao_campos(self):
        campos = {
            "CPF": self.cpf,
            "Nascimento": self.nascimento
        }
        self.faltando = [campo for campo, valor in self.campos.items() if not valor.strip()]
        if self.faltando:
            messagebox.showerror("Campos Obrigatórios", f"Preencha os campos faltantes: {', '.join(self.faltando)}", parent=self.main_window)
            return False

    def emitir_federal(self, iapp, main_window):
        self.main_window = main_window

        self.cpf = iapp.cpf2_entry.get()
        self.nascimento = iapp.nasc2_entry.get()

        if not self.verificacao_campos():
            return

         