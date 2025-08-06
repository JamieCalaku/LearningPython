import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

# OpenWeatherMap API-Key
api_key = "SECRET_API_KEY"

if len(api_key) == 0:
    print("**************************************************")
    print("PLEASE ENTER YOUR API KEY IN THE MAIN.PY ON LINE 7")
    print("YOU CAN GET IT FROM https://openweathermap.org/")
    print("**************************************************")
    sys.exit()


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton {
                font-family: Calibri;
            }
            QLabel#city_label {
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input {
                font-size: 40px;
                min-height: 60px;
            }
            QPushButton#get_weather_button {
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label {
                font-size: 75px;
            }
            QLabel#emoji_label {
                font-size: 100px;
                font-family: 'Apple Color Emoji', 'Noto Color Emoji', 'Segoe UI Emoji', sans-serif;
            }
            QLabel#description_label {
                font-size: 50px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        city = self.city_input.text()
        if not city:
            self.display_error("Please enter a city name")
            return

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        try:
            response = requests.get(url)
            data = response.json()

            if str(data.get("cod")) == "200":
                self.display_weather(data)
            else:
                message = data.get("message", "Unknown error occurred")
                self.display_error(f"Error: {message.capitalize()}")

        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request error:\n{req_error}")

    def display_error(self, message):
        self.temperature_label.setText(message)
        self.emoji_label.setText("")
        self.description_label.setText("")

    def display_weather(self, data):
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        weather_id = data["weather"][0]["id"]

        emoji = self.get_weather_emoji(weather_id)

        self.temperature_label.setText(f"{temp:.1f}°C")
        self.description_label.setText(description.capitalize())
        self.emoji_label.setText(emoji)

    def get_weather_emoji(self, weather_id):
        if 200 <= weather_id < 300:
            return "⛈️"
        elif 300 <= weather_id < 400:
            return "🌦️"
        elif 500 <= weather_id < 600:
            return "🌧️"
        elif 600 <= weather_id < 700:
            return "❄️"
        elif 700 <= weather_id < 800:
            return "🌫️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id < 900:
            return "☁️"
        else:
            return "❓"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())