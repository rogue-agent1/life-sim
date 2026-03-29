#!/usr/bin/env python3
"""life_sim - Conway's Game of Life."""
import sys, argparse, json, random, time

def random_grid(w, h, density=0.3):
    return [[1 if random.random() < density else 0 for _ in range(w)] for _ in range(h)]

def step(grid):
    h, w = len(grid), len(grid[0])
    new = [[0]*w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            n = sum(grid[(y+dy)%h][(x+dx)%w] for dy in (-1,0,1) for dx in (-1,0,1) if (dy,dx)!=(0,0))
            if grid[y][x]:
                new[y][x] = 1 if n in (2,3) else 0
            else:
                new[y][x] = 1 if n == 3 else 0
    return new

def render(grid):
    return "
".join("".join("█" if c else " " for c in row) for row in grid)

def count_alive(grid):
    return sum(sum(row) for row in grid)

def main():
    p = argparse.ArgumentParser(description="Game of Life")
    p.add_argument("--width", type=int, default=40)
    p.add_argument("--height", type=int, default=20)
    p.add_argument("--steps", type=int, default=10)
    p.add_argument("--density", type=float, default=0.3)
    p.add_argument("--seed", type=int)
    p.add_argument("--json", action="store_true")
    args = p.parse_args()
    if args.seed: random.seed(args.seed)
    grid = random_grid(args.width, args.height, args.density)
    history = [{"step": 0, "alive": count_alive(grid)}]
    for i in range(1, args.steps + 1):
        grid = step(grid)
        history.append({"step": i, "alive": count_alive(grid)})
    if args.json:
        print(json.dumps({"width": args.width, "height": args.height, "steps": args.steps, "history": history}))
    else:
        print(render(grid))
        print(f"
Step {args.steps}: {count_alive(grid)} alive cells")

if __name__ == "__main__": main()
