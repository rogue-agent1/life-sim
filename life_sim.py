#!/usr/bin/env python3
"""life_sim - Conway's Game of Life."""
import sys, time, os, random
def random_grid(w, h, density=0.3):
    return {(r, c) for r in range(h) for c in range(w) if random.random() < density}
def step(cells, w, h):
    neighbors = {}
    for r, c in cells:
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0: continue
                nr, nc = (r+dr) % h, (c+dc) % w
                neighbors[(nr, nc)] = neighbors.get((nr, nc), 0) + 1
    new = set()
    for pos, n in neighbors.items():
        if n == 3 or (n == 2 and pos in cells): new.add(pos)
    return new
def display(cells, w, h):
    for r in range(h):
        print("".join("█" if (r, c) in cells else " " for c in range(w)))
PATTERNS = {
    "glider": {(0,1),(1,2),(2,0),(2,1),(2,2)},
    "blinker": {(1,0),(1,1),(1,2)},
    "block": {(0,0),(0,1),(1,0),(1,1)},
}
if __name__ == "__main__":
    w, h = 40, 20
    gens = int(sys.argv[1]) if len(sys.argv) > 1 else 50
    pattern = sys.argv[2] if len(sys.argv) > 2 else "random"
    cells = PATTERNS.get(pattern, random_grid(w, h))
    for g in range(gens):
        os.system("clear" if os.name != "nt" else "cls")
        print(f"Generation {g} | Population: {len(cells)}")
        display(cells, w, h); cells = step(cells, w, h)
        time.sleep(0.1)
