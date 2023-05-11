from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "13976276"))
API_HASH = getenv("API_HASH", "7f024cbc744a2f44569c3641b5ccecb7")

BOT_TOKEN = getenv("BOT_TOKEN", "6052195748:AAFpuknQjZ9OOnqoTKoL2515BhhneWW_ZRI")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6008136265"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/b2258dbee2401c426eb3c.jpg")

SESSION = getenv("SESSION", "BQCt7yLuHRP5IXO66b7My80q4-cd1uIJxgNTU1R3391WSIULfnXWJOvJxREGEQa-xaYkUAM4mkKdCN35DqljR_qsAF-OkjB3xwSWRteM9Iqr4_E4f9AeXHAayO3tyYIOd7nvLdFLhiveqONQZfjDTUpgCX0U2tB-_8eplWja5WUKJAFQyzANivHrIods_t74ZgNar_dNNZr9OIKLMX-Qwi1FChXzeFL6At6DM0-9ZrEcdhJUOF_tqgDgPaoqBKw38oxD9IcCmqqbSUzeteGnjxE3KueUUuTsUm1pxKS0wg83ytXOj9GCo_LzNSszROECIJTYO1pHdJm55KmyQOkfN5HsAAAAAUgLerAA") 

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/indian_chatting_club_offical")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "http://t.me/tha_govind_op")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6020570673").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
