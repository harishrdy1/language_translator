from tkinter import *
from googletrans import Translator, LANGUAGES

# Initialize translator
translator = Translator()

# Function to translate text
def translate_text():
    input_text = input_box.get("1.0", "end-1c")
    src_lang = source_lang.get()
    tgt_lang = target_lang.get()

    try:
        translated = translator.translate(input_text, src=src_lang, dest=tgt_lang)
        output_box.delete("1.0", END)
        output_box.insert(END, translated.text)
    except Exception as e:
        output_box.delete("1.0", END)
        output_box.insert(END, "Error: " + str(e))

# Create main window
root = Tk()
root.title("Language Translator")
root.geometry("500x400")

# Dropdown language codes
language_codes = list(LANGUAGES.keys())
language_names = list(LANGUAGES.values())
lang_dict = dict(zip(language_names, language_codes))

# Source and Target Language Selection
Label(root, text="Source Language:").pack()
source_lang = StringVar(root)
source_lang.set("en")  # default English
OptionMenu(root, source_lang, *language_codes).pack()

Label(root, text="Target Language:").pack()
target_lang = StringVar(root)
target_lang.set("hi")  # default Hindi
OptionMenu(root, target_lang, *language_codes).pack()

# Input Box
Label(root, text="Enter text to translate:").pack()
input_box = Text(root, height=5, width=50)
input_box.pack()

# Translate Button
Button(root, text="Translate", command=translate_text).pack(pady=10)

# Output Box
Label(root, text="Translated Text:").pack()
output_box = Text(root, height=5, width=50)
output_box.pack()

# Run the app
root.mainloop()
