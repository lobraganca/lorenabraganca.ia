#!/usr/bin/env python3
"""Gera a prévia de uma página do site para publicar como Artifact.

O site é HTML estático com os estilos em arquivos separados. A página do
Artifact não carrega CSS de outro endereço, e ela mesma já vem embrulhada
em <html><head><body>. Então esta prévia: tira o embrulho, põe o CSS do
design system dentro da página e acrescenta a faixa "Prévia".

Uso: python3 scripts/gerar-previa.py site/index.html saida.html
"""
import re, sys, pathlib

origem, destino = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
raiz = origem.parent
html = origem.read_text(encoding="utf-8")

def css_local(m):
    caminho = raiz / m.group(1).lstrip("/")
    return "<style>\n" + caminho.read_text(encoding="utf-8") + "\n</style>"

cabeca = re.search(r"<head>(.*?)</head>", html, re.S).group(1)
corpo = re.search(r"<body[^>]*>(.*)</body>", html, re.S).group(1)
cabeca = re.sub(r'<link rel="stylesheet" href="(/estilos/[^"]+)">', css_local, cabeca)
cabeca = re.sub(r"<meta [^>]*>\n?", "", cabeca)
titulo = re.search(r"<title>.*?</title>", cabeca, re.S).group(0)
cabeca = cabeca.replace(titulo, "")
faixa = ('<div style="background:#EAFBFE;color:#0B1F3A;font:700 14px/1.4 system-ui,sans-serif;'
         'padding:8px 16px;text-align:center">Prévia · ainda não está no ar em lorenabraganca.com.br</div>')
destino.write_text(titulo + "\n" + cabeca + "\n" + faixa + corpo, encoding="utf-8")
print("prévia:", destino)
