import customtkinter as ctk
from AmazonSearch import Search

WEB_LINK = "https://www.alibaba.com/"
win = ctk.CTk()
win.geometry("450x500")
win.config(padx=30, pady=0)
win.title("Scraping Engin")
ctk.set_appearance_mode("system")


def search_command():
    wait.configure(text="please wait...")
    win.update()
    search = Search()
    max_price = max_p.get().title()
    min_price = min_p.get().title()

    item = search_entry.get().title()

    search.search_input(WEB_LINK, item)
    wait.configure(text="Data file created successfully.")







#   UI section


title = ctk.CTkLabel(master=win, text="Product Finder, Alibaba",
                     font=ctk.CTkFont(weight="bold", size=30, family="Berlin Sans FB"))
title.grid(row=0, column=0, pady=20)

search_entry = ctk.CTkEntry(win, placeholder_text="Search product by name...", width=350)
search_entry.grid(row=1, column=0, padx=20, pady=20, columnspan=3)

min_p = ctk.CTkEntry(win, placeholder_text="Minimum Price")
min_p.grid(row=2, column=0, padx=20, pady=20)

max_p = ctk.CTkEntry(win, placeholder_text="Maximum Price")
max_p.grid(row=3, column=0)

search_btn = ctk.CTkButton(master=win, text="Search", command=search_command)
search_btn.grid(row=4, column=0, pady=30)

wait = ctk.CTkLabel(win, text="...")
wait.grid(row=5, column=0, pady=30)

win.mainloop()
