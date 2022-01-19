# Clean Code Python

<p align="center">
  <a href="https://wazana.dev">
    <img src="https://www.datocms-assets.com/41512/1642548236-logo.png" height="128">
    <h1 align="center">wazana.dev</h1>
  </a>
</p>

<p align="center">
  <a aria-label="Linkedin wazana.dev" href="https://www.linkedin.com/company/wazana-dev/">
    <img src="https://img.shields.io/badge/wazana--dev-333.svg?style=for-the-badge&logo=linkedin&labelColor=0A66C2">
  </a>
  
  <a aria-label="Instagram wazana.dev" href="https://www.instagram.com/wazana.dev/">
    <img src="https://img.shields.io/badge/@wazana%2Edev-333.svg?style=for-the-badge&logo=instagram&logoColor=white&labelColor=E4405F">
  </a>
  
  <a aria-label="YouTube wazana.dev" href="https://www.youtube.com/channel/UCVE9-HO_GzLtDK4IGKVSYXA">
    <img src="https://img.shields.io/badge/Wazana-333.svg?style=for-the-badge&logo=youtube&logoColor=white&labelColor=FF0000">
  </a>
  
  <a aria-label="Discord wazana.dev" href="https://discord.gg/MF6F4t8eQw">
    <img src="https://img.shields.io/badge/wazana%2Edev-333.svg?style=for-the-badge&logo=discord&logoColor=white&labelColor=5865F2">
  </a>
</p>

**Playlist:** [Programando em Python no VS Code](https://www.wazana.dev/playlist/programando-em-python-no-vs-code).

## Introdução

Neste tutorial vamos utilizar alguns conceitos de Clean Code (código limpo) na nossa aplicação Python.

O termo Clean Code se refere a um conjunto de boas práticas na escrita de software que você pode aplicar para obter uma maior legibilidade e fácil manutenção do seu código.

### Nível
- [x] - Básico

### Pré-requisitos

O que você precisa para completar o tutorial:

- Já ter configurado o VS code conforme [vs-code-python](https://github.com/VianaArthur/config-vscode-python).
- Extensões do VS Code citadas a seguir.
- Pacote [Black](https://github.com/psf/black).
- Pacote [Pylint](https://pypi.org/project/pylint/).


## Instalação de pacotes

Este comando instalará todos os pacotes contidos no arquivo `requirements.txt`.

**macOS**

```
python3 -m pip install requirements.txt
```

**Windows**

```
python -m pip install requirements.txt
```

## Configuração VS Code

Abra o arquivo `settings.json` no VS Code e adicione as seguintes propriedades:

```
{
  "editor.formatOnSave": true,
  "[python]": {
    "editor.insertSpaces": true,
    "editor.tabSize": 4,
    "editor.defaultFormatter": "ms-python.python"
  },
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "indentRainbow.includedLanguages": ["python"]
}
```

## Autor

**Arthur Viana** 

[![Linkedin: arthur-viana](https://img.shields.io/badge/-Arthur%20Viana-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/arthur-viana/)](https://www.linkedin.com/in/arthur-viana/)
[![GitHub Arthur](https://img.shields.io/github/followers/VianaArthur?label=follow&style=social)](https://github.com/VianaArthur)

## Agradecimentos

- Conteúdo feito para [wazana.dev](https://www.wazana.dev/) - Tecnologia direto ao ponto.
