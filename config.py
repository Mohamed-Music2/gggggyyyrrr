import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BAAokFYkNkouh3MyD9WJzi6L-J5Kh_p1qRCj5KUluNf4Dvcl8YniPxTvqyCgeGKLQcAZSTxIC_ixRHwoDsls3IX4iDwR4y2OAhvdYJvFO6w4OyRunLg4R5hEH0AWzTFe_SLSdqNOIcB7YnbPebTljrCi4-YNm99oU9OGuqt_glN74Xz2J1EFWVXdx5rehErxH3WprgwhZjXWyqh-IiaZoWION15eSfScfhtTlsVOPaHh9lpPAriVDsd5i8Ktq3kyfjMpP1bJZAVbf1jG9H1j2RUV8YiTLaEITPxQvusecD5xPOOOa9VZAaq5YVjdZgo80khY5S5SbSsf94_QK3rJ9jNJAAAAAS2FcekA")
BOT_TOKEN = getenv("BOT_TOKEN", "5409818512:AAHNVmbdbgAV_NBWmRl3cpU7Wpp2rWDzpz4")
BOT_NAME = getenv("BOT_NAME", "teamesisamusic")
API_ID = int(getenv("API_ID", "16050450"))
API_HASH = getenv("API_HASH", "0dd89e225b6ddd6f03e8135460d31177")
OWNER_NAME = getenv("OWNER_NAME", "lMl4ll")
ALIVE_NAME = getenv("ALIVE_NAME", "lMl4ll_MUSIC")
BOT_USERNAME = getenv("BOT_USERNAME", "lMl4ll_MUSIC_BOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "lMl4ll_MUSIC")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "bareisa")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "D_o_m_A12")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5191100896").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Mohamed-Music2/gggggyyyrrr")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
