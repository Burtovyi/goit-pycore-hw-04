def total_salary(path):
    total_salary = 0
    count = 0
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    name, salary_str = line.split(',')
                    salary = float(salary_str)
                    total_salary += salary
                    count += 1
                except ValueError:
                    print(f"Неправильний формат рядка: {line}")
                    continue
        if count == 0:
            average_salary = 0
        else:
            average_salary = total_salary / count
        return (total_salary, average_salary)
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return (0, 0)
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return (0, 0)

total, average = total_salary("text.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")