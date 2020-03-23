;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname space-invaders) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/universe)
(require 2htdp/image)

;; Space Invaders


;; Constants:
;; =======================================================================
(define WIDTH  300)
(define HEIGHT 500)

(define INVADER-X-SPEED 1.5)  ;speeds (not velocities) in pixels per tick
(define INVADER-Y-SPEED 1.5)
(define TANK-SPEED 5)
(define MISSILE-SPEED 10)

(define HIT-RANGE 10)

(define INVADE-RATE 50)

(define BACKGROUND (empty-scene WIDTH HEIGHT))

(define INVADER
  (overlay/xy (ellipse 10 15 "outline" "blue")              ;cockpit cover
              -5 6
              (ellipse 20 10 "solid"   "blue")))            ;saucer

(define TANK
  (overlay/xy (overlay (ellipse 28 8 "solid" "black")       ;tread center
                       (ellipse 30 10 "solid" "green"))     ;tread outline
              5 -14
              (above (rectangle 5 10 "solid" "black")       ;gun
                     (rectangle 20 10 "solid" "black"))))   ;main body

(define TANK-HEIGHT/2 (/ (image-height TANK) 2))

(define MISSILE (ellipse 5 15 "solid" "red"))


;; Data Definitions:
;; =======================================================================

(define-struct game (invaders missiles tank))
;; Game is (make-game  (listof Invader) (listof Missile) Tank)
;; interp. the current state of a space invaders game
;;         with the current invaders, missiles and tank position

;; Game constants defined below Missile data definition

#;
(define (fn-for-game g)
  (... (fn-for-loi (game-invaders g))
       (fn-for-lom (game-missiles g))
       (fn-for-tank (game-tank g))))



(define-struct tank (x dir))
;; Tank is (make-tank Number Direction)
;; interp. the tank location is x, HEIGHT - TANK-HEIGHT/2 in screen coordinates
;;         the tank moves TANK-SPEED pixels per clock tick left if dir -1, right if dir 1

(define T0 (make-tank (/ WIDTH 2) 1))   ;center going right
(define T1 (make-tank 50 1))            ;going right
(define T2 (make-tank 50 -1))           ;going left

#;
(define (fn-for-tank t)
  (... (tank-x t) (tank-dir t)))


;; Direction is one of:
;; - -1
;; -  1
;; interp. the direction of the tank

;; <Examples are redundant for enumeration>

#;
(define (fn-for-direction d)
  (cond [(= d 1) (...)]
        [(= d -1) (...)]))


(define-struct invader (x y dx))
;; Invader is (make-invader Number Number Direction)
;; interp. the invader is at (x, y) in screen coordinates
;;         the invader along x by dx pixels per clock tick
;;         the invader will move left or right in Direction

(define I1 (make-invader 150 100 1))           ;not landed, moving right
(define I2 (make-invader 150 HEIGHT -1))       ;exactly landed, moving left
(define I3 (make-invader 150 (+ HEIGHT 10) 1)) ;> landed, moving right

#;
(define (fn-for-invader i)
  (... (invader-x i) (invader-y i) (invader-dx i)))


;; ListOfInvader is one of:
;; - empty
;; - (cons Invader ListOfInvader)
;; interp. A list of Invaders

(define LOI0 empty)
(define LOI1 (cons I1 empty))
(define LOI2 (cons I2 (cons I1 empty)))
(define LOI3 (cons I3 (cons I2 (cons I1 empty))))

#;
(define (fn-for-loi loi)
  (cond [(empty? loi) (...)]
        [else
         (... (fn-for-invader (first loi))
              (fn-for-loi (rest loi)))]))


(define-struct missile (x y))
;; Missile is (make-missile Number Number)
;; interp. the missile's location is x y in screen coordinates

(define M1 (make-missile 150 300))                       ;not hit I1
(define M2 (make-missile (invader-x I1) (+ (invader-y I1) 10)))  ;exactly hit I1
(define M3 (make-missile (invader-x I1) (+ (invader-y I1)  5)))  ;> hit I1

#;
(define (fn-for-missile m)
  (... (missile-x m) (missile-y m)))


