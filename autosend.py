import logging
import os
import random
import time

import requests
from dotenv import load_dotenv

# --- SETUP LOGGING ---
# Ini bakal bikin file 'bot.log' dan nyatet semua aktivitas bot beserta waktunya
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("bot.log"),  # Nyimpen log ke file bot.log
        logging.StreamHandler()          # Nampilin log di terminal juga
    ]
)

# Load environment variables dari file .env
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = os.getenv("DISCORD_CHANNEL_ID")
CHANNEL_ID_SURGE = os.getenv("DISCORD_CHANNEL_ID_SURGE")

# Variasi chat
chat_1 = """CHEAP SURG TOOLS AT <:Arrow:850540193626193941> HereCheapSurg

<:SurgicalStitches:892136728607985734> Surgical Stitches 1/ <:WL:880251447470596157>
<:SurgicalAnesthetic:892136763718512642> Surgical Anesthetic 10/ <:WL:880251447470596157>
<:SurgicalAntibiotics:892136764045684787> Surgical Antibiotics 8/ <:WL:880251447470596157>
<:SurgicalAntiseptic:892136764058255431> Surgical Antiseptic 10/ <:WL:880251447470596157>
<:SurgicalClamp:892136728104685628> Surgical Clamp 10/ <:WL:880251447470596157>
<:SurgicalDefibrillator:892136728511533076> Surgical Defibrillator 10/ <:WL:880251447470596157>
<:SurgicalLabKit:892136728566071367> Surgical Labkit 10/ <:WL:880251447470596157>
<:SurgicalPins:892136728566063104> Surgical Pins 10/ <:WL:880251447470596157>
<:SurgicalScalpel:958337498742935552> Surgical Scalpel 8/ <:WL:880251447470596157>
<:SurgicalSplint:892136728645746688> Surgical Splint 10/ <:WL:880251447470596157>
<:SurgicalSponge:892136728591216700> Surgical Sponge 8/ <:WL:880251447470596157>
<:SurgicalTransfusion:892136795712659516> Surgical Transfusion 10/ <:WL:880251447470596157>
<:SurgicalUltrasound:892136795570065489> Surgical Ultrasound 10/ <:WL:880251447470596157>

ALWAYS RESTOCK NON STOP, SO MINE NEVER SOLD👌

CHEAP SURG TOOLS AT <:Arrow:850540193626193941> HereCheapSurg"""

chat_2 = """CHEAP SURG TOOLS AT <:Arrow:850540193626193941> HereCheapSurg

<:SurgicalStitches:892136728607985734> Surgical Stitches 1/ <:WL:880251447470596157>
<:SurgicalAnesthetic:892136763718512642> Surgical Anesthetic 10/ <:WL:880251447470596157>
<:SurgicalAntibiotics:892136764045684787> Surgical Antibiotics 8/ <:WL:880251447470596157>
<:SurgicalAntiseptic:892136764058255431> Surgical Antiseptic 10/ <:WL:880251447470596157>
<:SurgicalClamp:892136728104685628> Surgical Clamp 10/ <:WL:880251447470596157>
<:SurgicalDefibrillator:892136728511533076> Surgical Defibrillator 10/ <:WL:880251447470596157>
<:SurgicalLabKit:892136728566071367> Surgical Labkit 10/ <:WL:880251447470596157>
<:SurgicalPins:892136728566063104> Surgical Pins 10/ <:WL:880251447470596157>
<:SurgicalScalpel:958337498742935552> Surgical Scalpel 8/ <:WL:880251447470596157>
<:SurgicalSplint:892136728645746688> Surgical Splint 10/ <:WL:880251447470596157>
<:SurgicalSponge:892136728591216700> Surgical Sponge 8/ <:WL:880251447470596157>
<:SurgicalTransfusion:892136795712659516> Surgical Transfusion 10/ <:WL:880251447470596157>
<:SurgicalUltrasound:892136795570065489> Surgical Ultrasound 10/ <:WL:880251447470596157>

🔥 STOCK ALWAYS READY! NEVER SOLD OUT 🔥

VISIT NOW <:Arrow:850540193626193941> HereCheapSurg"""

chat_list = [chat_1, chat_2]



chat_surge ="Sell Cheap Surg E 1/:WL: at HereCheapSurg"

# func chat surg-e
def send_messagesurge():
    if not TOKEN or not CHANNEL_ID_SURGE:
        logging.error("TOKEN atau CHANNEL_ID_SURGE tidak ditemukan di file .env")
        return False

    url = f"https://discord.com/api/v9/channels/{CHANNEL_ID_SURGE}/messages"

    headers = {
        "Authorization": TOKEN,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    pesan = chat_surge
    payload = {"content": pesan}

    try:
        res = requests.post(url, headers=headers, json=payload)
        if res.status_code == 200:
            logging.info("Sukses ngirim pesan promosi surg-e.")
            return True
        else:
            logging.error(f"Gagal ngirim, status: {res.status_code} - {res.text}")
            return False
    except Exception as e:
        logging.error(f"Koneksi/Script Error: {e}")
        return False

# func chat surg tools
def send_message():
    if not TOKEN or not CHANNEL_ID:
        logging.error("TOKEN atau CHANNEL_ID tidak ditemukan di file .env")
        return False

    url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages"

    headers = {
        "Authorization": TOKEN,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    pesan = random.choice(chat_list)
    payload = {"content": pesan}

    try:
        res = requests.post(url, headers=headers, json=payload)
        if res.status_code == 200:
            logging.info("Sukses ngirim pesan promosi surg tools.")
            return True
        else:
            logging.error(f"Gagal ngirim, status: {res.status_code} - {res.text}")
            return False
    except Exception as e:
        logging.error(f"Koneksi/Script Error: {e}")
        return False

# --- MAIN LOOP ---
logging.info("Bot Auto-Chat Dimulai...")

while True:
    while not send_message():
        logging.warning("Gagal ngirim pesan promosi surg tools, mencoba lagi dalam 60 detik...")
        time.sleep(60)

    delay = random.randint(5, 15)
    logging.info(f"Nunggu {delay} detik sebelum ngirim chat surg-e...")
    time.sleep(delay)

    while not send_messagesurge():
        logging.warning("Gagal ngirim pesan promosi surg-e, mencoba lagi dalam 60 detik...")
        time.sleep(60)

    jeda_tambahan = random.randint(60, 900)
    total_jeda = 7200 + jeda_tambahan

    menit = total_jeda // 60
    logging.info(f"Nunggu {menit} menit buat chat berikutnya...")
    time.sleep(total_jeda)