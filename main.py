import asyncio
import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from aiogram.filters import Command

logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher()

coding_tasks = [
    "Напишите функцию, которая проверяет, является ли строка палиндромом.",
    "Создайте программу, которая находит сумму всех чисел в списке.",
    "Реализуйте алгоритм сортировки пузырьком.",
    "Напишите функцию, которая принимает два числа и возвращает их наибольший общий делитель.",
    "Реализуйте класс для работы с комплексными числами.",
    "Создайте программу, которая генерирует таблицу умножения для числа, введенного пользователем.",
    "Напишите функцию, которая конвертирует десятичное число в двоичное представление.",
    "Реализуйте функцию, которая определяет, является ли число простым."
]

@dp.message(Command("start"))
async def bot_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}! Я помогу с учебными задачами по программированию!\n\n"
        f"Напиши /help, чтобы узнать доступные команды."
    )

@dp.message(Command("help"))
async def bot_help(message: Message):
    await message.answer(
        "Доступные команды:\n"
        "/start - Начать работу с ботом\n"
        "/help - Список команд\n"
        "/task - Получить случайную задачу по программированию"
    )

@dp.message(Command("task"))
async def generate_task(message: Message):
    task = random.choice(coding_tasks)
    await message.answer(f"🤔 Вот ваша задача:\n<b>{task}</b>")

@dp.message()
async def echo_message(message: Message):
    await message.answer("Я не понимаю ваш запрос. Напишите /help для списка доступных команд.")

async def main():
    logging.info("Бот запущен и готов к работе!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
