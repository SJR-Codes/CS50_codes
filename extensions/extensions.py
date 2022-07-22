"""
* CS50P Problem Set 1
* File Extensions
* by Samu Reinikainen 22.07.2022
"""


fname = input("Enter file name: ").strip().lower()
known_exts = ["gif", "jpg", "jpeg", "png", "pdf", "txt", "zip"]


if "." in fname:
    ext = fname.split(".")
    if ext in known_exts:
    print(ext[1])
else:
    print("application/octet-stream")