;; ListOfMissile is one of:
;; - empty
;; - (cons Missile ListOfMissile)
;; interp. A list of Missiles

(define LOM0 empty)
(define LOM1 (cons M1 empty))
(define LOM2 (cons M2 (cons M1 empty)))
(define LOM3 (cons M3 (cons M2 (cons M1 empty))))

#;
(define (fn-for-lom lom)
  (cond [(empty? lom) (...)]
        [else
         (... (fn-for-missile (first lom))
              (fn-for-lom (rest lom)))]))


(define G0 (make-game empty empty T0))
(define G1 (make-game empty empty T1))
(define G2 (make-game (list I1) (list M1) T1))
(define G3 (make-game (list I1 I2) (list M1 M2) T1))
(define G4 (make-game LOI3 LOM3 T1))


;; Functions:
;; =======================================================================

;; =========BIG BANG FUNCTIONS==========
;; Game -> Game
;; Start the world with (main (make-game empty empty (make-tank (/ WIDTH 2) 1)))
;; <Examples not necessary for main>

(define (main g)
  (big-bang g                            ; Game
            (on-tick update-game)        ; Game -> Game
            (to-draw render-game)        ; Game -> Image
            (stop-when game-over?)       ; Game -> Boolean
            (on-key handle-key-event)))  ; Game KeyEvent -> Game


;; =========ON TICK FUNCTIONS==========
;; Game -> Game
;; Produce the next state of the game
(check-random (update-game G1) (make-game
                                 (update-invaders (game-invaders G1) (game-missiles G1))
                                 (update-missiles (game-missiles G1) (game-invaders G1))
                                 (update-tank (game-tank G1))))

; (define (update-game g) G0) ; stub
; <Template taken from Game>
(define (update-game g)
  (make-game (update-invaders (game-invaders g) (game-missiles g))
             (update-missiles (game-missiles g) (game-invaders g))
             (update-tank (game-tank g))))


;; ListOfInvader ListOfMissile -> ListOfInvader
;; Advance the state of the consumed loi with the consumed lom
(check-random (update-invaders (cons (make-invader 100 100 -1) empty) empty)
              (cons (make-invader (+ 100 (* -1 INVADER-X-SPEED)) (+ 100 INVADER-Y-SPEED) -1) empty)) ;; no invader hit
(check-random (update-invaders LOI1 LOM2) empty) ;; only invader hit

; (define (update-invaders loi lom) loi) ; stub
; <Template taken from ListOfInvader w/ extra parameter>

(define (update-invaders loi lom)
  (add-random-invader (move-invaders (remove-hit-invaders loi lom))))


;; ListOfInvader ListOfMissile -> ListOfInvader
;; Remove invaders which have been hit by missiles
(check-expect (remove-hit-invaders LOI1 LOM2) empty)
(check-expect (remove-hit-invaders (cons (make-invader 100 100 1) (cons (make-invader 175 233 -1) empty)) (cons (make-missile 105 100) empty))
              (cons (make-invader 175 233 -1) empty))
(check-expect (remove-hit-invaders (cons (make-invader 200 75 -1) (cons (make-invader 122 100 -1) empty)) (cons (make-missile 100 300) empty))
              (cons (make-invader 200 75 -1) (cons (make-invader 122 100 -1) empty)))
(check-expect (remove-hit-invaders (cons (make-invader 200 75 -1) (cons (make-invader 122 100 -1) empty)) (cons (make-missile 200 75) (cons (make-missile 120 100) empty)))
              empty)

; (define (remove-hit-invaders loi lom) loi) ; stub
; <Template taken from ListOfInvader w/ extra parameter>

(define (remove-hit-invaders loi lom)
  (cond [(empty? loi) empty]
        [(empty? lom) loi]
        [else
         (if (lom-hit-invader? (first loi) lom)
             (remove-hit-invaders (rest loi) lom)
             (cons (first loi) (remove-hit-invaders (rest loi) lom)))]))


;; Invader ListOfMissile -> Boolean
;; Produce true if invader has been hit by missile in consumed lom
(check-expect (lom-hit-invader? (make-invader 100 150 -1) (cons (make-missile 105 152) (cons (make-missile 200 12) empty))) true)
(check-expect (lom-hit-invader? (make-invader 150 30 1) (cons (make-missile 105 152) (cons (make-missile 200 12) empty))) false)

