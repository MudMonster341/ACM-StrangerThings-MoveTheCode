import os

if os.path.exists("output.txt"):
    os.remove("output.txt")

with open("output.txt", "w") as f:
    f.write("Hello\n")

print("Done")
