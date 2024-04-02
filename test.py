import secrets

# Генерация случайной строки длиной 24 символа
secret_key = secrets.token_hex(24)
print(secret_key)
