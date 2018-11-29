# How to Code Simple Data Notes

## Basic Language 

### Values

- Natural: whole numbers greater than 0
- Integers: whole numbers negative and positive
- Real/Natural: decimal numbers
- Strings: string types
- Images: primitive type representing images
- Boolean: true/false

There are other primitive types that exist

### Primitive Operations

- Math operations: +, -, *, /
- String operations: string-append, string-length, substring
- Image operations: circle, square, overlay, above, beside
- Boolean/predicate operations: not, =, <, >, string=?

There are many more operations that exist.

### Forming Expressions

#### Value

```racket
3
```

#### Constant
```racket
WIDTH
```

#### Primitive Operation Expression

```racket
(+ 2 (* 3 6))
```

#### Defined Function Expression

```racket
(yell "hello")
```

#### If question

The form of an if question is:

<pre>
(if question
     true-answer
     false-answer)
</pre>

where question is a boolean expression evaluating to true or false, true-answer and false-answer can be any valid expression.

If the boolean condition is true, the true-answer replaces the entire if-expression, else the false-answer replaces the entire if-expression.

#### Multi Conditional

This for multiple conditions similar to an if-elif-else in other languages.

<pre>
(cond [question answer]
	  [question answer]
	  ...)
</pre>

Replace the entire cond expression with the first true question with the corresponding answer.

#### Boolean Logic

An and expression is of the form:

<pre>
(and question ... )
</pre>

And expressions evaluate to false the moment it encounters a false question.

An or expression is of the form:

<pre>
(or question ... )
</pre>

Or expressions evaluate to true the moment it encounters a true question.
### Forming Definitions

#### Constant Definitions

```racket
(define SIZE (* 3 6))
```

#### Function Definitions

```racket
(define (bulb c)
    (circle 30 "solid" c))
```

#### Struct Definitions

```racket
(define-struct wand (wood core length))
```

This creates the following functions as well:

- constructors: make-want
- selectors: wand-wood, wand-core, wand-length
- predicate: wand? 

## Design Recipes

### How to Design Functions Recipe

HtDF is a design method for systematic design of functions. 

Overview of Steps:

- Signature, purpose and stub
- Examples
- Template and Inventory
- Code the function body
- Test and debug until correct

#### Signature, Purpose and Stub

Example:

```racket
;; Number -> Number
;; Produces n times 2

(define (double n) 0) ; stub
```
The signature specifies the type of inputs coming in and the type of output being returned. For multiple input types, separate them by a space.

The purpose is a one-line statement explaining what the function does. Explain what the function produces in what situations as well as edge cases.

The stub is a complete function definition which produces a value of the right type. This allows you to run the function against the examples to verify that the function and examples are well-formed.

#### Examples

Examples are useful to verify that the function will behave as you expect it to. Examples should cover normal and boundary cases. The examples should cover all behaviours of the function.

Examples:

```racket
(check-expect (double 0) (* 0 2))
(check-expect (double 1) (* 1 2))
```
These examples use the stub with the correct arguments and same output type. It's also better for the output to be computed in the way you expect it to rather than just writing out the answer.

#### Template and Inventory

Template provides an idea of what the function has to work with (arguments and constants). Data Drive Templates will assist in what the template should look like for the consumed types.

Example:

```racket
(define (double n)  ; template
    (... n))
```
#### Code Body

Comment out the template and re-write the template out. Fill in the body using the above components of the function design recipe. 

Example:

```racket
(define (double n)
    (* n 2))
```

The body was easy to write since we created examples explaining what the function was supposed to do.

#### Test and Debug

Run the program, ensure check-expects pass, and debug if any issues.

### How to Design Data
