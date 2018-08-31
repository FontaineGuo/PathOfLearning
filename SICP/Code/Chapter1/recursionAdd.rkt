#lang planet neil/sicp

(define (1+ x) (+ x 1))
(define (-1+ x) (- x 1))

(define (+r x y)
  (if (= x 0)
      y
      (1+ (+r (-1+ x) y))))

(+r 3 4)

