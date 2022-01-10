scm> (/ 10 2)
5
scm> (/ 10 3)
3.3333333333333335 --> computer error float doesnt fit
scm> (quotient 10 3)
3
scm> (/ (+ 5 3) 2)
4

scm> (+)
0
scm> ()
()
scm> (*)
1
scm> (-)
Traceback Error

scm> (define x 5)
x
scm> (define y 6)
y
scm> (+ x y)
11
scm> x
5
scm> y
6
scm> (define x (+ x 1))
x

scm> (+ (* 3 (+ (* 2 4) (+ 3 5))) (+ (- 10 7) 6))
57
scm> (number? 5)
#t
scm> (zero? 9)
#f
scm> <zero? 0)
Traceback (most recent call last):
 0	<zero?
Error: unknown identifier: <zero?
0
ParseError: unexpected token: )
scm> (zero? 0)
#t
scm> (zero? (- 2 2))
#t
scm> (integer? 2)
#t
scm> (integer? 2.2)
#f
scm> (odd? 5)
#t
scm> (eq? 0 #f)
#f

scm> x
5
scm> (if (> 1 0) (- 3 4) (/ 1 0))
-1

if (condition) (condition true result) (condiiton false resutl)

scm> (define pi 3.14)
pi
scm> (define r 5)
r
scm> (* pi (* r r))
78.5
scm> (define (square x) (* x x))
square
scm> (square 5)
25

scm> (square (+ (square 3) (square 4)))
625
scm> (define (square x) (* x x))
square
scm> (square 2)
4
scm> square
(lambda (x) (* x x))
scm>

scm> (lambda (x) (* x x))
(lambda (x) (* x x))

scm> ((lambda (x) (+ x 4)) 5)
9

scm> (if #t 3 5)
3
scm> (if #f 3 5)
5
scm> (if 0 (+ 1 0) (/ 1 0))
1
scm> (if (> 10 1) (* 5 6))
30
scm> (if (not 4) 1 (if #f 5 6))
6
scm> (define x 5)
x
scm> (if x (* x x) (* x 2))
25
scm> (define (fact n) (if (<= n 1) 1 (* n (fact ( - n 1)))))
fact
scm> (fact 5)
120

(define (count-up n) (define (counter k) (print k) (if (< k n) (counter (+ k 1)  ) )   )  (counter 1) )

(define (count-down n) (print n) (if (> n 1) (count-down (- n 1)  ) )  )

(define (hailstone n) (print n) (if (= n 1) 1 (if (even? n) (hailstone (/ n 2)) (hailstone (+ (* 3 n) 1)) )  )  )


(eq? e1 e2) checks identical values
(equal? e1 e2) quivalent values (false if not same list)
(null? expr)
(= e1 e2) only numbers

car cdr


(list 1 2 3) --> Introcduces nesting
(list 0 (lust 1 2 3))


Quoting 
'(a b c)
(a b c)

scm> (define x '(1 2 3))
x
scm> x
(1 2 3)
scm> (car x)
1
scm> (cdr x)
(2 3)
scm> (equal? x (list 1 2 3))
#t
scm> (define a '(1 2 3))
a
scm> (define b '(1 2 3))
b
scm> (list a b)
((1 2 3) (1 2 3))
scm> (car '(a b))
a
scm> (eval (car '(a b)))
(1 2 3)
scm> (equal? '() nil)
#t

(define (add-to-end lst x)
    (if (null? lst) (list x) (if (null? (cdr lst))
                                 (cons (car lst) (cons x nil))
                                 (cons (car lst) (add-to-end (cdr lst) x))
    ))
scm> (add-to-end '(1 2 3 4) '(5 6))
(1 2 3 4 (5 6))


(define (fact n)
    (define (fact-tail n result)
        (if (<= n 1)
            result
        (fact-tail (- n 1) (* n result)))
    )
(fact-tail n 1)
)
(tail recursive)


LAB 10
(define (over-or-under x y)
 'YOUR-CODE-HERE

 (cond 
    ((< x y) -1)
    ((= x y) 0)
    ((> x y) 1)
 )

)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0




(define (filter f lst)
  'YOUR-CODE-HERE
 (if (null? lst)
     lst
     (if (f (car lst))
          (cons (car lst) (filter f (cdr lst)))
          (filter f (cdr lst))))
)

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)




(define (make-adder num)

 'YOUR-CODE-HERE
 (define (adder x) (+ num x))
  adder
)
;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13


(define lst

 'YOUR-CODE-HERE
    (cons (cons 1 nil) (cons 2 (cons (cons 3 (cons 4 nil)) (cons 5 nil))))

)





(define (composed f g)

 'YOUR-CODE-HERE
 (define (h x)
  (f (g x)))
 h
)





(define (remove item lst)

 'YOUR-CODE-HERE
  (if (null? lst)
      lst
  (filter-lst (lambda (x) (not (= item x))) lst)
)
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)









(define (no-repeats s)
 'YOUR-CODE-HERE
 (if (null? s)
     s
     (cons (car s)
        (no-repeats (filter-lst (lambda (x) (not (= x (car s)) ) ) (cdr s)) 
        ))
)
)

;;; Tests
(no-repeats (list 5 4 5 4 2 2))
; expect (5 4 2)

((define (substitute s old new)

 'YOUR-CODE-HERE
(if (null? s)
    s
(if (equal? (car s) old) 
    (cons new (substitute (cdr s) old new ))
    (cons (car s) (substitute (cdr s) old new))
    )
))



(define (sub-all s olds news)

 'YOUR-CODE-HERE
 (if (null? olds)
     s
     (sub-all (substitute s (car olds) (car news) ) (cdr olds) (cdr news)))
)