; (define (lom-hit-invader? i lom) false) ; stub
; <Template taken from ListOfMissile w/ extra paraemter>

(define (lom-hit-invader? i lom)
  (cond [(empty? lom) false]
        [else
         (if (missile-hit-invader? (first lom) i)
             true
             (lom-hit-invader? i (rest lom)))]))


;; ListOfInvader -> ListOfInvader
;; Move the invaders for consumed loi
(check-expect (move-invaders LOI1) (cons (make-invader (+ (invader-x I1) (* INVADER-X-SPEED (invader-dx I1)))    ;; invader middle of screen moving right
                                                       (+ (invader-y I1) INVADER-Y-SPEED) (invader-dx I1)) empty)) 
(check-expect (move-invaders (cons (make-invader 100 125 -1) empty))                                             ;; invader middle of screen moving left
              (cons (make-invader (+ 100 (* INVADER-X-SPEED -1)) (+ 125 INVADER-Y-SPEED) -1) empty))
(check-expect (move-invaders (cons (make-invader 10 125 1) empty))                                              ;; invader at left edge exactly
              (cons (make-invader (+ 10 (* INVADER-X-SPEED 1)) (+ 125 INVADER-Y-SPEED) 1) empty))
(check-expect (move-invaders (cons (make-invader 11 125 -1) empty))                                             ;; invader didn't exactly reach left edge
              (cons (make-invader 10  (+ 125 INVADER-Y-SPEED) 1) empty))
(check-expect (move-invaders (cons (make-invader 290 200 -1) empty))          ;; invader at right edge exactly
              (cons (make-invader (+ 290 (* INVADER-X-SPEED -1)) (+ 200 INVADER-Y-SPEED) -1) empty))
(check-expect (move-invaders (cons (make-invader 289 200 1) empty))          ;; invader reaches right edge, changes dx
              (cons (make-invader 290 (+ 200 INVADER-Y-SPEED) -1) empty))
              
; (define (move-invaders loi) loi) ; stub
; <Template taken from ListOfInvader>

(define (move-invaders loi)
  (cond [(empty? loi) empty]
        [else
         (cons (move-invader (first loi))
               (move-invaders (rest loi)))]))


;; Invader -> Invader
;; Move invader by INVADER-X-SPEED in direction of dx and INVADER-Y-SPEED down
(check-expect (move-invader I1) (make-invader (+ (invader-x I1) (* INVADER-X-SPEED (invader-dx I1)))  ; normal case
                                              (+ (invader-y I1) INVADER-Y-SPEED) (invader-dx I1)))
(check-expect (move-invader (make-invader 11 100 -1))              ;; invader reaches left edge
              (make-invader 10 (+ 100 INVADER-Y-SPEED) 1))
(check-expect (move-invader (make-invader 289 100 1))              ;; invader reaches right edge
              (make-invader 290 (+ 100 INVADER-Y-SPEED) -1))

; (define (move-invader i) i) ; stub
; <Template taken from Invader>

(define (move-invader i)
  (cond [(and (invader-left-edge? i) (= (invader-dx i) -1))
         (make-invader (/ (image-width INVADER) 2) (+ (invader-y i) INVADER-Y-SPEED) 1)]
        [(and (invader-right-edge? i) (= (invader-dx i) 1))
         (make-invader (- WIDTH (/ (image-width INVADER) 2)) (+ (invader-y i) INVADER-Y-SPEED) -1)]
        [else
         (make-invader (+ (invader-x i) (* INVADER-X-SPEED (invader-dx i))) (+ (invader-y i) INVADER-Y-SPEED) (invader-dx i))]))


;; Invader -> Boolean
;; Produce true if invader has reached left edge, false otherwise
(check-expect (invader-left-edge? (make-invader 11 100 -1)) (<= (+ 11 (* INVADER-X-SPEED -1)) (/ (image-width INVADER) 2)))
(check-expect (invader-left-edge? (make-invader 24 200 -1)) (<= (+ 24 (* INVADER-X-SPEED -1)) (/ (image-width INVADER) 2)))

