
import pandas as pd
import numpy as np

# Исходный датасет
data = pd.DataFrame({
    'Название угрозы': ['System Intrusion', 'System Intrusion', 'System Intrusion', 'Social Engineering', 'Social Engineering', 'Social Engineering','Basic Web-API Attacks', 'Basic Web-API Attacks', 'Basic Web-API Attacks', 'Miscellaneous Errors', 'Miscellaneous Errors', 'Miscellaneous Errors', 'Denial of Service (DoS)', 'Denial of Service (DoS)', 'Denial of Service (DoS)','Privilege Misuse','Privilege Misuse','Privilege Misuse', 'Lost and Stolen Assets', 'Lost and Stolen Assets', 'Lost and Stolen Assets', 'System Intrusion', 'System Intrusion', 'System Intrusion','Social Engineering', 'Social Engineering', 'Social Engineering','Basic Web-API Attacks','Basic Web-API Attacks','Basic Web-API Attacks', 'Miscellaneous Errors', 'Miscellaneous Errors', 'Miscellaneous Errors', 'Denial of Service (DoS)', 'Denial of Service (DoS)', 'Denial of Service (DoS)','Privilege Misuse','Privilege Misuse','Privilege Misuse', 'Lost and Stolen Assets', 'Lost and Stolen Assets', 'Lost and Stolen Assets'],
    'Коэффициент угрозы': [0.49,0.49,0.49, 0.54,0.54, 0.54, 0.93, 0.93,0.93, 0.85, 0.85, 0.85,0.01, 0.01, 0.01, 0.70, 0.70, 0.70, 0.07,0.07, 0.07, 0.49, 0.49,0.49, 0.54, 0.54, 0.54,0.93, 0.93, 0.93,0.85, 0.85, 0.85,0.01, 0.01, 0.01,0.70, 0.70, 0.70, 0.07,0.07, 0.07],
    'Отрасль компании': ['Agriculture', 'Construction', 'Entertainment', 'Entertainment', 'Utilities', 'Wholesale Trade', 'Wholesale Trade', 'Mining', 'Real Estate', 'Real Estate', 'Administrative', 'Transportation', 'Transportation', 'Finance', 'Healthcare', 'Information', 'Manufacturing', 'Accommodation', 'Accommodation', 'Agriculture', 'Entertainment', 'Finance', 'Healthcare', 'Information', 'Manufacturing', 'Professional', 'Public Administration', 'Retail', 'Transportation', 'Utilities', 'Public Administration', 'Retail', 'Transportation', 'Utilities', 'Public Administration', 'Retail', 'Transportation', 'Utilities', 'Public Administration', 'Retail', 'Transportation', 'Utilities'],
    'Коэффициент отрасли': [0.5,0.7,0.2,0.2,0.2,0.5,0.5,0.4,0.6,0.6,0.8,0.3,0.3, 0.3,0.8,0.2,0.2,0.2, 0.2, 0.5,0.2,0.3,0.8,0.2,0.2,0.3, 0.2,0.3,0.3,0.2,0.2,0.3, 0.3,0.2, 0.2,0.3,0.3,0.2,0.2,0.3,0.3, 0.2],
    'Кол-во сотрудников': [100, 300, 80, 120, 400, 150, 70, 200, 100, 300, 150, 80, 60, 80, 90, 15, 80, 40, 100, 20, 60, 80, 40, 15, 40, 30, 90, 80, 60, 20, 70, 100, 15, 28, 41, 17, 54, 23, 38, 12, 150, 84],
    'Регион': ['EMEA', 'APAC', 'NA', 'LAC', 'EMEA', 'NA', 'APAC', 'EMEA', 'NA', 'LAC', 'APAC', 'NA', 'EMEA', 'APAC', 'NA', 'EMEA', 'APAC', 'NA', 'EMEA', 'LAC', 'APAC', 'NA', 'EMEA', 'APAC', 'NA', 'EMEA', 'APAC', 'NA', 'EMEA', 'APAC', 'NA', 'EMEA', 'APAC', 'NA', 'EMEA', 'APAC', 'NA', 'EMEA', 'APAC', 'NA', 'EMEA', 'APAC'],
    'Коэффициент региона': [0.33,0.23,0.41,0.12,0.33, 0.41, 0.23, 0.33, 0.41, 0.12,0.23,0.41, 0.33, 0.23, 0.41,0.33, 0.23,0.41,0.33, 0.12,0.33, 0.41,0.33, 0.33, 0.41,0.25,0.25,0.21, 0.25,0.25,0.21, 0.25, 0.25, 0.21,0.25, 0.25, 0.21,0.25, 0.25,0.21, 0.25, 0.23],
})#0.33, 0.26, 0.41, 0.12
# Рассчитываем вероятность возникновения угрозы
data['Вероятность возникновения угрозы'] = (data['Коэффициент угрозы'] + data['Коэффициент отрасли'] + data['Коэффициент региона'] + data['Кол-во сотрудников'] * 0.001) / 4

