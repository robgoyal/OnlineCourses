# Questions

## What's `stdint.h`?

A header file which consists of sets of integer types having specified widths.

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

They allow to succintly specify the types of data along with information regarding their sign. An example is `uint8_t` which provides a range of numbers between 0 to 255 whereas `int8_t` provides -128 to 127 as the range.

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

A `BYTE` is 8 bits, `DWORD` is 32 bits, `LONG` is 32 bits, and a `WORD` is 16 bits.

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

The first two bytes must be BM to specify that its a bitmap.

## What's the difference between `bfSize` and `biSize`?

`bfSize` is the size of the entire bmp file. `biSize` is the size of the `BITMAPINFOHEADER` structure.

## What does it mean if `biHeight` is negative?

`biHeight` being negative means that the bitmap is top-down and the origin begins at the upper left corner.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

`biBitCount` specifies the number of bits per pixel.

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

`fopen` might return `NULL` in case the file that was being passed in doesn't exist.

## Why is the third argument to `fread` always `1` in our code?

`fread` is always `1` since we only want to read one chunk of the entire structure at a time.

## What value does line 63 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

`padding` will be equal to `3`.

## What does `fseek` do?

`fseek` is a function which allows you move the file pointer to a given location.

## What is `SEEK_CUR`?

`SEEK_CUR` is a constant which specifies the current file pointer location.
