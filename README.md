![Python](https://img.shields.io/badge/python-3.11-blue)
![Flask](https://img.shields.io/badge/flask-2.3-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)
![Dockerized](https://img.shields.io/badge/docker-ready-blue)


# PDF Compressor SaaS

Une application SaaS simple pour compresser des fichiers PDF trop volumineux à l’aide de Ghostscript.

## 🚀 Fonctionnalités

- Upload de fichier PDF via interface web
- Compression automatique avec Ghostscript
- Téléchargement du fichier compressé
- Compatible local (Windows) et Docker (Linux)
- Interface élégante avec Bootstrap 5

## 📦 Structure

```
pdf_compressor_saas/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── templates/
│       └── index.html
├── run.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

## 🖥️ Exécution locale (Windows)

1. Installer Python 3.11+
2. Installer Ghostscript : [https://ghostscript.com/download/gsdnld.html](https://ghostscript.com/download/gsdnld.html)
3. Ajouter `gswin64c.exe` au PATH
4. Installer les dépendances :

```bash
pip install -r requirements.txt
python run.py
```

Accès via [http://localhost:5000](http://localhost:5000)

## 🐳 Exécution avec Docker

### 1. Construction de l’image

```bash
docker build -t pdf-compressor .
```

### 2. Lancement du conteneur

```bash
docker run -d -p 5000:5000 --name pdf-compressor pdf-compressor
```

### ou via docker-compose

```bash
docker-compose up --build
```

## ✨ Auteur

© 2025 Frédéric SALERNO. Tous droits réservés.

---

Ce projet utilise Ghostscript dans le conteneur Linux (`gs`) ou sur Windows (`gswin64c.exe`) selon l’environnement.
