import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", "26728872"))
API_HASH = os.environ.get("API_HASH", "96985c2aaea6c75408528909b7e18879")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7825342391:AAHcA9HPcf2uEzKWlZwTHKxIksPwIRvPNX4")
ADMIN = int(os.environ.get("ADMIN", "1705634892"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", " -1002226481922")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002288135729"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://zoneunknown745:oPlpsH5OxkVuc5Wq@cluster0.kyw2p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "TechifyBots")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/ada3f739fed7efdbe7b08.jpg")
