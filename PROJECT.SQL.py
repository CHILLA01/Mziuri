import sqlite3

# გახსნა ბაზის
conn = sqlite3.connect("/mnt/data/book_db (1).sqlite")
cursor = conn.cursor()

# მაგ., ცხრილების სიის გამოყვანა
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", tables)

# მაგალითად, მონაცემების ამოღება რომელიმე ცხრილიდან
cursor.execute("SELECT * FROM books")  # შეცვალე შესაბამისი ცხრილის სახელით
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
