#pip install python-docx

import os
import subprocess
import sys

venv_name = "my_venv"
subprocess.run([sys.executable, "-m", "venv", venv_name])

activate_script = os.path.join(venv_name, "Scripts", "activate") if os.name == "nt" else os.path.join(venv_name, "bin", "activate")

subprocess.run(f"{activate_script} && pip install python-docx", shell=True)

from docx import Document

name = input("Введите название файла: ")
doc = Document()  
doc.add_heading('Title', 0)  

doc.save(f"{name}.docx")  



