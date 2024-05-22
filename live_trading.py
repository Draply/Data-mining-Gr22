import tkinter as tk
from tkinter import messagebox
from libs.exchange import *
from process import *
from binance.spot import Spot as Client


class Trade:
    def __init__(self, public_key, private_key):
        self.client = check_login(public_key, private_key)

    def open_trading_window(self):
        # Hàm mở cửa sổ trading
        trading_window = tk.Toplevel(root)
        trading_window.title("Trading BOT")
        trading_window.geometry("800x600")
        label = tk.Label(trading_window, text="Welcome to BOT ")
        client = self.client
        label.pack()

        symbol_label = tk.Label(trading_window, text="Symbol")
        symbol_entry = tk.Entry(trading_window)
        symbol = symbol_entry.get()
        trade_button = tk.Button(trading_window, text="Trade", command=lambda: self.trading(symbol_entry.get()))
        trade_button.pack()
        symbol_label.pack()
        symbol_entry.pack()
        self.trading_info = tk.Text(trading_window)
        self.trading_info.pack()
    def trading(self,symbols):

        print(symbols)
        while True:

            if (datetime.now().hour % 4 == 0) or first:
                # refresh data
                # self.trading_info.insert(tk.END, "Balance:" + str(balanceOf(self.client, "USDT")))
                df = gather_data(symbols)
                states = get_states(df)
                self.trading_info.insert(tk.END, 'Current state of the market:\n')
                self.trading_info.insert(tk.END, str(states) + '\n\n')

                if states == 'uptrend' and buyed == True:
                    takeBuyOrder(self.client, symbols, 10)
                    self.trading_info.insert(tk.END, "Buyed at price :" + str(df['close'].iloc[-1]) + '\n')
                    buyed = False
                if states == 'dowtrend' and buyed == False:
                    takeSellOrder(self.client, symbols, 10)
                    self.trading_info.insert(tk.END, "Selled at price :" + str(df['close'].iloc[-1]) + '\n\n')
                    buyed = True
                first = False



def login():
    # Hàm xử lý sự kiện đăng nhập
    public_key = public_key_entry.get()
    private_key = private_key_entry.get()



    Trade.open_trading_window(Trade(public_key, private_key))


# Tạo cửa sổ đăng nhập
root = tk.Tk()
root.title("Login Window")

public_key_label = tk.Label(root, text="Public Key")
private_key_label = tk.Label(root, text="Private Key")

# Create entry fields
public_key_entry = tk.Entry(root)
private_key_entry = tk.Entry(root)

# Create login button
login_button = tk.Button(root, text="Login", command=login)

# Grid layout
public_key_label.grid(row=0, column=0)
public_key_entry.grid(row=0, column=1)
private_key_label.grid(row=1, column=0)
private_key_entry.grid(row=1, column=1)
login_button.grid(row=2, column=1)

root.mainloop()
