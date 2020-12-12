#lang racket


; # Вариант 21: список из реверсированных концос исходного списка

; вспомогательная функция для конкатенации дву списков
(define (append list1 list2)
  (if (null? list1)
    list2
  (cons (car list1) (append (cdr list1) list2))))

; функция составления списка из всех реверсированных cdr компонентов
(let list_from_reversed_cdr_lists ((data (list 1 2 3 4 5 6)))
  (if (null? data)
      null
      (append
       (let reverse_list ((data data))
         (if (null? data)
           null
           (append (reverse_list (cdr data)) (list (car data)))
           ))
       (list_from_reversed_cdr_lists (cdr data))
       )))


; # Вариант 23: сумма числовых элементов списка с учетом подсписков

; функция подсчета суммы элементов (должны быть числовыми) списка
; с учетом подсписков
(let count ((lst (list 1 (list 2 3) 3)) (sum 0))
  (if(null? lst)
     sum
   (if (list? (car lst))
       (count(cdr lst) (+ sum (count(car lst) 0)))
    (count(cdr lst) (+ sum (car lst))))))



; # Вариант 38: проверка списка на сортировку
; функция, приверяющая, что список отсортирован по неубыванию
; Входные данные: список из числовых элементов
(let is_order_asc ((lst (list 1 2 3 4 5)))
  (if (null? (cdr lst))
      #t
  (if (> (car lst) (car (cdr lst)))
      #f
      (is_order_asc (cdr lst)))))

