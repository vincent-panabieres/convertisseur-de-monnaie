import tkinter as tk
from forex_python.converter import CurrencyRates

cr = CurrencyRates()

conversions = []
favorites = []

def add_to_history(conversion):
    conversions.append(conversion)
    history_text.config(state='normal')
    history_text.insert('end', conversion + '\n')
    history_text.config(state='disabled')

def add_to_favorites():
    currency = entry_from.get().upper()
    if currency not in favorites:
        favorites.append(currency)
        favorite_text.config(state='normal')
        favorite_text.insert('end', currency + '\n')
        favorite_text.config(state='disabled')

def convert():
    amount = float(entry_amount.get())
    from_currency = entry_from.get().upper()
    to_currency = entry_to.get().upper()

    output = cr.convert(from_currency, to_currency, amount)
    label_result.config(text=f'{output} {to_currency}')
    add_to_history(f'{amount} {from_currency} -> {output} {to_currency}')

app = tk.Tk()
app.title('Currency Converter')

label_amount = tk.Label(app, text='Amount')
label_amount.grid(row=0, column=0)

entry_amount = tk.Entry(app)
entry_amount.grid(row=0, column=1)

label_from = tk.Label(app, text='From')
label_from.grid(row=1, column=0)

entry_from = tk.Entry(app)
entry_from.grid(row=1, column=1)

label_to = tk.Label(app, text='To')
label_to.grid(row=2, column=0)

entry_to = tk.Entry(app)
entry_to.grid(row=2, column=1)

button_convert = tk.Button(app, text='Convert', command=convert)
button_convert.grid(row=3, column=0, columnspan=2)

label_result = tk.Label(app, text='')
label_result.grid(row=4, column=0, columnspan=2)

button_add_favorite = tk.Button(app, text='Add to favorites', command=add_to_favorites)
button_add_favorite.grid(row=1, column=2)

label_history = tk.Label(app, text='History')
label_history.grid(row=5, column=0, columnspan=2)

history_text = tk.Text(app, height=5, width=20, state='disabled')
history_text.grid(row=6, column=0, columnspan=2)

label_favorites = tk.Label(app, text='Favorites')
label_favorites.grid(row=5, column=2)

favorite_text = tk.Text(app, height=5, width=20, state='disabled')
favorite_text.grid(row=6, column=2)

app.mainloop()