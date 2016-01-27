## This is a combination of Listings 9.6, 9.7 (with a bug fix), and
## 9.8 (with minor improvements) from Python Programming in Context by
## Miller and Ranum to serve as a starting point for an MCS-177
## project.

from cTurtle import Turtle
import random
aTurtle=Turtle();
##aTurtle=Turtle();
## Listing 9.6
# applyProduction: string dict-of-char:string integer -> string
def applyProduction(axiom,rules,n):
    
    for i in range(n):
        newString = ""
        for ch in axiom:
            
            newString = newString + random.choice(rules.get(ch,ch))
            
        axiom = newString
    return axiom

## Listing 9.7
# drawLS: Turtle string number number -> void
def drawLS(aTurtle,instructions,angle,distance):
    stateSaver = []
    for cmd in instructions:
        if cmd == 'G':
            aTurtle.up();
            aTurtle.forward(distance);
            aTurtle.down();
        if cmd == 'F':
            
            aTurtle.forward(distance)
            
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == '[':
            pos = aTurtle.position()
            head = aTurtle.heading()
            stateSaver.append((pos,head))
        elif cmd == ']':
            pos,head = stateSaver.pop()
            aTurtle.up()   # this line was not in Listing 9.7 (a bug)
            aTurtle.setposition(pos)
            aTurtle.setheading(head)
            aTurtle.down() # this line was not in Listing 9.7 (a bug)

## Listing 9.8
# lsystem: string dict-of-char:string integer (integer, integer) number number number -> void
def lsystem(axiom,rules,depth,initialPosition,heading,angle,length):
    
    aTurtle = Turtle()
    
    aTurtle.speed(10)       # this line improves on Listing 9.8
    aTurtle.shape('blank') # this line improves on Listing 9.8
    aTurtle.up()
    aTurtle.setposition(initialPosition)
    aTurtle.down()
    aTurtle.setheading(heading)
    ## The variable "instructions" was called "newRules" in Listing 9.8,
    ## which was misleading regarding what kind of thing it names.
    instructions = applyProduction(axiom,rules,depth)

    drawLS(aTurtle,instructions,angle,length)
    aTurtle.exitOnClick()

def recursiveSort(List,lo,hi):
    
    maxNum=List[lo];
    for num in List[lo:hi]:
        if (num>maxNum):
            maxNum=num;
            
    if (List.index(maxNum)!=hi-1):
        maxIndex=List.index(maxNum)
        c=List[hi-1]
        List[hi-1]=maxNum
        List[maxIndex]=c
    
    if (hi>lo+1):
        recursiveSort(List,lo,hi-1)

def sortList(List):
    recursiveSort(List,0,len(List));
    return List;

#task 1: Level 4 Koch curve with segment length unit of 6. (remove comment to run).
# lsystem('F',{'F':['F-F++F-F']},4,(-216,0),0,60,6)

#task 2: Modify the code to support the 'G' operation.

#task 3: Draw the Sierpinski triangle:
# lsystem('F-F-F',{'F':['F-F-F-GG'],'G':['GG']},4,(0,0),0,120,6)
'''Task 3 explanation
    The alternative rule which is F-F-F will draw an triangle; the rule -GG will move the turtle forward without drawing
    anything. For level 0, it draws only a triangle. In level 1, each F in level 0 (represented by a side of the triangle) becomes a new
    triangle (drawn by the rule F-F-F). After each triangle is drawn, the pointer is moved to a new position by the rule -GG to draw a new triangle,
    replacing the previous triangle's side from level 0. In level 2, each F in level 1 becomes a new triangle (drawn by the rule F-F-F)
    and the pointer is moved to a new position by the rule -GG, so on and so forth.
    The overall picture is a big triangle, inside which small triangles are located. In side the small triangles, there are smaller
    triangles, so on and so forth. The higher the level is, the more triangles inside triangles are.
'''

#task 4: Draw fractal plan
# lsystem('F',{'F':['F[-F]F[+F]F']},4,(0,-150),90,25,6)

#task 5:
# lsystem('F',{'F':['F[-F]F[+F]F','F[-F]F','F[+F]F']},4,(0,0),0,90,6)

#task 6:
# lsystem('F',{'F':['FF-[-F+F+F]+[+F-F-F]']},4,(-9,0),90,22.5,6)
# lsystem('F',{'F':['F[+F[+F][-F]F][-F[+F][-F]F]F[+F][-F]F']},4,(-9,0),90,30,6)
    

