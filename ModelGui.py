from tkinter import *
from keras.models import load_model
import numpy as np
from PIL import ImageGrab
window = Tk()
window.title("Распознавание цифр")
l1 = Label()
model = load_model('mnist.h5')
def predict_digit(img):
    # изменение рзмера изобржений на 28x28
    img = img.resize((28,28))
    # конвертируем rgb в grayscale
    img = img.convert('L')
    img = np.array(img)
    # изменение размерности для поддержки модели ввода и нормализации
    img = img.reshape(1,28,28,1)
    img = img/255.0
    # предсказание цифры
    res = model.predict([img])[0]
    return np.argmax(res), max(res)

def MyProject():
    global l1
    widget = cv
    # Установка координат холста
    x = window.winfo_rootx() + widget.winfo_x()
    y = window.winfo_rooty() + widget.winfo_y()
    x1 = x + widget.winfo_width()
    y1 = y + widget.winfo_height()
    n=28
    m=n*n
    # Изображение захватывается с холста и имеет размер (28 X 28) пикселей
    img = ImageGrab.grab().crop((x, y, x1, y1)).resize((n, n))
    digit, acc = predict_digit(img)
    # Вывод результата на экран
    l1 = Label(window, text=str(digit),justify=CENTER, font=('Arial', 30))
    l1.place(x=450, y=200)
    lastx, lasty = None, None
# Очистка поля
def clear_widget():
    global cv, l1
    cv.delete("all")
    l1.destroy()
# Проверка введенного числа
def event_activation(event):
    global lastx, lasty
    cv.bind('<B1-Motion>', draw_lines)
    lastx, lasty = event.x, event.y
# Рисование цифры на поле
def draw_lines(event):
    global lastx, lasty
    x, y = event.x, event.y
    cv.create_line((lastx, lasty, x, y), width=20, fill='white', capstyle=ROUND, smooth=TRUE, splinesteps=12)
    lastx, lasty = x, y


# Кнопка очистки поля
b1 = Button(window, text=" Очистить ", bg="grey", fg="black", font=('Arial', 15), command=clear_widget)
b1.place(x=420, y=120)
# Кнопка для предсказания цифры, нарисованной на холсте
b2 = Button(window, text=" Проверить ", bg="green", fg="black", font=('Arial', 15), command=MyProject)
b2.place(x=420, y=70)

# Экран рисования цифры
cv = Canvas(window, width=350, height=290, bg='black')
cv.place(x=20, y=20)
cv.bind('<Button-1>', event_activation)
window.geometry("600x400")
window.mainloop()
