import telebot
from telebot import types
from newsapi import NewsApiClient
from application import get_from_env

bot = telebot.TeleBot(get_from_env('TELEGRAM_BOT_TOKEN'))
newsapi = NewsApiClient(api_key=get_from_env('NEWS_API_KEY'))


def response_news_api_handler(res, message):
    articles = res.get('articles')

    if not res or type(res) != dict or len(articles) == 0:
        bot.send_message(message.from_user.id, f"Did't find anything with {message.text} title")

    bot.send_message(message.from_user.id, f"Here what i have found 👇")

    for article in articles:
        bot.send_message(message.from_user.id, '--------------------')
        bot.send_message(message.from_user.id,
                         f'*{article.get("title")}*\n' + f'\n{article.get("description")}' + f'\n{article.get("content")}[read more]({article.get("url")})',
                         parse_mode='Markdown')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "👋 Hi! Let's type a topic keyword, you are interested in")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    top_headlines = newsapi.get_top_headlines(q=f'{message.text}',
                                              sources='bbc-news,the-verge',
                                              language='en')
    response_news_api_handler(top_headlines, message)


bot.polling(none_stop=True, interval=0)
