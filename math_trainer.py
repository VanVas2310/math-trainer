#!/usr/bin/env python3
import random

def generate_question():
    operations = ['+', '-', '*']
    operation = random.choice(operations)
    
    if operation == '+':
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        answer = a + b
    elif operation == '-':
        a = random.randint(1, 100)
        b = random.randint(1, a)
        answer = a - b
    else:
        a = random.randint(2, 12)
        b = random.randint(2, 12)
        answer = a * b
        
    question = f"{a} {operation} {b}"
    return question, answer

def check_answer(user_answer, correct_answer):
    try:
        return int(user_answer) == correct_answer
    except ValueError:
        return False


score = 0
total_questions = 0

print("Добро пожаловать в Тренажер устного счета!")
print("Решайте примеры. Для выхода введите 'quit' или 'выйти'")
print("-" * 40)

while True:
    question, correct_answer = generate_question()
    
    user_input = input(f"Сколько будет: {question}? ")
    
    if user_input.lower() == 'quit' or user_input.lower() == 'выйти':
        break
        
    total_questions += 1
        
    if check_answer(user_input, correct_answer):
        print("✅ Правильно!")
        score += 1
    else:
        print(f"❌ Неправильно! Правильный ответ: {correct_answer}")
    
    print()

print("=" * 40)
print("🏆 Тренировка завершена!")
print(f"Ваш результат: {score}/{total_questions}")

if total_questions > 0:
    percentage = (score / total_questions) * 100
    print(f"Процент правильных ответов: {percentage:.1f}%")

    if percentage >= 80:
        print("🎉 Отличный результат!")
    elif percentage >= 60:
        print("👍 Хороший результат!")
    else:
        print("Пупупу...")
