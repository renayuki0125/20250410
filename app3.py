import tkinter as tk
from tkinter import messagebox
import requests


def search_address():
    zipcode = zipcode_entry.get()
    # print(zipcode)
    if not zipcode:
        messagebox.showwarning("入力エラー", "郵便番号を入力してください")
        return

    url = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"
    response = requests.get(url)
    print(response)


def main():
    global zipcode_entry
    root = tk.Tk()
    root.title("郵便番号で住所検索")

    tk.Label(root, text="郵便番号:").grid(row=0, column=0, padx=5, pady=10)
    zipcode_entry = tk.Entry(root, width=20)
    zipcode_entry.grid(row=0, column=1, padx=5, pady=5)

    search_button = tk.Button(root, text="検索する", command=search_address)
    search_button.grid(row=0, column=2, padx=5, pady=5)

    tk.Label(root, text="住所: ").grid(row=1, column=0, padx=5, pady=10)

    address_entry = tk.Entry(root, width=50)
    address_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

    root.mainloop()






if __name__ == "__main__":
    main()
