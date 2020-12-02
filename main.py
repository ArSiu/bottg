import aiogram
import asyncio
import random

from aiogram import Bot, Dispatcher #import
from aiogram.types import Message

token = '1425269848:AAEtMvryEcO_w_HDQ-8eey8GnNQFz694ooI'
#key

bot = Bot(token)
dispatcher = Dispatcher(bot)
#objects

@dispatcher.message_handler(commands=["ping"])
async def echo(msg: Message):
    return await msg.reply("pong")

@dispatcher.message_handler(commands=["ball"])
async def sent_ball(msg: Message):
    return await msg.reply_photo("https://www.google.com/imgres?imgurl=https%3A%2F%2Fcdn11.bigcommerce.com%2Fs-5ig7x53cx8%2Fimages%2Fstencil%2F1280x1280%2Fproducts%2F2805%2F5906%2FME-4024-Sports-Ball-Soccer-2__49617.1539788684.png%3Fc%3D2&imgrefurl=https%3A%2F%2Fproadv.com%2Fapollo-sports-soccer-ball-2%2F&tbnid=lNNlaU61sfgP9M&vet=12ahUKEwic-d2D86_tAhXSBXcKHVKRBhYQMygOegUIARCjAg..i&docid=sNQ8ohLQeOnnTM&w=1280&h=1280&q=ball&ved=2ahUKEwic-d2D86_tAhXSBXcKHVKRBhYQMygOegUIARCjAg")

@dispatcher.message_handler(commands=["randballs"])
async def random_ball(msg: Message):
    ball_img = [
        r"C:\Users\ars\Desktop\Bot\bottg\img\pic1.jpg",
        r"C:\Users\ars\Desktop\Bot\bottg\img\pic2.jpg",
        r"C:\Users\ars\Desktop\Bot\bottg\img\pic3.jpg"
    ]
    random_ball_number = random.choice(ball_img)
    return await msg.reply_photo(open(random_ball_number, 'rb').read())


asyncio.run(dispatcher.start_polling())
#msg.from_user.full_name
