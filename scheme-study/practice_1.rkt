#lang racket
(require rnrs/base-6)

; # Наработки на практическом занятии

; Возведение в квадрат
(define (square2 x)
  (* x x))


; Функция вывода имени
(define (привет пользователь)
  (display "Привет, ")
  (display пользователь)
  (display "!")
  (newline))


; Процедура ввода имени
(define (пользователь)
  (write "Представьтесь: ")
  (newline)
  (read))

;(привет (пользователь))

; пробуем писать условия
(define (func1 x)
  (if (> x 0)
  x
  (square2 x)))

;(func1 -5)

; # Выполнение заданий (раскомментировать нужную процедуру - вычислитьОбъемКуба, вычислитьОбъемЦилиндра, вычислитьСтоимостьПоездки)

; 1. Вычисление объема куба
(define (объемКуба x)
  (* x (* x x)))
(define (сторонаКуба)
  (write "Введите длину ребра (см) и нажмите клавишу <Enter> = ")
  (read))

(define (вычислитьОбъемКуба)
  (write "Вычисление объема куба")
  (newline)
  (объемКуба (сторонаКуба)))

;(вычислитьОбъемКуба)

; 2. Вычисление объема цилиндра
(define (объемЦилиндра r h)
  (* h (* pi (* r r))))
(define (радиусОснования)
  (write "радиус основания (см) = ")
  (read))
(define (высотаЦилиндра)
  (write "высота цилиндра (см) = ")
  (read))
(define (вычислитьОбъемЦилиндра)
  (write "Вычисление объема цилиндра")
  (newline)
  (объемЦилиндра (радиусОснования) (высотаЦилиндра)))
;(вычислитьОбъемЦилиндра)

; 6. Вычисление стоимости поездки на автомобиле
; логика вычисление
(define (стоимостьПоездки расстояние бензинЛитрНа100Км ценаБензинаЛитр)
  (* ценаБензинаЛитр (+ (* (div расстояние 100) бензинЛитрНа100Км) (* (mod расстояние 100) (/ бензинЛитрНа100Км 100)))))
; получение данных
(define (расстояниеКм)
  (write "расстояние (км) = ")
  (read))

(define (бензинЛитрНа100Км)
  (write "расход бензина на 100 км (литр) = ")
  (read))

(define (бензинЦенаЛитр)
  (write "цена бензина за 1 литр (руб) = ")
  (read))

; базовая процедура
(define (вычислитьСтоимостьПоездки)
  (write "Вычисление стоимости поездки")
  (newline)
  (стоимостьПоездки (расстояниеКм) (бензинЛитрНа100Км) (бензинЦенаЛитр))
  )
(вычислитьСтоимостьПоездки)
