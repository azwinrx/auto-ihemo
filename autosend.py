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

TOKEN1 = os.getenv("DISCORD_TOKEN")
TOKEN2 = os.getenv("DISCORD_TOKEN2")
CHANNEL_ID = os.getenv("DISCORD_CHANNEL_ID")
CHANNEL_ID_SURGE = os.getenv("DISCORD_CHANNEL_ID_SURGE")

# Variasi chat
chat_1 = """CHEAP SURG TOOLS AT <:Arrow:850540193626193941> HereCheapSurg

<:SurgicalStitches:892136728607985734> Surgical Stitches 1/ <:WL:880251447470596157>
<:SurgicalAnesthetic:892136763718512642> Surgical Anesthetic 12/ <:WL:880251447470596157>
<:SurgicalAntibiotics:892136764045684787> Surgical Antibiotics 10/ <:WL:880251447470596157>
<:SurgicalAntiseptic:892136764058255431> Surgical Antiseptic 12/ <:WL:880251447470596157>
<:SurgicalClamp:892136728104685628> Surgical Clamp 12/ <:WL:880251447470596157>
<:SurgicalDefibrillator:892136728511533076> Surgical Defibrillator 12/ <:WL:880251447470596157>
<:SurgicalLabKit:892136728566071367> Surgical Lab Kit 12/ <:WL:880251447470596157>
<:SurgicalPins:892136728566063104> Surgical Pins 12/ <:WL:880251447470596157>
<:SurgicalScalpel:958337498742935552> Surgical Scalpel 10/ <:WL:880251447470596157>
<:SurgicalSplint:892136728645746688> Surgical Splint 12/ <:WL:880251447470596157>
<:SurgicalSponge:892136728591216700> Surgical Sponge 10/ <:WL:880251447470596157>
<:SurgicalTransfusion:892136795712659516> Surgical Transfusion 12/ <:WL:880251447470596157>
<:SurgicalUltrasound:892136795570065489> Surgical Ultrasound 12/ <:WL:880251447470596157>

ALWAYS RESTOCK NON STOP, SO MINE NEVER SOLD👌

CHEAP SURG TOOLS AT <:Arrow:850540193626193941> HereCheapSurg"""

chat_2 = """CHEAP SURG TOOLS AT <:Arrow:850540193626193941> HereCheapSurg

<:SurgicalStitches:892136728607985734> Surgical Stitches 1/ <:WL:880251447470596157>
<:SurgicalAnesthetic:892136763718512642> Surgical Anesthetic 12/ <:WL:880251447470596157>
<:SurgicalAntibiotics:892136764045684787> Surgical Antibiotics 10/ <:WL:880251447470596157>
<:SurgicalAntiseptic:892136764058255431> Surgical Antiseptic 12/ <:WL:880251447470596157>
<:SurgicalClamp:892136728104685628> Surgical Clamp 12/ <:WL:880251447470596157>
<:SurgicalDefibrillator:892136728511533076> Surgical Defibrillator 12/ <:WL:880251447470596157>
<:SurgicalLabKit:892136728566071367> Surgical Lab Kit 12/ <:WL:880251447470596157>
<:SurgicalPins:892136728566063104> Surgical Pins 12/ <:WL:880251447470596157>
<:SurgicalScalpel:958337498742935552> Surgical Scalpel 10/ <:WL:880251447470596157>
<:SurgicalSplint:892136728645746688> Surgical Splint 12/ <:WL:880251447470596157>
<:SurgicalSponge:892136728591216700> Surgical Sponge 10/ <:WL:880251447470596157>
<:SurgicalTransfusion:892136795712659516> Surgical Transfusion 12/ <:WL:880251447470596157>
<:SurgicalUltrasound:892136795570065489> Surgical Ultrasound 12/ <:WL:880251447470596157>

🔥 STOCK ALWAYS READY! NEVER SOLD OUT 🔥

VISIT NOW <:Arrow:850540193626193941> HereCheapSurg"""

chat_list = [chat_1, chat_2]



chat_surge ="""sell Surg E 1/ <:WL:880251447470596157> at HereCheapSurg"""

# func chat surg-e
def send_messagesurge(token, channel_id):
    if not token or not channel_id:
        logging.error("TOKEN atau CHANNEL_ID_SURGE tidak ditemukan di file .env")
        return False

    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"

    headers = {
        "Authorization": token,
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
def send_message(token, channel_id):
    if not token or not channel_id:
        logging.error("TOKEN atau CHANNEL_ID tidak ditemukan di file .env")
        return False

    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"

    headers = {
        "Authorization": token,
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

#Kirim akun 1
    if not send_message(TOKEN1, CHANNEL_ID):
        logging.warning("Gagal ngirim pesan promosi surg tools, sleep 15 detik")
        time.sleep(15)

    delay = random.randint(1, 60)
    logging.info(f"Nunggu {delay} detik sebelum ngirim chat surg-e...")
    time.sleep(delay)

    if not send_messagesurge(TOKEN1, CHANNEL_ID_SURGE):
        logging.warning("Gagal ngirim pesan promosi surg-e, sleep 15 detik")
        time.sleep(15)
    
    jeda_tambahan = random.randint(60, 600) 
    total_jeda = 3600 + jeda_tambahan

    menit = total_jeda // 60
    detik = total_jeda % 60
    logging.info(f"Nunggu {menit} menit {detik} detik buat chat di akun berikutnya...")
    time.sleep(total_jeda)

# Kirim akun 2
    if not send_message(TOKEN2, CHANNEL_ID):
        logging.warning("Gagal ngirim pesan promosi surg tools, sleep 15 detik")
        time.sleep(15)

    delay = random.randint(1, 60)
    logging.info(f"Nunggu {delay} detik sebelum ngirim chat surg-e...")
    time.sleep(delay)

    if not send_messagesurge(TOKEN2, CHANNEL_ID_SURGE):
        logging.warning("Gagal ngirim pesan promosi surg-e, sleep 15 detik")
        time.sleep(15)

    jeda_tambahan = random.randint(60, 600)
    total_jeda = 3600 + jeda_tambahan
    menit = total_jeda // 60
    detik = total_jeda % 60
    logging.info(f"Nunggu {menit} menit {detik} detik buat chat di akun berikutnya...")
    time.sleep(total_jeda)

