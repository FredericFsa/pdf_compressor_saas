import os
import uuid
import subprocess
import platform
import tempfile
from flask import request, render_template, send_file, flash, redirect, url_for, after_this_request
from app import app


UPLOAD_FOLDER = tempfile.gettempdir()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('pdf_file')
        if not file or not file.filename.endswith('.pdf'):
            flash("Veuillez téléverser un fichier PDF valide.", "error")
            return redirect(url_for('index'))

        input_path = os.path.join(UPLOAD_FOLDER, f"{uuid.uuid4()}.pdf")
        output_path = os.path.join(UPLOAD_FOLDER, f"{uuid.uuid4()}_compressed.pdf")
        file.save(input_path)

        # 🔁 Choisir la bonne commande selon l'environnement
        if platform.system() == "Windows":
            gs_path = r"C:\Program Files\gs\gs10.05.1\bin\gswin64c.exe"
        else:
            gs_path = "gs"  # Linux / Docker

        command = [
            gs_path, "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            "-dPDFSETTINGS=/ebook",
            "-dNOPAUSE", "-dQUIET", "-dBATCH",
            f"-sOutputFile={output_path}", input_path
        ]

        try:
            subprocess.run(command, check=True)

            if not os.path.exists(output_path):
                flash("La compression a échoué : aucun fichier n’a été généré.", "error")
                return redirect(url_for('index'))

            @after_this_request
            def cleanup(response):
                try:
                    os.remove(input_path)
                except:
                    pass
                try:
                    os.remove(output_path)
                except:
                    pass
                return response

            return send_file(output_path, as_attachment=True, download_name="compressed.pdf")
        except subprocess.CalledProcessError:
            flash("Erreur de compression du PDF.", "error")

    return render_template('index.html')


@app.get("/health")
def health():
    return {"ok": True}, 200
