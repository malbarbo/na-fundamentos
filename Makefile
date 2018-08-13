.PHONY: all default clean

DEST=pdfs
IGNORAR=README.md
SOURCES=$(filter-out $(IGNORAR), $(wildcard *.md))
PDFS=$(addprefix $(DEST)/, $(SOURCES:.md=.pdf))
PANDOC=./local/bin/pandoc
PANDOC_VERSION=2.2.2.1

default:
	@echo Executando make em paralelo [$(shell nproc) tarefas]
	@make -s -j $(shell nproc) all

all: $(PDFS)

$(DEST)/%.pdf: %.md templates/default.latex $(PANDOC) Makefile
	@mkdir -p $(DEST)
	@echo $@
	@$(PANDOC) \
		--template templates/default.latex \
		--toc \
		--standalone \
		-V author:"Marco A L Barbosa" \
		-V institute:"Departamento de Informática\\\\Universidade Estadual de Maringá" \
		-V theme:metropolis \
		-V themeoptions:"numbering=fraction,subsectionpage=progressbar,block=fill" \
		-t beamer \
		-o $@ $<

$(PANDOC):
	mkdir -p local
	curl -L https://github.com/jgm/pandoc/releases/download/$(PANDOC_VERSION)/pandoc-$(PANDOC_VERSION)-linux.tar.gz | tar xz -C local --strip-components=1

clean:
	@echo Removendo $(DEST)
	@rm -rf $(DEST)
