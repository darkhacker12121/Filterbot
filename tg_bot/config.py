from tg_bot.sample_config import Config


class Development(Config):
    API_KEY = "1423025003:AAENDAZ48eooLxNpxrPR7zwIbvejJZmvXbE"
    OWNER_ID = "1131653685"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "kavinduaj"
    OWNER_NAME = "KAVINDU AJ"
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:dkkaj0123456@postgresql/postgres'  # sample db credentials
    MESSAGE_DUMP = -1001329348574
    SUDO_USERS = [1131653685]  # List of id's for users which have sudo access to the bot.
    START_PHOTTO = 'https://telegra.ph/file/7703ef03a791f158e28db.jpg'
    SUPPORT_USERS = [1131653685]
    WHITELIST_USERS = [1131653685]  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    STRICT_GBAN = True
    ALLOW_EXCL = True
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'
    DEL_CMDS = True
    WEBHOOK = 'ANYTHING'

    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    
class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
