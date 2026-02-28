# Advanced BMI Calculator (GUI Version)

import tkinter as tk
from tkinter import messagebox
import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

FILE_NAME = "bmi_records.csv"

def calculate_bmi():
    try:
        name = name_entry.get()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Enter positive values only.")
            return

        bmi = round(weight / (height ** 2), 2)

        if bmi < 18.5:
            category = "Underweight"
            color = "blue"
        elif 18.5 <= bmi < 24.9:
            category = "Normal Weight"
            color = "green"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            color = "orange"
        else:
            category = "Obese"
            color = "red"

        result_label.config(
            text=f"BMI: {bmi}\nCategory: {category}",
            fg=color
        )

        save_data(name, weight, height, bmi, category)

    except ValueError:
        messagebox.showerror("Error", "Enter numeric values only.")

def save_data(name, weight, height, bmi, category):
    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Name", "Weight", "Height", "BMI", "Category", "Date"])
        writer.writerow([
            name,
            weight,
            height,
            bmi,
            category,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ])

def show_chart():
    if not os.path.exists(FILE_NAME):
        messagebox.showerror("Error", "No data available!")
        return

    bmis = []

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            bmis.append(float(row["BMI"]))

    if not bmis:
        messagebox.showerror("Error", "No BMI records found!")
        return

    plt.figure()
    plt.plot(bmis, marker='o')
    plt.title("BMI Trend Over Time")
    plt.xlabel("Record Number")
    plt.ylabel("BMI")
    plt.show()

def clear_fields():
    name_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")

# GUI Setup
root = tk.Tk()
root.title("Advanced BMI Calculator")
root.geometry("400x450")

tk.Label(root, text="Advanced BMI Calculator", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Weight (kg)").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Height (m)").pack()
height_entry = tk.Entry(root)
height_entry.pack()

tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)
tk.Button(root, text="Show BMI Trend", command=show_chart).pack()
tk.Button(root, text="Clear", command=clear_fields).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()