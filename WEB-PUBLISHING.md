# Publicación de la documentación web

La Base de Conocimiento Técnica se publica como un sitio estático mediante **Material for MkDocs**, **GitHub Actions** y **GitHub Pages**.

Los documentos Markdown del repositorio son la única fuente de contenido. La carpeta temporal `.site-docs` y la salida `site` se generan automáticamente y no deben incorporarse al control de versiones.

---

# Dirección del sitio

Una vez habilitado GitHub Pages, el sitio estará disponible en:

<https://jp-rma.github.io/base-de-conocimientos-tecnicos/>

Esta dirección requiere que el repositorio de GitHub se llame `base-de-conocimientos-tecnicos`.

---

# Primera habilitación en GitHub

Una persona con permisos de administración debe realizar esta configuración una sola vez:

1. Ingresar al repositorio en GitHub.
2. Si todavía conserva el nombre anterior, abrir **Settings > General** y renombrarlo como `base-de-conocimientos-tecnicos`.
3. Abrir **Settings**.
4. Seleccionar **Pages** dentro de **Code and automation**.
5. En **Build and deployment**, elegir **GitHub Actions** como fuente.
6. Subir los cambios a la rama `main` o ejecutar manualmente el workflow **Publicar documentación**.

Los cambios posteriores se publicarán automáticamente cuando se actualice la rama `main`.

---

# Vista previa local

Requisitos:

- Python 3.10 o superior.
- Las dependencias de `requirements-docs.txt`.

Preparar y visualizar la documentación:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --requirement requirements-docs.txt
python scripts\prepare_docs.py
mkdocs serve
```

El servidor local informará la dirección de vista previa, normalmente `http://127.0.0.1:8000/`.

Para verificar la construcción final:

```powershell
python scripts\prepare_docs.py
mkdocs build --strict
```

---

# Incorporación de nuevos documentos

1. Crear el Markdown utilizando la plantilla correspondiente.
2. Enlazarlo desde el `README.md` de su categoría y desde `INDEX.md`.
3. Agregarlo a la sección `nav` de `mkdocs.yml` para que aparezca en la navegación del sitio.
4. Verificar los enlaces con una construcción estricta antes de publicar.

---

# Privacidad

GitHub Pages normalmente publica el sitio en Internet, aunque el repositorio de origen sea privado.

Si la documentación debe quedar restringida exclusivamente al personal autorizado, se debe confirmar que la organización disponga de publicación privada mediante GitHub Enterprise Cloud antes de habilitar Pages. En caso contrario, no se debe publicar información interna o sensible mediante este mecanismo.
