PYTHON := python
PIP    := $(PYTHON) -m pip
PYTEST := $(PYTHON) -m pytest
WEEK   ?= w01

export PYTHONDONTWRITEBYTECODE := 1

BLUE   := \033[34m
GREEN  := \033[32m
YELLOW := \033[33m
RED    := \033[31m
RESET  := \033[0m

.PHONY: help test render clean

.DEFAULT_GOAL := help

help:
	@printf "$(BLUE)────────────────────────────────────────────────────────────────────────$(RESET)\n"
	@printf "     $(GREEN)Komputasi Probabilitas dan Statistika$(RESET) $(BLUE)[$(RESET) $(YELLOW)Assignment Helper$(RESET)$(BLUE) ]$(RESET)\n"
	@printf "$(BLUE)────────────────────────────────────────────────────────────────────────$(RESET)\n"
	@printf " $(BLUE)Cara Pakai:$(RESET)  make $(GREEN)<target>$(RESET) [WEEK=wXX]\n\n"
	@printf " $(BLUE)Daftar Perintah:$(RESET)\n"
	@printf "  $(GREEN)test$(RESET)    Menjalankan test lengkap untuk minggu aktif\n"
	@printf "  $(GREEN)render$(RESET)  Merender laporan Quarto (html)\n"
	@printf "  $(GREEN)clean$(RESET)   Menghapus file sementara, cache pytest, dan __pycache__\n"
	@printf "  $(GREEN)help$(RESET)    Menampilkan ringkasan bantuan ini\n"
	@printf "$(BLUE)────────────────────────────────────────────────────────────────────────$(RESET)\n"
	@printf " $(BLUE)Catatan:$(RESET) Default minggu adalah $(YELLOW)w01$(RESET). Gunakan $(GREEN)make test WEEK=w02$(RESET)\n"

test:
	@printf "$(BLUE)[1/2]$(RESET) Memastikan dependensi terinstall...\n"
	@$(PIP) install -r requirements.txt --quiet
	@printf "$(BLUE)[2/2]$(RESET) Menjalankan pengujian untuk $(YELLOW)$(WEEK)$(RESET)...\n"
	@$(PYTEST) checkers/$(WEEK)/quiz_tests.py || true

render:
	@printf "$(BLUE)[BUILD]$(RESET) Merender proyek Quarto...\n"
	@quarto render

clean:
	@printf "$(BLUE)[CLEAN]$(RESET) Menghapus artifact dan semua cache...\n"
	@rm -rf .pytest_cache .quarto docs
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@printf "$(GREEN)Selesai.$(RESET)\n"
