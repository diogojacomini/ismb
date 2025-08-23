#!/usr/bin/env python3
"""
Script para gerar arquivos estáticos do portfólio Flask para GitHub Pages
"""

import os
import shutil
from app import app


def generate_static_site():
    """Gera os arquivos estáticos do portfólio"""

    # Criar diretório de saída
    output_dir = "dist"
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    # Configurar Flask para modo de produção
    app.config["SERVER_NAME"] = None  # Remover para evitar problemas no GitHub Pages
    app.config["PREFERRED_URL_SCHEME"] = "https"

    with app.app_context():
        # Gerar página principal
        with app.test_client() as client:
            response = client.get("/")

            if response.status_code == 200:
                html_content = response.get_data(as_text=True)
                # Corrigir caminhos para funcionar como site estático
                html_content = html_content.replace('href="/static/', 'href="./static/')
                html_content = html_content.replace('src="/static/', 'src="./static/')

                with open(
                    os.path.join(output_dir, "index.html"), "w", encoding="utf-8"
                ) as f:
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
