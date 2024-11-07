"""
Program Title: CA Lime Estimator
Program Version: (Embedded)
Author: Hunter Brown
Created for: Earl Brown & Sons
Date Created: (08/01/2024)
Last Modified: (09/04/2024)
Description: Dehydrated Lime Pack Estimations for CA Environments
Dependencies: Python 3.12.5
License: None
"""
#------------------------------------------------------------------------------------------------------------
import tkinter as tk
from tkinter import messagebox
#------------------------------------------------------------------------------------------------------------
lime_calculation_factor_y = {
    'gala': 5.5, 'honeycrisp': 22, 'orga_honeycrisp': 22,
    'red': 6.6, 'orga_red': 6.6, 'orga_golden': 6.6,
    'golden': 6.6, 'grannysmith': 5.5, 'orga_grannysmith': 5.5,
    'fuji': 5.5, 'orga_fuji': 5.5, 'pink_lady': 5.5,
    'orga_pink_lady': 5.5, 'frozen_pink_lady': 10.5,
}
lime_calculation_factor_n = {
    'gala': 15.4, 'honeycrisp': 55, 'orga_honeycrisp': 55,
    'red': 15.4, 'orga_red': 15.4, 'orga_golden': 22,
    'golden': 22, 'grannysmith': 15.4, 'orga_grannysmith': 15.4,
    'fuji': 15.4, 'orga_fuji': 15.4, 'pink_lady': 15.4,
    'orga_pink_lady': 15.4, 'frozen_pink_lady': 33,
}
#------------------------------------------------------------------------------------------------------------
def calculate_lime_pallets(calculation_factor, bin_count, variety):
    if calculation_factor == "y":
        lime_factor = lime_calculation_factor_y.get(variety)
    elif calculation_factor == "n":
        lime_factor = lime_calculation_factor_n.get(variety)
    else:
        return None, None
    if lime_factor is None:
        return None, None
    lime_lbs = lime_factor * bin_count
    lime_packs = round(lime_lbs / 50, 2)
    lime_pallets = round(lime_packs / 7, 2)
    return lime_packs, lime_pallets
#------------------------------------------------------------------------------------------------------------
def calculate():
    try:
        fruit_variety = entry_variety.get()
        bin_count = float(entry_bin_count.get())
        calculation_factor = entry_calc_factor.get().lower()
        lime_packs, lime_pallets = calculate_lime_pallets(calculation_factor, bin_count, fruit_variety)

        if lime_packs is not None and lime_pallets is not None:
            messagebox.showinfo("CA Lime Requirements",
                                f"Pallets Required: {lime_pallets:.2f}\n"
                                f"Total Bags Needed: {lime_packs:.2f}")
        else:
            messagebox.showerror("Alphabetical Error Detected",
                                 "Check [Fruit Variety] or [Lime Scrub] for correct values")
    except ValueError:
        messagebox.showerror("Numerical Error Detected",
                             "Check [CA Bin Count] for correct values")
#------------------------------------------------------------------------------------------------------------
def helpvar():
    messagebox.showinfo(title="Fruit Variety",
                        message="Entries are Case Sensitive\n\n"
                                "gala (orga & conv)\n"
                                "honeycrisp\n"
                                "orga_honeycrisp\n"
                                "red\n"
                                "orga_red\n"
                                "golden\n"
                                "orga_golden\n"
                                "grannysmith\n"
                                "orga_grannysmith\n"
                                "fuji\n"
                                "orga_fuji\n"
                                "pink_lady\n"
                                "orga_pink_lady\n"
                                "frozen_pink_lady")
def helpbin():
    messagebox.showinfo(title="Bin Count",
                        message="Total # of bins stored in CA Room")
def helpscrub():
    messagebox.showinfo(title="Lime Scrubber Method",
                        message="( y or Y ) = Using lime scrubber\n"
                                "( n or N ) = Not using lime scrubber")
def showfact_y():
    messagebox.showinfo(title="Factor (Y): With Lime Scrubber", message=lime_calculation_factor_y)
def showfact_n():
    messagebox.showinfo(title="Factor (N): Without Lime Scrubber", message=lime_calculation_factor_n)
#------------------------------------------------------------------------------------------------------------
window = tk.Tk()
window.title("CA Lime Estimator")
label_version = tk.Label(window, text="Earl Brown & Sons - CA Lime Estimator\n"
                                      "-------------- Version: 1.1.0 --------------")
label_version.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
#----------------------------------------------------------------
entry_variety = tk.Entry(window)
entry_bin_count = tk.Entry(window)
entry_calc_factor = tk.Entry(window)
button_calculate = tk.Button(window, text="\n   CALCULATE   \n", command=calculate)
button_helpvar = tk.Button(window, text="  FRUIT VARIETY --->   ", command=helpvar)
button_helpbin = tk.Button(window, text=" CA BIN COUNT --->  ", command=helpbin)
button_help_scrub = tk.Button(window, text=" CA LIME SCRUB ---> ", command=helpscrub)
button_showfact_y = tk.Button(window, text="   FACTOR ( Y )   ", command=showfact_y)
button_showfact_n = tk.Button(window, text="   FACTOR ( N )   ", command=showfact_n)
#----------------------------------------------------------------

def update_factor_label(*args):
    variety = entry_variety.get()
    calc_factor = entry_calc_factor.get().lower()
    if calc_factor == "y":
        factor = lime_calculation_factor_y.get(variety, "N/A")
    elif calc_factor == "n":
        factor = lime_calculation_factor_n.get(variety, "N/A")
    else:
        factor = "N/A"
    info_variety.config(text=f"Ratio:\n{factor} LBS per Bin")

entry_variety.bind("<KeyRelease>", update_factor_label)
entry_calc_factor.bind("<KeyRelease>", update_factor_label)
info_variety = tk.Label(window, text="Factor: N/A")

#------------------------------------------------------------------------------------------------------------
button_helpvar.grid(row=1, column=0, padx=10, pady=5)
entry_variety.grid(row=1, column=1, padx=10, pady=5)
info_variety.grid(row=1, column=2, padx=10, pady=5)
#----------------------------------------------------------------
button_helpbin.grid(row=2, column=0, padx=10, pady=5)
entry_bin_count.grid(row=2, column=1, padx=10, pady=5)
#----------------------------------------------------------------
button_help_scrub.grid(row=3, column=0, padx=10, pady=5)
entry_calc_factor.grid(row=3, column=1, padx=10, pady=5)
#----------------------------------------------------------------
button_calculate.grid(row=4, column=1, rowspan=2, padx=5, pady=5)
#----------------------------------------------------------------
button_showfact_y.grid(row=4, column=0, padx=10, pady=5)
button_showfact_n.grid(row=5, column=0, padx=10, pady=5)
#----------------------------------------------------------------
window.mainloop()