.PHONY: default all pdf handout tex clean

DEST=target
DEST_PDF=$(DEST)/pdfs
DEST_PDF_HANDOUT=$(DEST)/pdfs/handout
DEST_TEX=$(DEST)/tex
FIGS_DIR=imagens
IGNORAR=README.md
SOURCES=$(filter-out $(IGNORAR), $(sort $(wildcard *.md)))
PDF=$(addprefix $(DEST_PDF)/, $(SOURCES:.md=.pdf))
PDF_HANDOUT=$(addprefix $(DEST_PDF_HANDOUT)/, $(SOURCES:.md=.pdf))
TEX=$(addprefix $(DEST_TEX)/, $(SOURCES:.md=.tex))
PANDOC=$(DEST)/bin/pandoc
PANDOC_VERSION=2.7.3
PANDOC_CMD=$(PANDOC) \
		-V mathspec \
		--metadata-file metadata.yml \
		--template templates/default.latex \
		--toc \
		--standalone \
		--pdf-engine tectonic \
		--to beamer

default:
	@echo Executando make em paralelo [$(shell nproc) tarefas]
	@make -s -j $(shell nproc) $(PDF) $(PDF_HANDOUT)

all: $(PDF) $(PDF_HANDOUT) $(TEX)

pdf: $(PDF)

handout: $(PDF_HANDOUT)

tex: $(TEX)

$(DEST_PDF)/%.pdf: %.md templates/default.latex metadata.yml $(FIGS_DIR)/* $(PANDOC) Makefile
	@mkdir -p $(DEST_PDF)
	@echo $@
	@$(PANDOC_CMD) -o $@ $<

$(DEST_PDF_HANDOUT)/%.pdf: %.md templates/default.latex metadata.yml $(FIGS_DIR)/* $(PANDOC) Makefile
	@mkdir -p $(DEST_PDF_HANDOUT)
	@echo $@
	@$(PANDOC_CMD) -V classoption:handout -o $@ $<

$(DEST_TEX)/%.tex: %.md templates/default.latex metadata.yml $(FIGS_DIR)/* $(PANDOC) Makefile
	@mkdir -p $(DEST_TEX)
	@echo $@
	@$(PANDOC_CMD) -o $@ $<

$(PANDOC):
	mkdir -p $(DEST)
	curl -L https://github.com/jgm/pandoc/releases/download/$(PANDOC_VERSION)/pandoc-$(PANDOC_VERSION)-linux.tar.gz | tar xz -C $(DEST) --strip-components=1

clean:
	@echo Removendo $(DEST_PDF) e $(DEST_TEX)
	@rm -rf $(DEST_PDF) $(DEST_TEX)