; (define (invader-left-edge? i) false) ; stub
; <Template taken from Invader>

(define (invader-left-edge? i)
  (<= (+ (invader-x i) (* INVADER-X-SPEED (invader-dx i))) (/ (image-width INVADER) 2)))


;; Invader -> Boolean
;; Produce true if invader has reached right edge, false otherwise
(check-expect (invader-right-edge? (make-invader 289 150 1)) (>= (+ 289 (* INVADER-X-SPEED 1)) (- WIDTH (/ (image-width INVADER) 2))))
(check-expect (invader-right-edge? (make-invader 189 225 1)) (>= (+ 189 (* INVADER-X-SPEED 1)) (- WIDTH (/ (image-width INVADER) 2))))

; (define (invader-right-edge? i) false) ; stub
; <Template taken from Invader>

(define (invader-right-edge? i)
  (>= (+ (invader-x i) (* INVADER-X-SPEED (invader-dx i))) (- WIDTH (/ (image-width INVADER) 2))))


;; ListOfInvader -> ListOfInvader
;; Add a random invader to consumed loi if random number generated is less than INVADE-RATE
(check-random (add-random-invader empty) (if (<= (random 1000) INVADE-RATE)
                                       (cons (make-invader (random WIDTH) (/ (image-height INVADER) 2) (if (= (random 2) 0) -1 1)) empty)
                                       empty))

; (define (add-random-invader loi) loi) ; stub
; <Template taken from ListOfInvader>

(define (add-random-invader loi)
  (if (<= (random 1000) INVADE-RATE)
      (cons (make-invader (random WIDTH) (/ (image-height INVADER) 2) (if (= (random 2) 0) -1 1)) loi)
      loi))


;; ListOfMissile ListOfInvader -> ListOfMissile
;; Advance the state of the consumed lom
(check-expect (update-missiles empty LOI1) empty)
(check-expect (update-missiles LOM1 LOI1) (cons (make-missile (missile-x M1) (- (missile-y M1) MISSILE-SPEED)) empty)) ; no hit missile or past screen
(check-expect (update-missiles LOM2 LOI1) (cons (make-missile (missile-x M1) (- (missile-y M1) MISSILE-SPEED)) empty)) ; M2 hit I1, no missiles past screen
(check-expect (update-missiles (cons (make-missile (/ WIDTH 2) 0) LOM2) LOI1) (cons (make-missile (missile-x M1) (- (missile-y M1) MISSILE-SPEED)) empty))

; (define (update-missiles lom loi) lom) ; stub
; <Template taken from ListOfMissile w/ extra parameter>

(define (update-missiles lom loi)
  (remove-offscreen-missiles (move-missiles (remove-hit-missiles lom loi))))


;; ListOfMissile ListOfInvader -> ListOfMissile
;; Remove missiles which have hit invaders
(check-expect (remove-hit-missiles empty LOI2) empty)
(check-expect (remove-hit-missiles (cons (make-missile 50 100) empty) (cons (make-invader 100 200 5) empty)) (cons (make-missile 50 100) empty)) ;; no hit
(check-expect (remove-hit-missiles (cons (make-missile 150 50) empty) (cons (make-invader 150 50 5) empty)) empty) ;; exact hit
(check-expect (remove-hit-missiles (cons (make-missile 150 50) empty) (cons (make-invader 145 45 5) empty)) empty) ;; hit within HIT-RANGE 

; (define (remove-hit-missiles lom loi) lom) ; stub
; <Template taken from ListOfMissiles w/ extra parameter>

(define (remove-hit-missiles lom loi)
  (cond [(empty? lom) empty]
        [(empty? loi) lom]
        [else
         (if (missile-hit-loi? (first lom) loi)
             (remove-hit-missiles (rest lom) loi)
             (cons (first lom) (remove-hit-missiles (rest lom) loi)))]))


