#!/usr/bin/env python3
"""
Script para gerar arquivos estáticos do portfólio Flask para GitHub Pages
"""

import os
import shutil
from app import create_app
import markdown

app = create_app()


def generate_static_site():
    """Gerar HTML dos arquivos Markdown dos indicadores"""
    output_dir = "dist"
    docs_src = "docs"
    docs_dest = os.path.join(output_dir, "docs")

    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    os.makedirs(output_dir)
    os.makedirs(docs_dest, exist_ok=True)

    for filename in os.listdir(docs_src):
        if filename.startswith("indicador") and filename.endswith(".md"):
            md_path = os.path.join(docs_src, filename)
            html_name = filename.replace(".md", ".html")
            with open(md_path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            md_content = "".join(lines[1:])  # ignora titulo
            html_content = markdown.markdown(md_content)
            html_template = f"""
            <div class='modal-content-indicador'>
            {html_content}
            </div>
            """
            with open(os.path.join(docs_dest, html_name), "w", encoding="utf-8") as f:
                f.write(html_template)

    print("Arquivos HTML dos indicadores gerados em dist/docs/")

    # Configurar Flask para modo de produção
    app.config["SERVER_NAME"] = None  # Remover para evitar problemas no GitHub Pages
    app.config["PREFERRED_URL_SCHEME"] = "https"

    # Gerar página principal
    with app.app_context():
        with app.test_client() as client:
            response = client.get("/")

            if response.status_code == 200:
                html_content = response.get_data(as_text=True)

                html_content = html_content.replace('href="/static/', 'href="./static/')
                html_content = html_content.replace('src="/static/', 'src="./static/')

                with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
                    f.write(html_content)
                print("index.html gerado com sucesso")
            else:
                print(f"Erro ao gerar index.html: {response.status_code}")
                return False

    # Copiar arquivos HTML de app/templates
    templates_src = "app/templates"
    for filename in os.listdir(templates_src):
        if filename.endswith('.html'):
            shutil.copy(os.path.join(templates_src, filename), os.path.join(output_dir, filename))

    print("Arquivos HTML copiados de app/templates para dist")

    # Copiar arquivos estáticos de app/static
    static_source = "app/static"
    static_dest = os.path.join(output_dir, "static")
    if os.path.exists(static_source):
        shutil.copytree(static_source, static_dest)
        print("Arquivos estáticos copiados com sucesso")

    # Criar arquivo .nojekyll para GitHub Pages
    with open(os.path.join(output_dir, ".nojekyll"), "w", encoding="utf-8") as f:
        f.write("")
    print("Arquivo .nojekyll criado")

    print("Site estático gerado com sucesso em ./dist/")
    return True


if __name__ == "__main__":
    success = generate_static_site()

    if not success:
        exit(1)
