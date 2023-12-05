![](http://ForTheBadge.com/images/badges/made-with-python.svg) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com) <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Selenium_logo.svg/2560px-Selenium_logo.svg.png" width="145"/>

### Instagram Reels Downloader
this is simple instagram reels downloader using  ```python + selenium + pyTelegramBotAPI```. In this example it uses a telegram bot to send the downloaded reels

#### Instalation
clone this repo to your local machine using git

```bash
git clone https://github.com/ahmadrivaldi-arv/reels-downloader.git
```
Or manually download this repo as zip [here](https://github.com/ahmadrivaldi-arv/reels-downloader/archive/refs/heads/main.zip)

Go to folder
```bash
cd reels-downloader
```
Install the dependencies
```bash
python3 pip install -r requirements
```

#### Setup the Telegram Bot Token

if you're using telegram bot paste your bot token in this line

open file ```src/main.py``` and replace the ```<your_token``` with your bot token

```python
bot = telebot.TeleBot("<your_token>", parse_mode=None)
```

#### Running the Bot

type this command in your terminal

```bash
python3 src/main.py
```
