#lang planet neil/sicp
(define (average x y)
    (/ (+ x y) 2))

(define (average-dump f)
    (lambda (x) (average x (f x))))

(define (abs x)
  (cond ((< x 0)(- x))
        ((= x 0) 0)
        ((> x 0) x)))

(define (good-enough? v1 v2)
    (< (abs (- v1 v2)) 0.001))

(define (fixed-point f first-guess)
  (define (iter old new)
    (if (good-enough? old new)
        new
        (iter new (f new))))
  (iter first-guess (f first-guess)))


(define (sqrt x)
    (fixed-point
        (average-dump (lambda (y) (/ x y)))
        1.0))
(sqrt 9)