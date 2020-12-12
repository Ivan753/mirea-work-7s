#lang racket
(require rnrs/base-6)

; # Вариант 3:
; Создать список из максимального и минимального по модлю
; элементов исходного списка, если елементы - целые числа
; Иначе вернуть среднее арифметическое найденных чисел

(define example (list 1 -12 3 4 5 10))

; Основная логиа
(define (generate_list_from_min_max sample)
  (define temp (car sample))                               ; сохраняем первый элемент списка
  (define min
    (let get_min_elem ((sample sample) (temp temp) (n (length sample)))
       (if (= n 0)
         temp
         (if (< (abs (car sample)) (abs temp))
             (get_min_elem (cdr sample) (car sample) (- n 1))
             (get_min_elem (cdr sample) temp (- n 1)))
         )))  ; получаем минимальный элемент с помощью lambda функции
  (define max
    (let get_max_elem ((sample sample) (temp temp) (n (length sample)))
      (if (= n 0)
        temp
        (if (> (abs (car sample)) (abs temp))
          (get_max_elem (cdr sample) (car sample) (- n 1))
          (get_max_elem (cdr sample) temp (- n 1)))
        )))  ; получаем максимальный элемент
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
((lambda (arg)
   (if (number? arg)
      (if (even? arg)
          (expt arg 2)
          (expt arg 3))
      (list? arg))) 763)


; # Вариант 6
; По вещественному числу вернуть список
; (знак числа, значение по модулю, ближайщее целое число)
((lambda (arg)
   (list
   (if (>= arg 0) "+" "-")
   (abs arg)
   (round arg)
   )) -5.5)