#lang planet neil/sicp
(define (-1+ x) (- x 1))
(define (1+ x) (+ x 1))

(define (+p x y)
  (if (= x 0)
      y
      (+p (-1+ x) (1+ y))))

(+p 3 4)
