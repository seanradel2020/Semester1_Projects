#Sean Radel
#December 11 2020
#  **I Did Not get any help from anyone on this project**
# **However, I did help Ryan Ciesinski, Zach hatch, Ayan Tari, and Dharani, understand the recursion portion of the project.
#  I did not show them any code, I just explained how to use recursion  **
"The more basic the color, the more inward, the more pure. - Piet Mondrian"

#(Algorithm for myslef to follow 0.0)
#https://www.bing.com/images/search?view=detailV2&ccid=0SAX5GoP&id=43123FA6983335FA6D518ED3057C51C0C12C5630&thid=OIP.0SAX5GoP7VbvXW72N-Z6kAHaEo&mediaurl=http%3a%2f%2f1.bp.blogspot.com%2f-4In4tQ3X17E%2fT8Fiv7vhpKI%2fAAAAAAAAB0c%2fPLXKC58ytCY%2fs1600%2finspired_bei_mondrian_by_manshonyagger-d35kfou.png&exph=707&expw=1131&q=mondrian+art&simid=608037953622968899&ck=C8F442C0D31B81AD7F4A6480966DABFA&selectedIndex=11&FORM=IRPRST&ajaxhist=0
#How I'm going to do something like that ^^ (image of mondrian art)
#
#           Givens: 800,800 canvas; Stroke width 3, color: black
#           rect colors will be black yellow blue white
            # red rgb = (255,0,0) blue = (0,0,255) yellow = (255,255,0) black = (0,0,0) white = (255,255,255)
            #color breakdown like .0833 yellow .1667 blue .25 red else white
            #

            #Max width or height is 120

#split
#Dimensions cut in half
#y + 400
#x + 400
#take the complement of the size, add it to the coordinate
#2 new dimension lists
#if decide by width and random chance

#split hot dog or hamburger style
# make 2 different regions now
"Intellect confuses intuition. ~ Piet Mondrian"
#if x or y is 20 or less and x or y is not greater than 120
#draw that thing
#if x #or y is = OR <120
#.48 chance it splits (recurses)
#make two regions
#recurse on the regions
#else
#draw that thing
#else recurse
#($plit)

import random
flipper = False

"abstract art is not the creation of another reality but the true vision of reality. ~ Piet Mondrian"


dimensionList = ["800","800", "0","0"]
directions = ["<html>"
,"<head></head>"
,"<body>",
"<svg width = '800' height='800'>"
]

"The emotion of beauty is always obscured by the appearance of the object. Therefore, the object must be eliminated from the picture. ~ Piet Mondrian"

def splitter(dimension): #Split dimesnions by making a fraction of a whole region, region A will be the complement to region B, return both of them
    w = int(dimension[0])
    h = int(dimension[1])
    x = int(dimension[2])
    y = int(dimension[3])
    split = random.randint(33, 67)/100
    rando = random.randint(0, 100) #add a bit of random in it

    if rando > 90:#split by width
        #split hamburger style
        w1 = w * split
        w2 = w - w1
        x2 = x + w1
        mon = [[w1,h,x,y],[w2,h,x2,y]]
        return mon
    elif rando > 80 and rando < 90:#split by height
        #split hotdog style
        h1 = h * split
        h2 = h - h1
        y2 = y + h1
        mon = [[w,h1,x,y],[w,h2,x,y2]]
        return mon
    elif w < h: #split by height
        #verticle (hotdog split)
        h1 = h * split
        h2 = h - h1
        y2 = y + h1
        mon = [[w,h1,x,y],[w,h2,x,y2]]
        return mon
    else: #hamburger split #split by width
        w1 = w * split
        w2 = w - w1
        x2 = x + w1
        mon = [[w1,h,x,y],[w2,h,x2,y]]
        return mon


"The surface of things gives enjoyment, their interiority gives life. ~ Piet Mondrian"

def seandrian(dimension):
    global flipper

    if (int(dimension[0]) < 21 or int(dimension[1]) < 21) and (int(dimension[0]) < 121 or int(dimension[0]) < 121):
        directions.append(stringBuilder(dimension))
    elif (int(dimension[0]) < 121 or int(dimension[1]) < 121):
        rand = random.random()
        if rand < .49:
            b = splitter(dimension)
            seandrian(b[0])#Call the function on the 2 new regions
            seandrian(b[1])
        else:
            directions.append(stringBuilder(dimension))
            if ("(255,255,255)" in directions[len(directions)-1]) and flipper == True :
                a = directions[len(directions)-2]
                a1 = directions[len(directions)-1]
                directions[len(directions)-2] = a1
                directions[len(directions)-1] = a

    else:
        b = splitter(dimension)
        seandrian(b[0])#Call the function on the 2 new regions
        seandrian(b[1])


"Art is not made for anybody and is, at the same time, for everybody. ~ Piet Mondrian"


def stringBuilder(dims):
    global flipper
    rand = random.random()
    # red rgb = (255,0,0) blue = (0,0,255) yellow = (255,255,0) black = (0,0,0) white = (255,255,255)
    #color breakdown like .0833 yellow .1667 blue .20 red .0833 black else white
    if rand < .0833:
        color = "(118,17,55)"
    elif rand > .0833 and rand < .25:
        color = "(237,51,95)"
    elif rand > .25 and rand < .45:
        color = "(249,133,139)"
    else:
        color = "(255,255,255)"
    fill = "fill:rgb"
    color = fill + color
# <text x="10" y="15" fill="red">LOVE</text>
    if (color == "fill:rgb(255,255,255)") and (dims[0] > 60) and (dims[1] > 25): #If color is white,and big enough add "Love" to it
        flipper = True
        code = f'<rect width="{dims[0]}" height="{dims[1]}" x="{dims[2]}" y="{dims[3]}" style="{color};stroke-width:3;stroke:rgb(0,0,0)"/>'
        #b = (int(dims[3]) / 2) - 10
        directions.append( f'<text x="{dims[2]+5}" y="{dims[3]+20}" fill="red">LOVE</text>')
        return code



    else:
        code = f'<rect width="{dims[0]}" height="{dims[1]}" x="{dims[2]}" y="{dims[3]}" style="{color};stroke-width:3;stroke:rgb(0,0,0)"/>'
        return code


"Curves are so emotional. ~ Piet Mondrian"   # <----- My favorite quote right there

def writerToHtmler():
    htmlfile = input("Enter the name of the file you'd like to save to")
    seandrian(dimensionList)
    directions.append("</svg>")
    directions.append("</body>")
    directions.append("</html>")
    #html = open("mondr.txt", "w")
    html = open(htmlfile, "w") #Uncomment this if you want to just test without writing out the file name each time
    for j in range(len(directions)-1):
        line = directions[j]
        print(line, file = html)
    html.close()

"I don't want pictures, I want to find things out. ~ Piet Mondrian"

writerToHtmler()
