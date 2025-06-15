import pyfiglet
from termcolor import colored
import os

# Get user input
text = input("Enter your name or text: ")
font = input("Enter a font (or press Enter for default): ")
color = input("Enter a color (red, green, blue, etc.): ")

# Apply font
try:
    if font.strip():
        ascii_art = pyfiglet.figlet_format(text, font=font)
    else:
        ascii_art = pyfiglet.figlet_format(text)
except pyfiglet.FontNotFound:
    print("Font not found. Using default font.")
    ascii_art = pyfiglet.figlet_format(text)

# Print colored output
if color.strip():
    print(colored(ascii_art, color))
else:
    print(ascii_art)

# Save to file
file_name = f"{text.replace(' ', '_')}_banner.txt"
with open(file_name, "w", encoding="utf-8") as file:
    file.write(ascii_art)

print(f"\n✅ Banner saved as: {file_name}")
print(f"📂 Location: {os.path.abspath(file_name)}")
