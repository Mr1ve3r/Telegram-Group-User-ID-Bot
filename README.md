# Telegram Group/User ID Bot

A simple Pyhton bot for getting ID's
On "/start" sends:
- in private chat: user ID;
- in a group chat: group ID

## Deploy
1. Install Python (Linux)
   ```bash
   apt install python
   ```

3. Install environment:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   pip install -r requirements.txt
   ```
   
4. Create ```.env``` file and paste variable and your bot token: 
   ```
   BOT_TOKEN=Your_bot_token_here
   ```
   
5. Start bot
   ```bash
   python bot.py
   ```

## Usage
- `/start` the bot to get your user ID;
- Add bot just like a group chat member, grant rights to read messages (tip: if the bot can read messages, it will be stated in the group chat members list). Then, send `/start` to the chat (if there are many chats in the group (a supergroup) you can send `/start` in whatever chat you want). That's how you can get the group ID