;; Missile ListOfInvader -> Boolean
;; Check if missile has hit any invader in consuemd loi
(check-expect (missile-hit-loi? (make-missile 150 50) (cons (make-invader 100 200 5) (cons (make-invader 145 45 5) empty))) true)
(check-expect (missile-hit-loi? (make-missile 150 50) (cons (make-invader 145 45 5) (cons (make-invader 150 50 5) empty))) true)
(check-expect (missile-hit-loi? (make-missile 25 100) (cons (make-invader 100 200 5) empty)) false)

; (define (missile-hit-invader? m loi) false) ; stub
; <Template taken from ListOfInvader w/ extra parameter>

(define (missile-hit-loi? m loi)
  (cond [(empty? loi) false]
        [else
         (if (missile-hit-invader? m (first loi))
             true
             (missile-hit-loi? m (rest loi)))]))


;; Missile Invader -> Boolean
;; Produce true if missile hit invader within HIT RANGE
(check-expect (missile-hit-invader? M2 I1) (and (<= (- (invader-x I1) HIT-RANGE) (missile-x M2) (+ (invader-x I1) HIT-RANGE))
                                (<= (- (invader-y I1) HIT-RANGE) (missile-y M2) (+ (invader-y I1) HIT-RANGE))))
(check-expect (missile-hit-invader? M1 I1) (and (<= (- (invader-x I1) HIT-RANGE) (missile-x M1) (+ (invader-x I1) HIT-RANGE))
                                (<= (- (invader-y I1) HIT-RANGE) (missile-y M1) (+ (invader-y I1) HIT-RANGE))))

; (define (missile-hit-invader? m i) false) ; stub
; <Template taken from Missile w/ extra parameter>

(define (missile-hit-invader? m i)
  (and (<= (- (invader-x i) HIT-RANGE) (missile-x m) (+ (invader-x i) HIT-RANGE))
       (<= (- (invader-y i) HIT-RANGE) (missile-y m) (+ (invader-y i) HIT-RANGE))))


;; ListOfMissile -> ListOfMissile
;; Move missiles in consumed lom
(check-expect (move-missiles empty) empty)
(check-expect (move-missiles LOM1) (cons (make-missile (missile-x M1) (- (missile-y M1) MISSILE-SPEED)) empty))
(check-expect (move-missiles LOM2) (cons (make-missile (missile-x M2) (- (missile-y M2) MISSILE-SPEED))
                                         (cons (make-missile (missile-x M1) (- (missile-y M1) MISSILE-SPEED)) empty)))
(check-expect (move-missiles (cons (make-missile 150 0) empty)) (cons (make-missile 150 (- 0 MISSILE-SPEED)) empty))

; (define (move-missiles lom) lom) ; stub
; <Template taken from ListOfMissile>

(define (move-missiles lom)
  (cond [(empty? lom) empty]
        [else
         (cons (move-missile (first lom))
               (move-missiles (rest lom)))]))


;; Missile -> Missile
;; Move missile up screen by MISSILE-SPEED
(check-expect (move-missile M1) (make-missile (missile-x M1) (- (missile-y M1) MISSILE-SPEED)))

; (define (move-missile m) m) ; stub
; <Template taken from Missile>

(define (move-missile m)
  (make-missile (missile-x m) (- (missile-y m) MISSILE-SPEED)))


;; ListOfMissile -> ListOfMissile
;; Remove missiles which have past the top of the BACKGROUND (- (/ (image-height MISSILE) 2))
(check-expect (remove-offscreen-missiles empty) empty)
(check-expect (remove-offscreen-missiles (cons (make-missile 150 50) empty)) (cons (make-missile 150 50) empty))
(check-expect (remove-offscreen-missiles (cons (make-missile 150 (- (/ (image-height MISSILE) 2))) empty)) empty)
(check-expect (remove-offscreen-missiles (append LOM3 (cons (make-missile 150 (- (/ (image-height MISSILE) 2))) empty))) LOM3)
(check-expect (remove-offscreen-missiles (cons (make-missile 150 (- (/ (image-height MISSILE) 2))) (cons (make-missile 150 50) empty)))
              (cons (make-missile 150 50) empty))

; (define (remove-offscreen-missiles lom) lom) ; stub
; <Template taken from ListOfMissile>

