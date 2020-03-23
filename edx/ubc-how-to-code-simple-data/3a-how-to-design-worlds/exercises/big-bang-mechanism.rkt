;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname big-bang-mechanism) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(define SPEED 3)

;; Cat is Number
;; interp. x coordinate of cat
;;
(define C1 0)
(define C2 (/ WIDTH 2))
#;
(define (fn-for-cat c)
  (... c))
;; Template rules used:
;; - atomic non-distinct: Number


;; Cat -> Cat
;; Increase cat x position by SPEED
(check-expect (next-cat 0) SPEED)
(check-expect (next-cat 100) (+ 100 SPEED))
#;
(define (next-cat c) 1) ; stub

;; <Template from Cat>
(define (next-cat c)
  (+ c SPEED))


;; Cat -> Image
;; add CAT-IMG to MTS at proper x coordinate and CTR-Y
(check-expect (render-cat 100) (place-image CAT-IMG 100 CTR-Y MTS))
#;
(define (render-cat c) MTS) ; stub

;; <Template from Cat>
(define (render-cat c)
  (place-image CAT-IMG c CTR-Y MTS))

