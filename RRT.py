import pygame
import random
from RRTbasePy import RRTGraph
from RRTbasePy import RRTMap

def main():
    dimensions = (600,1000)
    start = (50,50)
    goal = (510,510)
    obsdim = 30
    obsnum = 50
    iteration = 0

    pygame.init()
    map=RRTMap(start,goal,dimensions,obsdim,obsnum)
    graph=RRTGraph(start,goal,dimensions,obsdim,obsnum)

    obstacles=graph.makeObs()
    map.drawMap(obstacles)

    while(iteration<500):
        if (random.uniform(0,100)<2):
            X,Y,Parent = graph.bias(goal)
            pygame.draw.circle(map.map,map.grey,(X[-1],Y[-1]),map.nodeRad,0)
            pygame.draw.line(map.map,map.Blue,(X[-1],Y[-1]),(X[Parent[-1]],Y[Parent[-1]]),map.edgeThickness)

        else:
            X,Y,Parent = graph.expand()
            pygame.draw.circle(map.map,map.grey,(X[-1],Y[-1]),map.nodeRad,0)
            pygame.draw.line(map.map,map.Blue,(X[-1],Y[-1]),(X[Parent[-1]],Y[Parent[-1]]),map.edgeThickness)

        
        pygame.display.update()
        pygame.event.wait(25)
        iteration=iteration+1
        if(graph.goalFlag==True):
            break

    pygame.display.update()
    pygame.event.clear()
    pygame.event.wait(0)


if __name__ == '__main__':
    main()