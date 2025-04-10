import tkinter as tk


def show_name():
    name = entry.get()
    label.config(text=f"こんにちは,{name}さん！")


root = tk.Tk()
root.title("名前表示アプリ")
root.geometry("300x150")

tk.Label(root, text="名前を入力してください").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="表示", command=show_name).pack()
label = tk.Label(root, text="", fg="pink")
label.pack()

root.mainloop()
