(define (length-tail lst) 
        (define (length-helper lst length)
            (if (null? lst)
                length
                
            (length-helper (cdr lst) (+ 1 length))
                
            ))
        (length-helper lst 0)
)


(list '+ 'x 2)
(+ x 2)

(list '+ '(+ 1 2) 3)
(+ (+ 1 2) 3)


(define (make-and-expr e1 e2)
    (list 'and e1 e2))

(make-and-expr #f #t)
(and #f #t)

(eval (make-and-expr #f #t))
#f

(define (fact-expr n) 
 (if (= n 0)
 1
 (list '* n (fact-expr (- n 1))))
)

(fact-expr 5)
(* 5 ( * 4 ( * 3 ( * 2 ( * 1 1)))))

(eval (fact-expr 5))
120


(begin (define x 2) (define x (+ x 1)) x)
3

(begin (define x 1) (define y 2 ) (+ x y))
3
This applies globally

(let ((a 1)
    (b (+ 2 3)))
    (+ a b))
Only in the frame/function, cannot be accesed outside




(define (double expr)
(list 'begin expr expr))

(double '(print 2))
(begin (print 2) (print 2))
(eval (double '(print 2)))
2
2

Or

(define (double expr)
(begin eval(expr) eval(expr)))


(define-macro (twice expr)
(list 'begin expr expr))

(twice (print 2))
2
2


Equivalent to (begin (print 2) (print 2)), automatically evals
have to create lists inside macros


(define x (+ x (+ 1 2)))

(define-macro (add-to var expr)
(list 'define var (list '+ var expr)))

(define x 1)
(add-to x (+ 2 3))
6




(for x in '(1 2 3 4) do (* x x))
(1 4 9 16)

(map (lambda (x) (* x x)) '(1 2 3 4))

Applies function to all numbers in list

(define-macro (for var in lst do expr)
(list 'map (list 'lambda (list var) expr )lst))

(for y in '(4 5 6) do (* y 2))


`(x y z)
(x y z)

A way to evaluate one of the values in a list
`(,x y z)
(2 y z)

(define-macro (for var in lst do expr)
`(map (lambda (,var) ,expr) ,lst))

Streams/generators

(define (ints first)
(cons-stream first
            (ints (+ first 1))))

scm> (ints 1)
(1 . #[promise (not forced)])

(define s (cons-stream 1 (cons-stream 2 nil)))

(cdr-stream s)
(2 . #[promise (not forced)])

(cdr-stream (cdr-stream s))
()


Delay
(delay (print 5))
(define x (delay (print 5)))

x
#[promise (not forced)]

Force

(force x)
5

(define (constant-stream i)
(cons-stream i(constant-stream i)))

Continous 1

scm> (define ones (constant-stream 1))
ones
scm> ones
(1 . #[promise (not forced)])
scm> (car ones)
1
scm> (cdr ones)
#[promise (not forced)]
scm> (car (cdr-stream ones))
1

(define (nats start)
   (cons-stream start (nats (+ start 1))) )
   scm> (define s (nats 1))
s
scm> s
(1 . #[promise (not forced)])
scm> (car s)
1
scm> (car (cdr-stream s))
2
scm> (car (cdr-stream (cdr-stream s)))
3


(define (add-stream s1 s2)
(cons-stream (+ (car s1) (car s2))
            (add-stream (cdr-stream s1) (cdr-stream s2))))

(define ones (cons-stream ones))
(define ints (cons-stream 1 (add-stream ones ints)))
1 2 3 4 5

(define (map-stream fn s)
(if (null? s)
nil
(cons-stream (fn (car s))
(map-stream fn (cdr-stream s)))))

(define (stream-to-list s num-elements)
 (if (or (null? s) (= num-elements 0)) nil
 (cons (car s)
        (stream-to-list (cdr-stream s)
                (- num-elements 1))))
)


(define (add k s) (cons-stream (+ k (car s)) (add k (cdr-stream s))))

(define not-three (cons-stream 1  (cons-stream 2 (add 3 not-three)))
)
1 2 4 5 7 8 10 11


(define (e n d) (cons-stream (quotient n d) (e (* 10 (remainder n d)) d)))

remaind is %

(e 1 8)

    0 1 2 5 0 0 0
n : 1 10 20 40 0 
d : 8 8 8 8 8 