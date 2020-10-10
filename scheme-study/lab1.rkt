#lang racket
(require rnrs/base-6)

; # Вариант 3:
; Создать список из максимального и минимального по модлю
; элементов исходного списка, если елементы - целые числа
; Иначе вернуть среднее арифметическое найденных чисел

(define example (list 1 -12 3 4 5 10))

; Получить максимальный по модулю элемент
; Через рекурсию перебираются n элементов, во втором аргументе (temp1) хранится наибольшее значение
(define (get_max_elem sample temp n)
  (if (= n 0)
      temp
  (if (> (abs (car sample)) (abs temp))
   (get_max_elem (cdr sample) (car sample) (- n 1))
   (get_max_elem (cdr sample) temp (- n 1)))
  ))

; Получить минимальный по  модулю элемент наподобие
; фнукции получения максимального элемента
(define (get_min_elem sample temp n)
  (if (= n 0)
      temp
  (if (< (abs (car sample)) (abs temp))
   (get_min_elem (cdr sample) (car sample) (- n 1))
   (get_min_elem (cdr sample) temp (- n 1)))
  ))

; Основная логиа
(define (generate_list_from_min_max sample)
  (define temp (car sample))                               ; сохраняем первый элемент списка
  (define min (get_min_elem sample temp (length sample)))  ; получаем минимальный элемент
  (define max (get_max_elem sample temp (length sample)))  ; получаем максимальный элемент
  (if (and (integer? min) (integer? max))
      (list min max)
      (/ (+ min max) 2))
  )

; Пример вызова
; (generate_list_from_min_max (list 1.6 2 12.5))
; (generate_list_from_min_max example)


; # Вариант 18
; Вернуть квадрат четного аргумента, куб нечетного
; Иначе результат проверки на принадлежность к списочному типу
(define (some_func arg)
  (if (number? arg)
      (if (even? arg)
          (expt arg 2)
          (expt arg 3))
      (list? arg)))

; Пример вызова
; (some_func 3)

; # Вариант 6
; По вещественному числу вернуть список
; (знак числа, значение по модулю, ближайщее целое число)
(define (generate_list_for_6 arg)
  (list
   (if (>= arg 0) "+" "-")
   (abs arg)
   (round arg)
   ))

; Пример вызова
; (generate_list_for_6 -5.5)