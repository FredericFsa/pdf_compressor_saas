# Render Deploy Pack

## Fichiers inclus
- `Dockerfile` : image Python + Ghostscript/qpdf/poppler, lance gunicorn.
- `render.yaml` : blueprint Render (déploie un service web Docker).
- `README_deploy.md` (ce fichier) : étapes.

## Étapes Render (avec Dockerfile)
1. Pousse ces fichiers à la racine du dépôt backend.
2. Sur Render → **New +** → **Blueprint** → pointe vers ton repo GitHub.
3. Render lit `render.yaml` et crée le service **pdf-compressor-backend**.
4. Premier déploiement (build Docker, install deps, run gunicorn).
5. URL fournie par Render (ex: https://pdf-compressor-backend.onrender.com).

## API
- Ajoute un endpoint santé `/health` (Flask) :
  ```python
  @app.get("/health")
  def health():
      return {"ok": True}
  ```

## CORS (si front sur un autre domaine)
  ```bash
  pip install flask-cors
  ```
  ```python
  from flask_cors import CORS
  CORS(app, resources={r"/*": {"origins": "*"}})  # restreins si besoin
  ```
