#!/usr/bin/env python3

import random

class MathTrainer:
    def __init__(self):
        self.score = 0
        self.total_questions = 0
        
    def generate_question(self):
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
    
    def check_answer(self, user_answer, correct_answer):
        try:
            return int(user_answer) == correct_answer
        except ValueError:
            return False
    
    def run(self):
        print("Добро пожаловать в Тренажер устного счета!")
        print("Решайте примеры. Для выхода введите 'quit или выйти'")
        print("-" * 40)
        
        while True:
            question, correct_answer = self.generate_question()
            
            user_input = input(f"Сколько будет: {question}? ")
            
            if user_input.lower() == 'quit' or user_input.lower() == 'выйти':
                 break
                
            self.total_questions += 1  # ← ПЕРЕМЕСТИЛИ СЮДА!
                
            if self.check_answer(user_input, correct_answer):
                print("✅ Правильно!")
                self.score += 1
            else:
                print(f"❌ Неправильно! Правильный ответ: {correct_answer}")
            
            print()
        
        self.show_results()
    
    def show_results(self):
        print("=" * 40)
        print("🏆 Тренировка завершена!")
        print(f"Ваш результат: {self.score}/{self.total_questions}")
        
        if self.total_questions > 0:
            percentage = (self.score / self.total_questions) * 100
            print(f"Процент правильных ответов: {percentage:.1f}%")
        
            if percentage >= 80:
                print("🎉 Отличный результат!")
            elif percentage >= 60:
                print("👍 Хороший результат!")
            else:
                print("Пупупу...")

if __name__ == "__main__":
    trainer = MathTrainer()  
    trainer.run()
    