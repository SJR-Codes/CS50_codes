"""
* CS50P Problem Set 1
* File Extensions
* by Samu Reinikainen 22.07.2022
"""


fname = input("Enter file name: ").strip().lower()

if "." in fname:
    ext = fname.split(".")
    
    print(ext[1])
else:
    print("application/octet-stream")
