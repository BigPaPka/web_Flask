from flask import Flask, render_template, request
import pickle
# Создание экземпляра приложения Flask
app = Flask(__name__)
# Загрузка модели из файла
model1 = pickle.load(open('D:\\ml\\project\\model\\model12.pkl', 'rb'))

# Определение маршрута для основной страницы
@app.route("/")
def index():
    # Отображение главной страницы
    return render_template('index.html')

# Определение маршрута для предсказания цены на дом
@app.route("/predict", methods=['POST'])
def predict():
    # Извлечение данных из формы
    rooms = int(request.form['rooms'])
    area = int(request.form['area'])  # Общая площадь
    kitchen_area = int(request.form['kitchen_area'])  # Площадь кухни

    # Выполнение предсказания с использованием модели
    prediction = model1.predict([[rooms, area, kitchen_area]])

    # Округление предсказания до двух знаков после запятой
    output = round(prediction[0], 2)

    # Возврат предсказания на страницу
    return render_template('index.html', prediction_text=f' Predicted price: {output}')


# Запуск приложения
if __name__ == "__main__":
    app.run(debug=True)  # Включаем режим отладки для разработки