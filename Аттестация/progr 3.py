import re

def check_answers(student_file, answer_key):
    """
    Автоматическая проверка текстовых заданий формата "Термин: Определение"
    
    Параметры:
        student_file (str): путь к файлу с ответами студента
        answer_key (dict): словарь с эталонными ответами {термин: определение}
    
    Возвращает:
        tuple: (количество баллов, список с обратной связью)
    """
    score = 0
    feedback = []
    line_counter = 0
    
    with open(student_file, 'r', encoding='utf-8') as f:
        print(f"\n🔍 Анализ файла: {student_file}")
        print("=" * 50)
        
        for line in f:
            line_counter += 1
            line = line.strip()
            
            # Проверка соответствия формату
            if re.match(r'^[^:]+:.+$', line):
                term, definition = map(str.strip, line.split(':', 1))
                normalized_term = term.lower()
                
                # Поиск термина в эталонном словаре
                if normalized_term in answer_key:
                    correct_def = answer_key[normalized_term]
                    
                    # Сравнение определений
                    if definition.lower() == correct_def.lower():
                        score += 1
                        feedback.append(f"[✓] Правильно: {term} - {definition}")
                        print(f"✅ Строка {line_counter}: Верно! '{term}'")
                    else:
                        feedback.append(f"[×] Ошибка: {term}: ваш ответ '{definition}', правильно '{correct_def}'")
                        print(f"❌ Строка {line_counter}: Неверно! {term}")
                        print(f"    Ваш ответ: '{definition}'")
                        print(f"    Эталон:    '{correct_def}'")
                else:
                    feedback.append(f"[?] Неизвестный термин: {term}")
                    print(f"⚠️ Строка {line_counter}: Неизвестный термин '{term}'")
            else:
                feedback.append(f"[!] Ошибка формата: {line}")
                print(f"⛔ Строка {line_counter}: Некорректный формат!")
    
    print("=" * 50)
    print(f"📊 Итоговый балл: {score}/{len(answer_key)}")
    return score, feedback

# ТЕСТИРОВАНИЕ СКРИПТА
if __name__ == "__main__":
    # Эталонные ответы
    reference = {
        "фотосинтез": "процесс преобразования света в химическую энергию",
        "митоз": "непрямое деление клетки",
        "мейоз": "редукционное деление клеток"
    }
    
    # Создаем тестовый файл студента
    with open("test_answers.txt", "w", encoding="utf-8") as f:
        f.write("Фотосинтез: процесс преобразования света в химическую энергию\n")
        f.write("Митоз: простое деление клетки\n")  # Опечатка
        f.write("Мейоз: редукционное деление клеток\n")
        f.write("Хлоропласт: органоид растительной клетки\n")  # Лишний термин
        f.write("Некорректная строка без разделителя\n")
    
    # Запуск проверки
    print("\n🚀 Запуск тестовой проверки...")
    points, comments = check_answers("test_answers.txt", reference)
    
    # Вывод подробных результатов
    print("\n📝 Детализированный отчет:")
    for comment in comments:
        print(comment)
    
    print(f"\n💯 Итоговая оценка: {points} из {len(reference)} баллов")