(define (remove-offscreen-missiles lom)
  (cond [(empty? lom) empty]
        [else
         (if (missile-top? (first lom))
             (remove-offscreen-missiles (rest lom))
             (cons (first lom) (remove-offscreen-missiles (rest lom))))]))


;; Missile -> Boolean
;; Produce true if the missile is past the top of the BACKGROUND
(check-expect (missile-top? (make-missile 150 50)) false)
(check-expect (missile-top? (make-missile 150 -25)) true)
(check-expect (missile-top? (make-missile 150 (- (/ (image-height MISSILE) 2)))) true)

; (define (missile-top? m) false) ; stub
; <Template taken from Missile>

(define (missile-top? m)
  (<= (missile-y m) (- (/ (image-height MISSILE) 2))))


;; Tank -> Tank
;; Advance Tank, prevent Tank from going past left and right edge of BACKGROUND
(check-expect (update-tank T1) (make-tank (+ (* (tank-dir T1) TANK-SPEED) (tank-x T1)) (tank-dir T1)))
(check-expect (update-tank (make-tank (/ (image-width TANK) 2) -1)) (make-tank (/ (image-width TANK) 2) -1)) ; tank reached left edge
(check-expect (update-tank (make-tank (/ (image-width TANK) 2) 1)) (make-tank (+ (/ (image-width TANK) 2) TANK-SPEED) 1)) ; tank at left edge moving right
(check-expect (update-tank (make-tank (- WIDTH (/ (image-width TANK) 2)) 1)) (make-tank (- WIDTH (/ (image-width TANK) 2)) 1)) ; tank reached right edge
(check-expect (update-tank (make-tank (- WIDTH (/ (image-width TANK) 2)) -1)) (make-tank (- (- WIDTH (/ (image-width TANK) 2)) TANK-SPEED) -1)) ; tank at right edge moving left

; (define (update-tank t) t) ; stub
; <Template taken from Tank>

(define (update-tank t)
  (cond [(and (tank-left-edge? t) (= (tank-dir t) -1)) t]
        [(and (tank-right-edge? t) (= (tank-dir t) 1)) t]
        [else (move-tank t)]))


;; Tank -> Boolean
;; Produce true if tank has reached left edge of BACKGROUND, false otherwise
(check-expect (tank-left-edge? (make-tank 0 -1)) (<= 0 (/ (image-width TANK) 2)))
(check-expect (tank-left-edge? (make-tank 150 1)) (<= 150 (/ (image-width TANK) 2)))

; (define (tank-left-edge? t) false) ; stub
; <Template taken from Tank>

(define (tank-left-edge? t)
  (<= (tank-x t) (/ (image-width TANK) 2)))


;; Tank -> Boolean
;; Produce true if tank has reached right edge of BACKGROUND, false otherwise
(check-expect (tank-right-edge? (make-tank 200 1)) (>= 200 (- WIDTH (/ (image-width TANK) 2))))
(check-expect (tank-right-edge? (make-tank WIDTH -1)) (>= WIDTH (- WIDTH (/ (image-width TANK) 2))))

; (define (tank-right-edge? t) false) ; stub
; <Template taken from Tank>

(define (tank-right-edge? t)
  (>= (tank-x t) (- WIDTH (/ (image-width TANK) 2))))


;; Tank -> Tank
;; Move tank by TANK-SPEED
(check-expect (update-tank (make-tank 150 1)) (make-tank (+ 150 TANK-SPEED) 1))
(check-expect (update-tank (make-tank 230 -1)) (make-tank (- 230 TANK-SPEED) -1))

; (define (move-tank t) t) ; stub
; <Template taken from Tank>

(define (move-tank t)
  (make-tank (+ (* (tank-dir t) TANK-SPEED) (tank-x t)) (tank-dir t)))


;; =========TO DRAW FUNCTIONS==========
;; Game -> Image
;; Render the invaders, missiles, and tank on BACKGROUND
(check-expect (render-game G1) (render-invaders (game-invaders G1) (render-missiles (game-missiles G1) (render-tank (game-tank G1) BACKGROUND))))
(check-expect (render-game G2) (render-invaders (game-invaders G2) (render-missiles (game-missiles G2) (render-tank (game-tank G2) BACKGROUND))))
(check-expect (render-game G3) (render-invaders (game-invaders G3) (render-missiles (game-missiles G3) (render-tank (game-tank G3) BACKGROUND))))

