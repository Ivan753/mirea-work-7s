#lang racket


; # Вариант 1: сортировка пузырьком (по убыванию)

; Аналог внутреннего цикла
; Проверяем соседние элементы, меняем местами при необходимости,
; формируем новый список из элементов, неотсортированные таким же
; образом проверяем с помощью рекурсии на последующих элементах 
(define (bubble-sort lst)
  (if (> (length lst) 1)
  (if (> (car lst) (cadr lst))
      (cons (car lst) (bubble-sort (cons (cadr lst) (cddr lst))))
      (cons (cadr lst) (bubble-sort (cons (car lst) (cddr lst))))
      )
  lst
  ))

(define (bubble lst)
  (if (> (length lst) 1)
      (bubble-sort (cons (car lst) (bubble (cdr lst))))
      lst
      ))

; Пример запуска
; (bubble (list 1 -2 3 10 5))



; # Вариант 2: быстрая сортировка

; Используется встроенная функция filter
; для раделения списка по pivot
(define (quick-sort lst)
  (cond
    [(< (length lst) 2) lst]
    [else (let ([pivot (car lst)] [rest (cdr lst)])
        (append
           (quick-sort (filter (lambda (x) (< x pivot)) rest))
           (list pivot)
           (quick-sort (filter (lambda (x) (>= x pivot)) rest))
        )
   )]))

; Пример запуска
; (quick-sort (list 1 -2 3 10 5))



; # Вариант 9: синтаксический анализатор
; Входной язык содержит знак #, ключевое слово define, идентификатор, число

(require parser-tools/lex)
(require (prefix-in : parser-tools/lex-sre))

(define custom-lexer
  (lexer
   ; define
   [(:: "define")
    (cons `(DEFINE ,(string->symbol lexeme))
          (custom-lexer input-port))]

   ; идентификатор
   [(:+ (:or (char-range #\a #\z) (char-range #\A #\Z)))
    (cons `(ID ,(string->symbol lexeme))
          (custom-lexer input-port))]
   ; знак #
   [(:: "#")
    (cons `(SHARP ,(string->symbol lexeme))
          (custom-lexer input-port))]
   ; число (может быть отрицательным)
   [(:: (:? #\-) (:+ numeric))
    (cons `(INT ,(string->number lexeme))
          (custom-lexer input-port))]

   [whitespace
    (custom-lexer input-port)]

   [(eof)
    '()]))

(define (my-lang-lexer value)
    (let ([input (open-input-string value)]) (custom-lexer input))
)

; Пример вызова
; (my-lang-lexer "define x #11")
