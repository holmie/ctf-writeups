#!/usr/bin/env python3
import string
fen = "/".join(["pBrpnRrB/nPpbrBPP/rRbnpNBR/pBNBPrPP/pNrnNpPR/rPRBbNrB/bBPpNPpn/rPRbpRrN", "nRrBBRPN/bBPNnrPP/rRPnRpNr/rNPbnprB/pPNbPbRP/rBRpNrBP/rNBRrPRp/nPBrbnrN", "pPNBrbPp/bNBnPnrP/rNRbbprB/bPBrBPBr/pBNRrNnp/pPBnpPpP/rNBRnrBn/bNPBRRnN"])
solve = ""
for l in fen.split('/'):
    out = 0
    for idx, c in enumerate(l):
        if c in string.ascii_lowercase:
            out |= 0 << (7 - idx)
        else:
            out |= 1 << (7 - idx)
    solve += chr(out)

print(solve)
