from tg_bot.sample_config import Config


class Development(Config):
    
    LOGGER = True

    # REQUIRED
    API_KEY = "Y1423025003:AAENDAZ48eooLxNpxrPR7zwIbvejJZmvXbE"
    OWNER_ID = "1131653685"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "kavinduaj"
    OWNER_NAME = "Kavindu AJ "

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgresql://kaj117:dkkaj0123456@postgresql/postgres'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    START_PHOTTO = 'https://telegra.ph/file/7703ef03a791f158e28db.jpg' # Any img Url To shown In the Start Menu
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = [1131653685]  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = [1131653685]  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = [1131653685]  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    ALLOW_EXCL = False  # Allow ! commands as well as /
