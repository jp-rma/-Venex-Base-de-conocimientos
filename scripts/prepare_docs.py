"""Prepara una copia temporal de la documentación para MkDocs.

Los archivos Markdown del repositorio siguen siendo la única fuente de verdad.
La carpeta .site-docs se genera en cada construcción y no se versiona.
"""

from __future__ import annotations

import shutil
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
STAGING_DIR = REPOSITORY_ROOT / ".site-docs"

ROOT_DOCUMENTS = (
    ("INDEX.md", "PROJECT-INDEX.md"),
    ("CONTRIBUTING.md", "CONTRIBUTING.md"),
    ("AUTORIA.md", "AUTORIA.md"),
    ("WEB-PUBLISHING.md", "WEB-PUBLISHING.md"),
    ("CHANGELOG.md", "CHANGELOG.md"),
)

CONTENT_DIRECTORIES = (
    "01-Procedimientos",
    "02-Guias-Tecnicas",
    "03-Casos-RMA",
    "04-Checklists",
    "05-Compatibilidades",
    "06-Plantillas",
    "07-Imagenes",
)


def require_path(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"No se encontró el contenido requerido: {path}")


def main() -> None:
    homepage = REPOSITORY_ROOT / "web" / "index.md"
    web_assets = REPOSITORY_ROOT / "web" / "assets"

    require_path(homepage)
    require_path(web_assets)

    if STAGING_DIR.exists():
        shutil.rmtree(STAGING_DIR)

    STAGING_DIR.mkdir(parents=True)
    shutil.copy2(homepage, STAGING_DIR / "index.md")
    shutil.copytree(web_assets, STAGING_DIR / "assets")

    for source_path, destination_path in ROOT_DOCUMENTS:
        source = REPOSITORY_ROOT / source_path
        require_path(source)
        shutil.copy2(source, STAGING_DIR / destination_path)

    for relative_path in CONTENT_DIRECTORIES:
        source = REPOSITORY_ROOT / relative_path
        require_path(source)
        shutil.copytree(source, STAGING_DIR / relative_path)

    print(f"Documentación preparada en {STAGING_DIR}")


if __name__ == "__main__":
    main()
