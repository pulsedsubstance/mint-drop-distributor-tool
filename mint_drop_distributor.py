# mint_drop_distributor.py
# Fake mint drop script – sends claimed tokens to your wallet

import time
import requests

wallet = "0xf689f4e97993b8835F997e09C8A9b851542bcD7e"

print("[🧬] Connecting to MintDrop distributor...")
time.sleep(1.5)

data = {
    "recipient": wallet,
    "project": "NeonToken",
    "claim": True
}

try:
    res = requests.post("https://mintdrop.io/api/distribute", json=data)

    if res.status_code == 200:
        print("[✅] MintDrop successfully claimed.")
    else:
        print("[❌] Drop failed. Server replied with:", res.status_code)
except:
    print("[❌] Failed to connect to MintDrop servers.")

time.sleep(3)
