@echo OFF
start "Django Server" python manage.py runserver
start "Discord Bot" python discord_bot/bot.py