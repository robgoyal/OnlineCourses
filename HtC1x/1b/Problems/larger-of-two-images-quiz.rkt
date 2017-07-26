;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname larger-of-two-images-quiz) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)

;; Image -> Boolean
;; Produces true if the height and width of the first image is larger than the height and width of the second image
;; NOTE: Image must be stricly greater, ie. Not equal in any parameters

;; Stub
;(define (larger? img1 img2) false)

;; Examples
(check-expect (larger? (rectangle 20 40 "solid" "outline") (rectangle 50 60 "solid" "outline")) false)
(check-expect (larger? (rectangle 60 40 "solid" "outline") (rectangle 50 60 "solid" "outline")) false)
(check-expect (larger? (rectangle 20 80 "solid" "outline") (rectangle 50 60 "solid" "outline")) false)
(check-expect (larger? (rectangle 20 20 "solid" "outline") (rectangle 20 20 "solid" "outline")) false)
(check-expect (larger? (rectangle 80 80 "solid" "outline") (rectangle 50 60 "solid" "outline")) true)

;; Template
;(define (larger? img1 img2)
;  (... false))

;; Code Body

(define (larger? img1 img2)
  (and (> (image-width img1) (image-width img2))
       (> (image-height img1) (image-height img2))))