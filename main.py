class ChatBotDnD:
    def __init__(self):
        self.state = 'help'

    def respond(self, user_input):
        if self.state == 'help':
            return self.help_state(user_input)
        elif self.state == 'options':
            return self.options_state(user_input)
        elif self.state == 'quit':
            return self.quit_state(user_input)
        elif self.state == 'find':
            return self.find_state(user_input)
        else:
            return self.error_state(user_input)

    def help_state(self, user_input):
        if user_input.lower() in ['книга', 'книги', 'найти книгу', 'купить книгу', 'покупка книги', 'поиск книги']:
            self.state = 'options'
            return "Выберите вариант:\n1. Купить новую книгу\n2. Найти книгу в личной библиотеке"
        elif user_input.lower() in ['ничего', 'все в порядке', 'все хорошо']:
            self.state = 'quit'
            return "Рад был помочь! Если возникнут вопросы - обращайтесь."
        else:
            return "Извините, я не понимаю. Пожалуйста, уточните вопрос."

    def options_state(self, user_input):
        if user_input == '1':
            self.state = 'quit'
            return "Перейдите по ссылке https://www.chitai-gorod.ru/"
        elif user_input == '2':
            self.state = 'find'
            return "Введите название"
        else:
            return "Пожалуйста, выберите одну из предложенных опций (1 или 2)."

    def find_state(self, user_input):
        if user_input.lower() in ['братья карамазовы', 'преступление и наказание', 'дон кихот', 'война и мир']:
            self.state = 'quit'
            return "Полка 1"
        elif user_input.lower() in ['голубой карбункул', 'человек на четвереньках', 'десять негритят', 'чудо полумесяца']:
            self.state = 'quit'
            return "Полка 2"
        else:
            self.state = 'quit'
            return "Книга не найдена"

    def quit_state(self, user_input):
        self.state = 'help'
        return "Сессия завершена. Если возникнет необходимость - пишите снова."


if __name__ == "__main__":
    bot = ChatBotDnD()
    print("Бот: Для завершения введите 'выход'. Что вас интересует?")
    while True:
        user_input = input("Вы: ")
        if user_input.lower() == 'выход':
            print ("Бот: Спасибо за обращение. Если возникнут проблемы, обращайтесть.")
            break
        print("Бот:", bot.respond(user_input))

"""
Пример работы:
    
Бот: Для завершения введите 'выход'. Что вас интересует?
Вы: rybuf
Бот: Извините, я не понимаю. Пожалуйста, уточните вопрос.
Вы: книга
Бот: Выберите вариант:
1. Купить новую книгу
2. Найти книгу в личной библиотеке
Вы: 1
Бот: Перейдите по ссылке https://www.chitai-gorod.ru/
Вы: 
Бот: Сессия завершена. Если возникнет необходимость - пишите снова.
Вы: найти книгу
Бот: Выберите вариант:
1. Купить новую книгу
2. Найти книгу в личной библиотеке
Вы: 2
Бот: Введите название
Вы: человек на четвереньках
Бот: Полка 2
Вы: 
Бот: Сессия завершена. Если возникнет необходимость - пишите снова.
Вы: выход
Бот: Спасибо за обращение. Если возникнут проблемы, обращайтесть.


"""