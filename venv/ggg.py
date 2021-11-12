import pandas as pd
import openpyxl
name = "Атай"
n = 0
book = openpyxl.load_workbook(filename="Worker.xlsx", data_only=True)
sheet = book["logins"]

while n != "9":
    workers = pd.read_excel("Worker.xlsx", sheet_name="logins", engine="openpyxl")
    work = pd.read_excel("Worker.xlsx", sheet_name="clients", engine="openpyxl")
    n = input("""Выберите действие:
1.Показать список всех зон покрытия
2.Показать список категорий бюджета
3.Показать выделенный бюджет для определенной категории мест для маркетинга
4.Показать текущие средства для маркетинга
5.Показать общий бюджет необходимый для зарплаты
6.Повысить зарплату сотруднику
7.Понизить зарплату сотруднику
8.Показать список оборудований для строительства объектов
9.Выход\n""")
    if n == "1":
        zones = work["Зона"]
        summ = len(zones)
        for i in set(zones):
            num = list(zones).count(i)
            print("Зона охвата клиентами для {} - {}% - {} клиентов".format(i, num/summ*100, num))

    if n == "2":
        print("Бюджет для маркетинга: {}".format(pd.read_excel("Worker.xlsx", sheet_name="budget", engine="openpyxl")["Маркетинг"][0]))
        print("Бюджет для заработной платы: {}".format(sum(workers["Зарплата"])))

    if n == "3":
        zones = work["Зона"]
        for i in set(zones):
            isZone = work["Зона"] == i
            print("Бюджет для зоны {} равен {}".format(i, sum(work[isZone]["Бюджет"])))

    if n == "4":
        print("Бюджет для маркетинга: {}".format(pd.read_excel("Worker.xlsx", sheet_name="budget", engine="openpyxl")["Маркетинг"][0]))

    if n == "5":
        print("Бюджет для заработной платы: {}".format(sum(workers["Зарплата"])))

    if n == "6":
        worker = input("Наберите имя сотрудника которому хотите повысить зарплату: ")
        isExist = False
        for row in range(2, sheet.max_row + 1):
            cell_name = "{}{}".format("B", row)
            if sheet[cell_name].value == worker:
                isExist = True
                break
        if not isExist:
            print("Мы не нашли такого сотрудника")
        else:
            delta = int(input('Наберите сумму надбавки к зарплате: '))
            cell_name = "{}{}".format("D", row)
            sheet[cell_name].value += delta
            book.save("Worker.xlsx")
            print("Надбавка успешно произведено! Текущая зарплата для этого сотрудника после надбавки: {}".format(
                sheet[cell_name].value))

    if n == "7":
        worker = input("Наберите имя сотрудника которому хотите повысить зарплату: ")
        isExist = False
        for row in range(2, sheet.max_row + 1):
            cell_name = "{}{}".format("B", row)
            if sheet[cell_name].value == worker:
                isExist = True
                break
        if not isExist:
            print("Мы не нашли такого сотрудника")
        else:
            delta = int(input('Наберите сумму надбавки к зарплате: '))
            cell_name = "{}{}".format("D", row)
            sheet[cell_name].value -= delta
            book.save("Worker.xlsx")
            print(
                "Понижение зарплаты успешно произведено! Текущая зарплата для этого сотрудника после надбавки: {}".format(
                    sheet[cell_name].value))

    if n == "8":
        print(pd.read_excel("Worker.xlsx", sheet_name="inventory", engine="openpyxl"))
    print("\n=====================================================================================\n")