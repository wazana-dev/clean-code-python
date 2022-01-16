# Clean Code Python

Neste tutorial vamos utilizar alguns conceitos de Clean Code (código limpo) na nossa aplicação Python.

O termo Clean Code se refere a um conjunto de boas práticas na escrita de software que você pode aplicar para obter uma maior legibilidade e fácil manutenção do seu código.

**Agenda**

- Instalação das extensões e pacotes.
- Configuração no VS Code (`settings.json`).
- Aplicar os conceitos de Clean Code.

**Playlist:** [Programando em Python no VS Code](https://www.wazana.dev/playlist/programando-em-python-no-vs-code).

**Episódio:** [Clean Code Python](https://www.wazana.dev/player/clean-code-python/programando-em-python-no-vs-code).

## Introdução

Essas instruções fornecerão uma cópia do projeto para executar em sua máquina para desenvolvimento e teste.

### Pré-requisitos

O que você precisa para completar o tutorial:

- Já ter configurado o VS code conforme [vs-code-python](https://github.com/VianaArthur/config-vscode-python).
- Extensões do VS Code citadas a seguir.
- Pacote [Black](https://github.com/psf/black).
- Pacote [Pylint](https://pypi.org/project/pylint/).

## Instalação de extensões

1. Instale a extensão [Python Indent](https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent).

2. Instale a extensão [indent-rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow).

3. Instale a extensão [Python Docstring Generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring).

4. Instale a extensão [Bracket Pair Colorizer 2](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer-2).

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

## Licença

Projeto licenciado pela [GNU General Public License](https://opensource.org/licenses/GPL-3.0).

## Agradecimentos

- Conteúdo feito para [wazana.dev](https://www.wazana.dev/) - Tecnologia direto ao ponto.
