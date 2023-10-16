import os
import openai
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from settings import Bot_token, GPT_token

openai.api_key = GPT_token

bot = Bot(Bot_token)
dp = Dispatcher(bot)

messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}]

def update(messages, role, content):
    messages.append({'role': role, 'content': content})
    return messages
    
@dp.message_handler()
async def send(message: types.Message):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = messages
)

    await message.answer(response['choices'][0]['message']['content'], parse_mode="markdown")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

