#!/usr/bin/env python3
"""life_sim - Simple artificial life simulation."""
import sys,random
class Creature:
    def __init__(s,x,y,energy=50):s.x=x;s.y=y;s.energy=energy;s.age=0
    def move(s,w,h):
        s.x=(s.x+random.choice([-1,0,1]))%w;s.y=(s.y+random.choice([-1,0,1]))%h;s.energy-=1;s.age+=1
    def alive(s):return s.energy>0
    def reproduce(s):
        if s.energy>80:s.energy-=30;return Creature(s.x,s.y,30)
        return None
class World:
    def __init__(s,w=40,h=20,food=100,creatures=20):
        s.w=w;s.h=h;s.food=set();s.creatures=[]
        for _ in range(food):s.food.add((random.randint(0,w-1),random.randint(0,h-1)))
        for _ in range(creatures):s.creatures.append(Creature(random.randint(0,w-1),random.randint(0,h-1)))
    def step(s):
        for c in s.creatures:
            c.move(s.w,s.h)
            if(c.x,c.y) in s.food:c.energy+=20;s.food.discard((c.x,c.y))
            baby=c.reproduce()
            if baby:s.creatures.append(baby)
        s.creatures=[c for c in s.creatures if c.alive()]
        for _ in range(3):s.food.add((random.randint(0,s.w-1),random.randint(0,s.h-1)))
    def display(s):
        grid={}
        for f in s.food:grid[f]="·"
        for c in s.creatures:grid[(c.x,c.y)]="@"
        for y in range(s.h):print("".join(grid.get((x,y)," ") for x in range(s.w)))
        print(f"Creatures: {len(s.creatures)}, Food: {len(s.food)}")
if __name__=="__main__":
    steps=int(sys.argv[1]) if len(sys.argv)>1 else 100
    w=World();
    for i in range(steps):
        w.step()
        if i%10==0:print(f"\nStep {i}: {len(w.creatures)} creatures, {len(w.food)} food")
    w.display()
