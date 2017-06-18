# Как да стартираме под Windows

## Добавете Python към системния път

За да е достъпен Python през терминала (програмата "Command Prompt"), пътят до
директорията, където е инсталиран Python трябва да се добави към системния път.
Има два начина това да се направи:

 - при инсталация на Python, на първата стъпка има отметка "Add Python 3.5 to PATH" (има го само за новите версии)
 - [следвайте инструкциите] (https://www.webucator.com/blog/wp-content/uploads/2015/03/add-python-to-path.png)

## Изпълнете командите

```
cd week24\todo
pip install virtualenv
virtualenv .env
.env\Scripts\activate
pip install -r requirements.txt
python app.py
```