; (define (render-game g) BACKGROUND) ; stub
; <Template taken from Game>

(define (render-game g)
  (render-invaders (game-invaders g) (render-missiles (game-missiles g) (render-tank (game-tank g) BACKGROUND))))


;; Tank Image -> Image
;; Render tank on consumed image at tank's x and at bottom of screen (HEIGHT - TANK-HEIGHT/2)
(check-expect (render-tank T0 BACKGROUND) (place-image TANK (tank-x T0) (- HEIGHT TANK-HEIGHT/2) BACKGROUND))
(check-expect (render-tank T1 BACKGROUND) (place-image TANK (tank-x T1) (- HEIGHT TANK-HEIGHT/2) BACKGROUND))

; (define (render-tank t img) BACKGROUND) ; stub
; <Template taken from Tank>

(define (render-tank t img)
  (place-image TANK (tank-x t) (- HEIGHT TANK-HEIGHT/2) img))


;; ListOfMissile Image -> Image
;; Render lom's on consumed image
(check-expect (render-missiles LOM0 BACKGROUND) BACKGROUND)
(check-expect (render-missiles LOM1 BACKGROUND) (render-missile M1 BACKGROUND))
(check-expect (render-missiles LOM2 BACKGROUND) (render-missile M2 (render-missile M1 BACKGROUND)))

; (define (render-missiles lom img) BACKGROUND) ; stub
; <Template taken from ListOfMissile>

(define (render-missiles lom img)
  (cond [(empty? lom) img]
        [else
         (render-missile (first lom) (render-missiles (rest lom) img))]))


;; Missile Image -> Image
;; Render missile's x and y position on consumed image
(check-expect (render-missile M1 BACKGROUND) (place-image MISSILE (missile-x M1) (missile-y M1) BACKGROUND))
(check-expect (render-missile M2 BACKGROUND) (place-image MISSILE (missile-x M2) (missile-y M2) BACKGROUND))

; (define (render-missile m img) BACKGROUND) ; stub
; <Template taken from Missile>

(define (render-missile m img)
  (place-image MISSILE (missile-x m) (missile-y m) img))


;; ListOfInvader Image -> Image
;; Render loi on consumed image
(check-expect (render-invaders LOI0 BACKGROUND) BACKGROUND)
(check-expect (render-invaders LOI1 BACKGROUND) (render-invader I1 BACKGROUND))
(check-expect (render-invaders LOI2 BACKGROUND) (render-invader I2 (render-invader I1 BACKGROUND)))

; (define (render-invaders loi img) BACKGROUND) ; stub
; <Template taken from ListOfInvader>

(define (render-invaders loi img)
  (cond [(empty? loi) img]
        [else
         (render-invader (first loi) (render-invaders (rest loi) img))]))


;; Invader Image -> Image
;; Render invader's x and y position on consumed image
(check-expect (render-invader I1 BACKGROUND) (place-image INVADER (invader-x I1) (invader-y I1) BACKGROUND))
(check-expect (render-invader I2 BACKGROUND) (place-image INVADER (invader-x I2) (invader-y I2) BACKGROUND))

; (define (render-invader i img) BACKGROUND) ; stub
; <Template taken from Invader>

(define (render-invader i img)
  (place-image INVADER (invader-x i) (invader-y i) img))


;; =========STOP WHEN FUNCTIONS==========
;; Game -> Boolean
;; Produce true if game is over (an invader has reached bottom edge of BACKGROUND)
(check-expect (game-over? G1) (invader-bottom? (game-invaders G1)))
(check-expect (game-over? G3) (invader-bottom? (game-invaders G3)))

; (define (game-over? g) false) ; stub
; <Template taken from Game>

(define (game-over? g)
  (invader-bottom? (game-invaders g)))


;; ListOfInvaders -> Boolean
;; Produce true if loi contains invader which passed bottom edge of BACKGROUND
(check-expect (invader-bottom? empty) false)
(check-expect (invader-bottom? LOI1) false)
(check-expect (invader-bottom? LOI2) true)
(check-expect (invader-bottom? LOI3) true)

