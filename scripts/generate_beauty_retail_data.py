pip install pandas numpy faker

import datetime
import random
import numpy as np
import pandas as pd
from faker import Faker

# Инициализация Faker с британской локалью
fake = Faker('en_GB')
Faker.seed(42)
np.random.seed(42)

# 1. Конфигурация параметров
NUM_CUSTOMERS = 1500
NUM_TRANSACTIONS = 20000
START_DATE = datetime.date(2024, 1, 1)
END_DATE = datetime.date(2026, 3, 1)

UK_CITIES = [
    'Newcastle upon Tyne',
    'London',
    'Manchester',
    'Birmingham',
    'Edinburgh',
    'Leeds',
    'Glasgow',
    'Bristol',
    'Liverpool',
]
CITY_WEIGHTS = [0.25, 0.20, 0.15, 0.10, 0.08, 0.07, 0.05, 0.05, 0.05]

CATEGORIES = {
    'Skincare': [
        ('Hydrating Serum 30ml', 28.00),
        ('SPF 50 Daily Moisturiser', 22.00),
        ('Cleansing Balm 100g', 18.50),
        ('Retinol Night Cream', 35.00),
    ],
    'Haircare': [
        ('Nourishing Shampoo 250ml', 14.00),
        ('Repair Conditioner 250ml', 14.00),
        ('Hair Repair Oil 50ml', 26.00),
    ],
    'Makeup': [
        ('Volumising Mascara', 16.00),
        ('Matte Lipstick', 19.00),
        ('Radiant Foundation 30ml', 32.00),
    ],
    'Fragrance': [
        ('Eau de Parfum 50ml', 65.00),
        ('Floral Body Mist 100ml', 15.00),
    ],
    'Body Care': [
        ('Exfoliating Body Scrub', 12.50),
        ('Rich Body Butter 200ml', 16.50),
    ],
}

# 2. Генерация клиентов
customers = []
for i in range(1, NUM_CUSTOMERS + 1):
    signup_date = fake.date_between(start_date=START_DATE, end_date=END_DATE)
    customers.append({
        'Customer_ID': f'CUST_{i:05d}',
        'City': np.random.choice(UK_CITIES, p=CITY_WEIGHTS),
        'Gender': np.random.choice(
            ['Female', 'Male', 'Non-Binary'], p=[0.75, 0.20, 0.05]
        ),
        'Signup_Date': signup_date,
    })

df_customers = pd.DataFrame(customers)

# 3. Генерация транзакций
transactions = []
all_categories = list(CATEGORIES.keys())

for i in range(1, NUM_TRANSACTIONS + 1):
    customer = df_customers.sample(1).iloc[0]
    cust_id = customer['Customer_ID']
    cust_signup = customer['Signup_Date']

    # Дата транзакции не может быть раньше даты регистрации
    tx_date = fake.date_between(start_date=cust_signup, end_date=END_DATE)

    category = random.choice(all_categories)
    product_name, unit_price = random.choice(CATEGORIES[category])

    quantity = np.random.choice([1, 2, 3, 4], p=[0.70, 0.20, 0.07, 0.03])
    channel = np.random.choice(['Online Store', 'Mobile App'], p=[0.55, 0.45])

    # Скидки по промокодам (в 30% случаев)
    discount = (
        round(unit_price * quantity * random.choice([0.10, 0.15, 0.20]), 2)
        if random.random() < 0.3
        else 0.0
    )
    total_spent = round((unit_price * quantity) - discount, 2)

    transactions.append({
        'Transaction_ID': f'TXN_{i:07d}',
        'Customer_ID': cust_id,
        'Transaction_Date': tx_date,
        'Channel': channel,
        'Category': category,
        'Product_Name': product_name,
        'Quantity': quantity,
        'UnitPrice_GBP': unit_price,
        'Discount_Amount_GBP': discount,
        'Total_Spent_GBP': total_spent,
    })

df_transactions = pd.DataFrame(transactions)

# Объединение в один датасет
df_final = df_transactions.merge(df_customers, on='Customer_ID', how='left')

# Сохранение в CSV
df_final.to_csv('uk_beauty_retail_dataset.csv', index=False)
print(
    f'Успешно сгенерировано {len(df_final)} строк! Файл сохранен как uk_beauty_retail_dataset.csv'
)