# Получаем 5 случайных записей
sample_data = data.sample(n=2000, replace=True, random_state=42)

# Сохраняем в файл
sample_data.to_csv("NewGenerationData.csv", index=False)





















import tkinter as tk
from tkinter import ttk
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

data = pd.read_csv('NewGenerationData.csv')

data = pd.get_dummies(data, columns=['Название угрозы', 'Отрасль компании', 'Регион'])

X = data.drop(columns=['Вероятность возникновения угрозы'])
y = data['Вероятность возникновения угрозы']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

threats = [
    'System Intrusion', 'Social Engineering', 'Basic Web-API Attacks', 'Miscellaneous Errors',
    'Denial of Service (DoS)', 'Privilege Misuse', 'Lost and Stolen Assets'
]
threat_coeffs = [0.49, 0.54, 0.93, 0.85, 0.01, 0.70, 0.07]
industries = [
    'Agriculture', 'Construction', 'Entertainment', 'Utilities', 'Wholesale Trade', 'Mining',
    'Real Estate', 'Administrative', 'Transportation', 'Finance', 'Healthcare', 'Information',
    'Manufacturing', 'Accommodation', 'Professional', 'Public Administration', 'Retail'
]
industry_coeffs = [0.5, 0.7, 0.2, 0.2, 0.5, 0.4, 0.6, 0.8, 0.3, 0.3, 0.8, 0.2, 0.2, 0.2, 0.3, 0.2, 0.3]
regions = ['EMEA', 'APAC', 'NA', 'LAC']
region_coeffs = [0.33, 0.26, 0.41, 0.12]
threat_actions = {
    "Social Engineering": [
        "Обучение персонала правилам безопасности помогает им распознавать и избегать попыток социальной инженерии, увеличивая общий уровень безопасности компании.",
        "Многофакторная аутентификация добавляет дополнительный уровень безопасности, требуя от сотрудников предоставления нескольких форм идентификации при доступе к системам или данным компании.",
        "Регулярная проверка и анализ запросов на доступ к чувствительным данным позволяет быстро обнаруживать и блокировать подозрительную активность."
    ],
    "Denial of Service (DoS)": [
        "Системы предотвращения вторжений (IPS) могут обнаруживать и блокировать попытки DoS-атак, минимизируя их влияние на работу вашей сети.",
        "Фильтрация трафика помогает отсеивать вредоносные запросы до их достижения целевых серверов, снижая вероятность успешной DoS-атаки.",
        "Мониторинг сетевого трафика позволяет быстро обнаруживать аномальную активность, а резервное копирование данных помогает восстановить работоспособность систем после атаки."
    ],
    "Basic Web-API Attacks": [
        "Регулярное обновление и патчинг веб-API позволяет закрывать уязвимости и устранять известные угрозы, снижая риск атак.",
        "API Gateway предоставляет централизованную точку доступа к веб-API, что облегчает контроль доступа и мониторинг активности.",
        "Мониторинг активности веб-API и ведение журналов помогают выявлять аномальную активность и атаки на ранних стадиях."
    ],
    "Privilege Misuse": [
        "Ограничение прав доступа помогает предотвратить злоупотребление привилегиями и снижает возможные последствия компрометации учетных записей.",
        "Регулярные аудиты и мониторинг позволяют отслеживать действия пользователей и выявлять подозрительную или несанкционированную активность.",
        "Системы управления доступом обеспечивают централизованное управление привилегиями и автоматизацию процесса предоставления и отзыва доступа."
    ],
    "Miscellaneous Errors": [
        "Внедрение проверок и валидаций данных позволяет предотвращать ошибки ввода и обработки данных, уменьшая риск возникновения уязвимостей.",
        "Автоматизация процессов помогает уменьшить зависимость от человеческого фактора и снизить вероятность возникновения ошибок.",
        "Регулярное обучение сотрудников позволяет поддерживать их осведомленность о безопасности и обновлять процедуры в соответствии с изменяющимися угрозами."
    ],
    "Lost and Stolen Assets": [
        "Шифрование данных на устройствах помогает предотвратить несанкционированный доступ к чувствительной информации в случае утери или кражи устройства.",
        "Обеспечение физической безопасности активов включает в себя использование замков, меток и других средств для защиты компьютеров, устройств хранения данных и других ценных активов от кражи или несанкционированного доступа.",
        "Процедуры отслеживания и управления устройствами позволяют быстро обнаруживать утерянные или украденные устройства, а также удаленно управлять ими для защиты данных и информации."
    ],
    "System Intrusion": [
        "Регулярное обновление и патчинг систем помогает закрывать известные уязвимости и предотвращать эксплуатацию их злоумышленниками.",
        "Антивирусное ПО и системы обнаружения вторжений помогают обнаруживать и блокировать вредоносное программное обеспечение и злонамеренные действия в системе.",
        "Мониторинг систем и ведение журналов позволяют выявлять аномальную активность, необычные события или подозрительные действия в системе, что помогает предотвращать вторжения и компрометацию."
    ]}