; (define (invader-passed? loi) false) ; stub
; <Template taken from ListOfInvader>

(define (invader-bottom? loi)
  (cond [(empty? loi) false]
        [else
         (if (>= (invader-y (first loi)) HEIGHT)
             true
             (invader-bottom? (rest loi)))]))


;; =========KEY EVENT FUNCTIONS==========
;; Game KeyEvent -> Game
;; Move tank left or right with left or right arrow keys or 
;;    shoot missiles from tank using space key
(check-expect (handle-key-event (make-game empty empty (make-tank 50 -1)) "left") (change-tank-dir (make-game empty empty (make-tank 50 -1)) -1))
(check-expect (handle-key-event (make-game empty empty (make-tank 50 1)) "left") (change-tank-dir (make-game empty empty (make-tank 50 1)) -1))
(check-expect (handle-key-event (make-game empty empty (make-tank 50 -1)) "right") (change-tank-dir (make-game empty empty (make-tank 50 -1)) 1))
(check-expect (handle-key-event (make-game empty empty (make-tank 50 1)) "right") (change-tank-dir (make-game empty empty (make-tank 50 1)) 1))
(check-expect (handle-key-event (make-game empty empty T1) " ") (shoot-missile (make-game empty empty T1)))
(check-expect (handle-key-event (make-game (list I1) (list M1) T1) " ") (shoot-missile (make-game (list I1) (list M1) T1)))

; (define (handle-key-event g ke) G0) ; stub
#;
(define (handle-key-event g ke)
  (cond [(key=? "left" ke) (... g)]
        [(key=? "right" ke) (... g)]
        [(key=? " " ke) (... g)]
        [else g]))
;; Template formed using the large enumeration case

(define (handle-key-event g ke)
  (cond [(key=? "left" ke) (change-tank-dir g -1)]
        [(key=? "right" ke) (change-tank-dir g 1)]
        [(key=? " " ke) (shoot-missile g)]
        [else g]))


;; Game -> Game
;; Launch a missile from Tank
(check-expect (shoot-missile (make-game empty empty T1)) (make-game empty (add-missile-lom empty T1) T1))
(check-expect (shoot-missile (make-game (list I1) (list M1) T1)) (make-game (list I1) (add-missile-lom (list M1) T1) T1))

;(define (shoot-missile g) g) ; stub
; <Template taken from Game>
(define (shoot-missile g)
  (make-game (game-invaders g) (add-missile-lom (game-missiles g) (game-tank g)) (game-tank g)))


;; ListOfMissile Tank -> ListOfMissile
;; Add a missile to consumed lom from tank's current position
(check-expect (add-missile-lom empty T1) (cons (make-missile (tank-x T1) (- HEIGHT (image-height TANK))) empty))
(check-expect (add-missile-lom (list M1) T1) (cons (make-missile (tank-x T1) (- HEIGHT (image-height TANK))) (cons M1 empty)))

; (define (add-missile-lom lom t) lom) ; stub
; <Template taken from ListOfMissile>

(define (add-missile-lom lom t)
  (cons (make-missile (tank-x t) (- HEIGHT (image-height TANK))) lom))


;; Game Direction -> Game
;; Change direction of game's tank based off of consumed direction value
(check-expect (change-tank-dir (make-game empty empty (make-tank 50 -1)) -1) (make-game empty empty (make-tank 50 -1)))
(check-expect (change-tank-dir (make-game empty empty (make-tank 50 -1)) 1) (make-game empty empty (make-tank 50 1)))
(check-expect (change-tank-dir (make-game empty empty (make-tank 50 1)) -1) (make-game empty empty (make-tank 50 -1)))
(check-expect (change-tank-dir (make-game empty empty (make-tank 50 1)) 1) (make-game empty empty (make-tank 50 1)))

; (define (change-tank-dir g d) g) ; stub
; <Template taken from Game>

(define (change-tank-dir g d)
  (make-game (game-invaders g) (game-missiles g) (make-tank (tank-x (game-tank g)) d)))