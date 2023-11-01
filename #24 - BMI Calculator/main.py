import tkinter

# Window
window = tkinter.Tk()
window.title("BMI Calculator")
window.geometry("250x250")


# Calculate BMI
def calculate_bmi():
    weight = weight_input.get()
    height = height_input.get()

    if weight == "" or height == "":
        result_label.config(text="Please enter your weight and height.")
    else:
        try:
            bmi = round(float(weight) / ((float(height) / 100) ** 2), 2)
            result_string = write_result(bmi)
            result_label.config(text=result_string)
            clear()
        except ValueError:
            result_label.config(text="Please enter valid values.")


# Function to clear the input fields
def clear():
    weight_input.delete(0, 'end')
    height_input.delete(0, 'end')


# Write Results
def write_result(bmi):
    result_string = f"Your BMI is: {bmi}. You are "
    if bmi <= 16:
        result_string += "severely thin."
    elif 16 < bmi <= 17:
        result_string += "moderately thin."
    elif 17 < bmi <= 18.5:
        result_string += "mildly thin."
    elif 18.5 < bmi <= 25:
        result_string += "normal."
    elif 25 < bmi <= 30:
        result_string += "overweight."
    elif 30 < bmi <= 35:
        result_string += "obese."
    elif 35 < bmi <= 40:
        result_string += "severely obese."
    else:
        result_string += "very severely obese."
    return result_string


# UI
weight_input_label = tkinter.Label(text="Enter your weight (kg):", font=("Arial", 15), pady=15)
weight_input_label.pack()

weight_input = tkinter.Entry(width=10, font=("Arial", 15))
weight_input.pack()

height_input_label = tkinter.Label(text="Enter your height (cm):", font=("Arial", 15), pady=15)
height_input_label.pack()

height_input = tkinter.Entry(width=10, font=("Arial", 15))
height_input.pack()

calculate_button = tkinter.Button(text="Calculate", font=("Arial", 12, "bold"), pady=10, command=calculate_bmi)
calculate_button.pack()

result_label = tkinter.Label(font=("Arial", 12), pady=20)
result_label.pack()

window.mainloop()
