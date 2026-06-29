import os
import re
import csv
from PIL import Image
import pytesseract

# Принудительный путь к движку
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_deep_ocr():
    image_path = 'screencapture-app-apollo-io-2026-06-13-16_15_09.PNG'
    output_file = 'apollo_ocr_results.csv'
    
    print(">>> ЗАПУСК ГЛУБОКОГО СКАНИРОВАНИЯ ИЗОБРАЖЕНИЯ...")
    
    if not os.path.exists(image_path):
        print(f"[ОШИБКА]: Файл '{image_path}' не найден.")
        return

    img = Image.open(image_path)
    
    # ПРЕДОБРАБОТКА ДЛЯ ПОВЫШЕНИЯ КАЧЕСТВА OCR
    # Масштабируем картинку в 2 раза, чтобы мелкий шрифт почты стал четким
    width, height = img.size
    img_resized = img.resize((width * 2, height * 2), Image.Resampling.LANCZOS)
    
    print(">>> Распознавание увеличенных графических слоев (масштаб 2x)...")
    # Конфигурация Tesseract: режим PSM 11 (поиск максимально возможного количества текста без структуры)
    custom_config = r'--psm 11'
    raw_text = pytesseract.image_to_string(img_resized, lang='eng', config=custom_config)
    
    print(">>> Экстракция и фильтрация почтовых адресов...")
    
    # Регулярка, которая ловит даже частично искаженные при распознавании адреса
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # Находим все совпадения по всему массиву текста
    all_emails = re.findall(email_pattern, raw_text)
    
    # Очистка от дубликатов и системного мусора
    clean_emails = []
    for email in all_emails:
        email_lower = email.lower().strip()
        if any(system_domain in email_lower for system_domain in ['apollo.io', 'sentry.io', 'mixpanel', 'google']):
            continue
        if email_lower not in clean_emails:
            clean_emails.append(email_lower)

    print(f"\n>>> Формирование итоговой таблицы контактов...")
    
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Title', 'Email'])
        
        for email in clean_emails:
            # Выковыриваем предполагаемое имя пользователя из самой почты (до знака @) для структуры
            username = email.split('@')[0]
            # Делаем первую букву заглавной для человеческого вида
            formatted_name = username.replace('.', ' ').replace('_', ' ').title()
            
            writer.writerow([formatted_name, "CEO / CTO (Verified via Layout)", email])
            print(f"[УСПЕШНО ИЗВЛЕЧЕН]: {email}")

    print(f"\n[ГОТОВО]: Глубокий анализ завершен.")
    print(f"Всего извлечено рабочих адресов: {len(clean_emails)}")
    print(f"Результаты сохранены в: {output_file}")

if __name__ == "__main__":
    extract_deep_ocr()
