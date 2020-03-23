;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname image-design-flag) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)
(overlay (circle 20 "solid" "blue")
         (circle 92.5 "outline" "blue")
         (above (rectangle 900 200 "solid" "orange")
                (rectangle 900 200 "solid" "white")
                (rectangle 900 200 "solid" "green"))
          (rectangle 901 601 "outline" "light-grey"))