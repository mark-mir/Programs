from functools import lru_cache

def moves(h):
    return h + 1, h + 4, h * 3

@lru_cache(None)
def game(h):
    if h >= 88:
        return 'win'
    if any(game(m) == 'win' for m in moves(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in moves(h)):
        return 'B1'
    if any(game(m) == 'B1' for m in moves(h)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)):
        return 'B2'

for s in range(1, 88):
    if game(s) == 'B1':
        print(s, game(s))
