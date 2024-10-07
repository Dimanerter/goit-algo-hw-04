def total_salary(path):
    # обработка исключения когда файл не найден или поврежден
    try:
        # безопасное открытие файла
        with open(path, 'r', encoding="utf-8") as fh:
            # создание списка со строками
            lines = [el.strip() for el in fh.readlines()]
            salarys =[]
            for line in lines:
                # Заполнение списка, где будут тоько числовые значения зарплат
                salarys.append(line.split(',')[1])
        # закрытие файла
        fh.close()
        total = 0
        for salary in salarys:
                #Сумма всех зарплат работников
                total += int(salary)
        # Среднее значение зарплат
        average = int(total/len(salarys))
        result = (total, average)
        return result
    except FileNotFoundError:
         # Если файл не найден то программа возвращает 0, 0 и выводит "File not found"
         print("File not found")
         result = (0,0)
         return result
    except UnicodeDecodeError:
         # Если файл не найден то программа возвращает 0, 0 и выводит "The file is corrupted or cannot be read"
         print("The file is corrupted or cannot be read")
         result = (0,0)
         return result

def main():
    total, average = total_salary("salary_file.txt")
    if total and average:
         print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

if __name__ == '__main__':
    main()