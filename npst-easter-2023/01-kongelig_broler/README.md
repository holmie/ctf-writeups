# 01.04.2023 - Kongelig Brøler
The challenge text says that "Pen GWYN" was caught in the security check at the airport. He had a chess board with him and a document that seems to be encrypted.

The file was called fen.txt and contained
```FEN "8/2kqrn2/2b2b2/2nrpp2/2p5/2p5/8/8 w - - 0 1",
FEN "8/2kqrn2/2b5/2bnrp2/5p2/2pppp2/8/8 w - - 0 1",
FEN "8/1kqrnb2/3b4/3n4/3r4/3p4/8/8 w - - 0 1",
FEN "8/3kq3/3r4/2nb4/3b4/3nr3/8/8 w - - 0 1",
``` etc...

I play a bit of recreational chess and recognized the Forsyth-Edwards Notation
The format goes like;
The board "lines" are separated by slashes, numbers means no pieces for the next *number* squares.
Then the characters represents the pieces, colors depends on uppercase/lowercase.

Taking the line
```FEN "8/2kqrn2/2b2b2/2nrpp2/2p5/2p5/8/8 w - - 0 1",```
Means the first row is empty, then the two first squares on the next row contains king, queen, etc.
As you can see it forms

```00000000
00111100
00100100
00111100
00100000
00100000
00000000
00000000
```

Looking at this like a picture it forms a P.
Then iterate over all the lines and you'll see that the string is:
**PST{NOEN_UVANLIGE_STILLINGER}**

I actually made a crazy script (solve.py) to just parse this stuff and create images, I was thinking about doing OCR on it, but one only has so much time. :P


But there's more, there are three "characters" that contains pieces in every square... what can it be?
Giving that there are 8 squares in each row, maybe they encoded 8 bit ascii into FEN?
The first row was "pBrpnRrB", so I tried the theory:
```>>> chr(0b01000101)
'E'
```
Interesting, I mocked up a simple script to iterate over the lines and got an extra flag EGG{Kule_sjakkvarianter}.
