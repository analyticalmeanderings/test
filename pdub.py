"""Decryption only, reads from e_passwords.txt
Must install libraries from requirements.txt
"""

import re
import getpass
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# decrypt and search
resp = getpass.getpass(prompt="Enter Creds: ")
try:
    key_unpadded = resp.split(" ")[0]
    iv_unpadded = resp.split(" ")[1]
except:
    print("No luck, bro bro.")
else:
    search_request = getpass.getpass(prompt="Which account? ")
    key = pad(key_unpadded.encode(), AES.block_size)
    iv = pad(iv_unpadded.encode(), AES.block_size)
    with open("e_passwords.txt", "rb") as r_obj:
        e_txt = r_obj.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    try:
        plain_txt = unpad(cipher.decrypt(e_txt), AES.block_size).decode()
    except:
        print("No luck, bro bro.")
    else:
        pw_list = plain_txt.splitlines()
        for line in pw_list:
            result = re.findall(search_request, line)
            if len(result) > 0:
                print(line.split(",")[-1])
    print("")
