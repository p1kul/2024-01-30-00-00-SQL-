import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS USERS(
id INTEGER PRIMAL KEY, 
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

for i in range(1,11):
    cursor.execute('INSERT INTO USERS (id,username, email, age, balance) VALUES (?,?, ?, ?, ?)', (f'{i}',f'User{i}',f'example{i}@gmail.com',f'{i*10}','1000'))

for i in range(1,11,2):
    cursor.execute('UPDATE USERS SET balance = ? WHERE username = ?',(500,f'User{i}'))

for i in range(1,11,3):
    cursor.execute('DELETE FROM USERS WHERE username = ?', (f'User{i}',))

cursor.execute('SELECT * FROM Users WHERE age != ?',('60',))
users = cursor.fetchall()

for user in users:
    print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')

cursor.execute('DELETE FROM USERS WHERE id = ?',('6',))

cursor.execute('SELECT COUNT(*) FROM USERS')
total_users = cursor.fetchone()[0]

cursor.execute('SELECT SUM(balance) FROM USERS')
all_balances = cursor.fetchone()[0]

print(all_balances / total_users)
connection.commit()
connection.close()