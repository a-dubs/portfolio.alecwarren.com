from base64 import b64decode, b64encode 
from pyperclip import copy

print("This program will obfuscate (encode with base64) your token.")

token = input("Paste your token: ")
obfuscated_token = b64encode(token.encode("utf-8"))

print("Original token:", token)
print("Obfuscated token:", obfuscated_token)

if input("Would you like the obfuscated token copied to your clipboard? (yes/y) : ").lower().strip() in ("y", "yes"):
    copy(obfuscated_token.decode("utf-8"))
    print("Copied obfuscated token to the clipboard! :)")

# if input("Would you like to have this program automatically fill the new obfuscated token into github_token.py (line ? (yes/y) : ").lower().strip() in ("y", "yes"):
#     copy(obfuscated_token)
#     print("Filled obfuscated token into github_token.py! :)")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

