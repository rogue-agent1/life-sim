#!/usr/bin/env python3
"""Conway's Game of Life simulator."""
import sys, time, random

def random_grid(w, h, density=0.3):
    return {(x,y) for x in range(w) for y in range(h) if random.random() < density}

def step(cells):
    neighbors = {}
    for x, y in cells:
        for dx in (-1,0,1):
            for dy in (-1,0,1):
                if dx or dy:
                    neighbors[(x+dx,y+dy)] = neighbors.get((x+dx,y+dy), 0) + 1
    return {pos for pos, n in neighbors.items() if n == 3 or (n == 2 and pos in cells)}

def render(cells, w, h):
    return '\n'.join(''.join('██' if (x,y) in cells else '  ' for x in range(w)) for y in range(h))

def glider(x=1, y=1):
    return {(x+1,y),(x+2,y+1),(x,y+2),(x+1,y+2),(x+2,y+2)}

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('-W', '--width', type=int, default=40)
    p.add_argument('-H', '--height', type=int, default=20)
    p.add_argument('-g', '--generations', type=int, default=100)
    p.add_argument('--glider', action='store_true')
    p.add_argument('--seed', type=int)
    args = p.parse_args()
    if args.seed: random.seed(args.seed)
    cells = glider() if args.glider else random_grid(args.width, args.height)
    for gen in range(args.generations):
        sys.stdout.write(f"\033[H\033[J")
        print(f"Generation {gen} | Population: {len(cells)}")
        print(render(cells, args.width, args.height))
        cells = step(cells)
        time.sleep(0.1)
