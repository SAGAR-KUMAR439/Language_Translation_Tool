import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator
import asyncio


# ---------------- LANGUAGE LIST ----------------

languages_dict = {
    "English": "en",
    "Hindi": "hi",
    "Bengali": "bn",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Chinese": "zh-cn",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
    "Tamil": "ta",
    "Telugu": "te",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Punjabi": "pa"
}


# ---------------- MAIN WINDOW ----------------

root = tk.Tk()

root.title("Language Translation Tool")
root.geometry("700x650")
root.resizable(False, False)


# ---------------- HEADING ----------------

heading = tk.Label(
    root,
    text="Language Translation Tool",
    font=("Arial", 20, "bold")
)

heading.pack(pady=15)


# ---------------- SOURCE LANGUAGE ----------------

source_label = tk.Label(
    root,
    text="Source Language",
    font=("Arial", 11, "bold")
)

source_label.pack()

source_box = ttk.Combobox(
    root,
    values=list(languages_dict.keys()),
    state="readonly",
    font=("Arial", 10),
    width=20
)

source_box.pack(pady=5)

source_box.set("English")


# ---------------- INPUT TEXT ----------------

input_label = tk.Label(
    root,
    text="Enter Text",
    font=("Arial", 11, "bold")
)

input_label.pack(pady=(10, 5))

input_text = tk.Text(
    root,
    height=6,
    width=70,
    font=("Arial", 11)
)

input_text.pack()


# ---------------- TARGET LANGUAGE ----------------

target_label = tk.Label(
    root,
    text="Target Language",
    font=("Arial", 11, "bold")
)

target_label.pack(pady=(10, 5))

target_box = ttk.Combobox(
    root,
    values=list(languages_dict.keys()),
    state="readonly",
    font=("Arial", 10),
    width=20
)

target_box.pack(pady=5)

target_box.set("Hindi")


# ---------------- OUTPUT TEXT ----------------

output_label = tk.Label(
    root,
    text="Translated Text",
    font=("Arial", 11, "bold")
)

output_label.pack(pady=(5, 5))

output_text = tk.Text(
    root,
    height=6,
    width=70,
    font=("Arial", 11)
)

output_text.pack()


# ---------------- TRANSLATION FUNCTION ----------------

def translate_text():

    text = input_text.get("1.0", "end-1c")

    source_language = source_box.get()
    target_language = target_box.get()

    if not text.strip():

        messagebox.showerror(
            "Error",
            "Please enter some text."
        )

        return

    source_code = languages_dict[source_language]
    target_code = languages_dict[target_language]

    print("-----------------------------")
    print("Source Language:", source_language)
    print("Target Language:", target_language)
    print("Source Code:", source_code)
    print("Target Code:", target_code)

    try:

        async def do_translation():

            async with Translator(
                service_urls=["translate.googleapis.com"]
            ) as translator:

                result = await translator.translate(
                    text,
                    src=source_code,
                    dest=target_code
                )

                print("Original:", result.origin)
                print("Detected Language:", result.src)
                print("Translated Result:", result.text)

                return result.text

        translated_text = asyncio.run(do_translation())

        output_text.delete("1.0", "end")

        output_text.insert(
            "1.0",
            translated_text
        )

    except Exception as error:

        print("ERROR:", error)

        messagebox.showerror(
            "Translation Error",
            f"Something went wrong:\n\n{error}"
        )


# ---------------- TRANSLATE BUTTON ----------------

translate_button = tk.Button(
    root,
    text="TRANSLATE",
    command=translate_text,
    font=("Arial", 12, "bold"),
    padx=30,
    pady=8
)

translate_button.pack(pady=12)


# ---------------- CLEAR FUNCTION ----------------

def clear_text():

    input_text.delete("1.0", "end")
    output_text.delete("1.0", "end")


# ---------------- CLEAR BUTTON ----------------

clear_button = tk.Button(
    root,
    text="CLEAR",
    command=clear_text,
    font=("Arial", 10, "bold"),
    padx=25,
    pady=5
)

clear_button.pack(pady=10)


# ---------------- START APPLICATION ----------------

root.mainloop()
