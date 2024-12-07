import tkinter as tk
from tkinter import messagebox
import requests
import json

API_URL = 'https://leakosintapi.com/'
NAZAPI_TOKEN = 'token:token'

def send_request(query, limit=100, lang='en', report_type='json'):
    data = {
        'token': NAZAPI_TOKEN,
        'request': query,
        'limit': limit,
        'lang': lang,
        'type': report_type
    }
    
    try:
        response = requests.post(API_URL, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Erreur de connexion", f"Une erreur est survenue : {e}")
        return None

def on_submit():
    query = entry_query.get()
    if not query:
        messagebox.showwarning("Entrée manquante", "Veuillez entrer une requête avant de soumettre.")
        return

    limit = int(entry_limit.get()) if entry_limit.get().isdigit() else 100
    lang = entry_lang.get() or 'fr'

    results = send_request(query, limit=limit, lang=lang)

    if results:
        text_results.delete(1.0, tk.END)
        text_results.insert(tk.END, json.dumps(results, indent=2))

root = tk.Tk()
root.title("LeakOSint API Interface")
root.geometry("600x600")
root.config(bg="#2A2A2A")

frame_input = tk.Frame(root, padx=10, pady=10, bg="#333333")
frame_input.pack(padx=20, pady=20, fill="x")

label_query = tk.Label(frame_input, text="Entrez votre requête :", fg="#FFFFFF", bg="#333333", font=("Helvetica", 12))
label_query.grid(row=0, column=0, sticky="w", pady=5)
entry_query = tk.Entry(frame_input, width=40, font=("Helvetica", 12))
entry_query.grid(row=0, column=1, pady=5)

label_limit = tk.Label(frame_input, text="Limite des résultats :", fg="#FFFFFF", bg="#333333", font=("Helvetica", 12))
label_limit.grid(row=1, column=0, sticky="w", pady=5)
entry_limit = tk.Entry(frame_input, width=40, font=("Helvetica", 12))
entry_limit.grid(row=1, column=1, pady=5)

label_lang = tk.Label(frame_input, text="Langue (code) :", fg="#FFFFFF", bg="#333333", font=("Helvetica", 12))
label_lang.grid(row=2, column=0, sticky="w", pady=5)
entry_lang = tk.Entry(frame_input, width=40, font=("Helvetica", 12))
entry_lang.grid(row=2, column=1, pady=5)

submit_button = tk.Button(root, text="Soumettre", command=on_submit, bg="#4CAF50", fg="white", font=("Helvetica", 14, "bold"), relief="raised", bd=2)
submit_button.pack(pady=20)

text_results = tk.Text(root, width=70, height=15, wrap=tk.WORD, font=("Courier", 10), bg="#222222", fg="#FFFFFF", bd=2)
text_results.pack(padx=20, pady=10)

label_footer = tk.Label(root, text="Créé par Y2K$", fg="#FFFFFF", bg="#2A2A2A", font=("Helvetica", 10))
label_footer.pack(side="bottom", pady=10)

root.mainloop()
