# Notas de aula de Fundamentos da Computação

Para gerar os pdfs execute o comando

```
make
```

Os pdfs são gerados no diretório `target/pdfs`.

Se preferir, faça o download dos [pdfs](https://malbarbo.pro.br/ensino/2019/1640/) diretamente.


## Dependências

Em um sistema baseado no Debian as seguintes dependências são requeridas para gerar os pdfs:

```
curl
librsvg2-bin
make
python3
python3-pyqt5
python3-pyqt5.qtsvg
```

Os programas [pandoc](https://pandoc.org/) e [tectonic](https://tectonic-typesetting.github.io/) são baixados automaticamente e extraídos para o diretório `target/bin`.
