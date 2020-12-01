## Как работать

Хорошой практикой является работа в виртуальном окружении.
Необходимо установить зависимости

```
> python -m venv .venv
> pip3 install -r requirements.txt
```

### Запуск

```
> python3 main.py
```

### Краткое описание работы

Решается задача аппроксимации функции `x^2` на промежутке
от -5 до 5 с помощью нейронной сети (НС) прямого распространения.

_Требуемая точность_: нет указано.

_Строение НС_: два нейрона во входном слое -- параметр `x` и вес `b`, скрытый
слой -- 5 нейронов, выходной слой -- один нейрон `y`, функция активации
на скрытом слое -- `ReLu`. Число нейронов в скрытом слое определено случайно. 
Функция активации `ReLu` разекомендовала себя как более подходящая
в сравнении с `Sigmoid`.

_Метод обучение_: генетические алгоритмы (библиотека `pygad``)

**Результат**: точность аппроксимации программно не
измерена, однако зрительно соответствует примерно 80%.
