

def total_salary(path):
    with open(path, 'r') as fh:
        pass

def main():
    total, average = total_salary("salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

if __name__ == '__main__':
    main()