def make_prediction():
    threat = threat_var.get()
    industry = industry_var.get()
    region = region_var.get()
    employees = int(employee_entry.get())
    threat_coeff = threat_coeffs[threats.index(threat)]
    industry_coeff = industry_coeffs[industries.index(industry)]
    region_coeff = region_coeffs[regions.index(region)]
    new_data = pd.DataFrame({
        'Коэффициент угрозы': [threat_coeff],
        'Коэффициент отрасли': [industry_coeff],
        'Кол-во сотрудников': [employees],
        'Коэффициент региона': [region_coeff]

    })
    for column in X.columns:
        if column not in new_data.columns:
            new_data[column] = 0

    predicted_probability = model.predict(new_data)[0]

    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f'Predicted Probability of Threat Occurrence: {predicted_probability:.3f}\n\n')
    actions = threat_actions.get(threat, [])
    result_text.insert(tk.END, f'Recommended Actions for {threat}:\n')
    for action in actions:
        result_text.insert(tk.END, f'- {action}\n')

root = tk.Tk()
root.title("Threat Prediction Interface")
tk.Label(root, text="Выберите угрозу:").grid(row=0, column=0, padx=10, pady=5)
threat_var = tk.StringVar(value=threats[0])
threat_menu = ttk.Combobox(root, textvariable=threat_var, values=threats)
threat_menu.grid(row=0, column=1, padx=10, pady=5)
tk.Label(root, text="Выберите отрасль:").grid(row=1, column=0, padx=10, pady=5)
industry_var = tk.StringVar(value=industries[0])
industry_menu = ttk.Combobox(root, textvariable=industry_var, values=industries)
industry_menu.grid(row=1, column=1, padx=10, pady=5)
tk.Label(root, text="Выберите регион:").grid(row=2, column=0, padx=10, pady=5)
region_var = tk.StringVar(value=regions[0])
region_menu = ttk.Combobox(root, textvariable=region_var, values=regions)
region_menu.grid(row=2, column=1, padx=10, pady=5)
tk.Label(root, text="Введите количество сотрудников:").grid(row=3, column=0, padx=10, pady=5)
employee_entry = tk.Entry(root)
employee_entry.grid(row=3, column=1, padx=10, pady=5)
predict_button = tk.Button(root, text="Сделать прогноз", command=make_prediction)
predict_button.grid(row=4, column=0, columnspan=2, pady=10)
result_text = tk.Text(root, height=20, width=80)
result_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
root.mainloop()