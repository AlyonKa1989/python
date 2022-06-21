# Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

import time
import turtle
from time import sleep

class TrafficLight:
    __color = 'color'

    def running(self):
        while True:
            turtle.title("Turtle Drawing")
            color_1 = turtle.Turtle()
            color_1.pencolor("red")
            color_1.fillcolor("red")
            color_1.dot(500)
            sleep(7)
            color_2 = turtle.Turtle()
            color_2.pencolor("yellow")
            color_2.fillcolor("yellow")
            color_2.dot(500)
            sleep(2)
            color_3 = turtle.Turtle()
            color_3.pencolor("green")
            color_3.fillcolor("green")
            color_3.dot(500)
            sleep(2)
            break

color_trafficLight = TrafficLight()
color_trafficLight.running()
