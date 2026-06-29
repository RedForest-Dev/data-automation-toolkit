# Data Automation Toolkit

### [EN] Overview
This repository contains automation tools for data extraction. The primary script (`ocr_lead_parser.py`) performs deep OCR analysis on screenshots to extract and structure professional email contacts.

### [RU] Обзор
Репозиторий содержит инструменты автоматизации для извлечения данных. Основной скрипт (`ocr_lead_parser.py`) проводит глубокий OCR-анализ скриншотов для извлечения и структурирования профессиональных контактов.

### [EN] Features
* **Image Upscaling:** Uses 2x resizing for high-accuracy OCR.
* **Regex Filtering:** Advanced email pattern matching with system-domain exclusion.
* **Structured Output:** Automatically generates clean CSV files with contact names.

### [RU] Возможности
* **Масштабирование:** Увеличение в 2 раза для точности распознавания.
* **Фильтрация:** Поиск e-mail по регулярным выражениям с исключением системных доменов.
* **Структурирование:** Автоматическая генерация аккуратных CSV-файлов.

### [EN] Requirements
* `pytesseract`
* `PIL` (Pillow)
* `Tesseract OCR` engine installed locally.
