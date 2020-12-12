#Sean Radel
#Project1
#*I did not collaborate with any students, teachers, etc.*
#I used (https://stackoverflow.com/questions/12386199/applying-multiple-filters-to-list-of-tuples) as a reference
#for help with my function "def listFilter(rankings):"
#Nov. 2020
#cos125

def opt1(lines,word):
    sentimentFound = [] #add sentiment values here


#input word
# check word to each word of a line, as soon as a match is found <--- add line's sentiment value to a list, move to the next line,
#check next line, and so on
#sigma found sentiments, divided by number of recorded sentiments
    for line in range(len(lines)): #iterate through each line

        temp = [] #temporary list, created and destroyed in each loop
        temp.append(lines[line].split())

        for i in range(len(temp[[0][0]])):

            if word == str(temp[[0][0]][i].lower()): #if the word is found

                sentimentFound.append(temp[[0][0]][0]) #add its sentiment value to the list

    avgSent = 0
    for num in sentimentFound:
        avgSent += int(num) #add all of the sentiments together

    foundAmount = len(sentimentFound)
    if foundAmount != 0: #divide to get the mean
        avgSent/= foundAmount

    returnStatement = (avgSent,foundAmount,word) #return as a tuple
    return returnStatement



#This was my first attempt, and a valid way to solve the problem, uncomment it, it will run, but I dont think
#its the write way to approach this problem. this method is too generous with the rating because of garbage words that werent filtered out
#def opt2(lines): #weighted average to correctly average the words, and not just the lines
# (sigma (line's sentiment * words in the line)) / number of lines
#    sentiments = []
#    totalWords = 0
#    for line in range(len(lines)):
#        temp = []
#        temp.append(lines[line].split())
#        temp2 = temp[[0][0]][0]
#        temp2 = int(temp2)* len(temp[[0][0]]) - 1
#        totalWords += len(temp[[0][0]]) - 1
#        sentiments.append(temp2)
#    div = 0
#    for line in sentiments:
#        div += line

#    totalSentiment = div / totalWords
#    return totalSentiment

def opt2(lines): #this is a much better way to find the average sentiment of the words,
# because first we filtered the garbage words, the we find the average
#we use opt3, to give us the words we think are important and their average sentiments. Then find the average among those
    buffer = opt3(lines)
    sentiments = []
    for i in range(len(buffer)-1):
        sentiments.append(buffer[[i][0]][0])

    div = 0
    for line in sentiments:
        div += line

    totalSentiment = div / len(buffer)-1
    return totalSentiment



def opt3(lines):
    # NOTE could use the first function here...except every 'word' is not user input, but a word from the txt... maybe
    #Sort using sorted() because... well its easy and why write my own sorting algo when we've got sorted()...

#we use the first function to find the sentiment of each word, then each words sentiment, amount of uses, and the word is stored in a tuple
# then that tuple is filtered to take out all of the garbage words that I don't want to be accounted for, then we sort those tuples
#by avg sentiment value. Then we get the best and worst sentiment words by picking from the bottom and from the top of that list
    rankings = []
    #first word of first line,
    for i in range(len(lines)):
        temp = []
        temp.append(lines[i].split())
        for j in range(len(temp[[0][0]])):
            rankings.append(opt1(lines,temp[[0][0]][j]))


    filtered = listFilter(rankings)

    #print(sort(filtered)) print a sorted filtered list
    #Uncomment this if you want to see all the tuples in the list, filtered, and sorted
    return sort(filtered)



def firstOfTuple(n):
    return n[0]

def sort(rankings):
    return sorted(rankings, key=firstOfTuple)

def listFilter(rankings):
    removeList = ["A","a","the","The","their","there","are","is","be","been","but","of","have","in","I","it","not","with","on","as","do"
    , "say", "would","about","can","'s","because","n't","1","2","3","4","0","this","This","Even","even","Ismail","They","If", "then","while"
    ,"had","and","'",".",",","to","an","some","for","that","To","too","Too"] #these are all words that I decided were not useful, should be excluded, or were accidentally being counted as words
    remove = set(removeList)
    rankingsFiltered = [i for i in rankings if not set(i) & remove]
    #I used this page as a reference for the above line
    #https://stackoverflow.com/questions/12386199/applying-multiple-filters-to-list-of-tuples


    return rankingsFiltered

def main():

    #f = open("reviews.txt", "r")
    #lines = []
    #for line in f:
        #lines.append(line)
    #f.close()

    quit = ""
    txtFileName = ""

    while quit.lower() != "quit":
        j = 0
        txtFileName = input("Enter the name of a .txt you would like to analyze ('name'.txt): ")


        f = open(txtFileName, "r")
        lines = []
        for line in f:
            lines.append(line)
        f.close()

        while j != 4:
            print("What would you like to do?")
            print(" 1. Get the sentiment score of a single word")
            print(" 2. Get the average score of words in a file")
            print(" 3. Find the highest and lowest scoring words in a file. ")
            print(" 4. Exit the program")
            nu = int(input("Enter a number 1-4: "))

            if nu == 1:
                word = input("Enter a word ")
                tupler = opt1(lines,word)
                print("'"+word+"'"+" appears "+str(tupler[1])+" times")
                print("the average score for reviews containing "+"'"+word+"'"+" is "+str(tupler[0]))

            if nu == 2:
                avgSentiment = opt2(lines)
                if avgSentiment <= 1.75:
                    print("The average score was "+ str(avgSentiment)+ " This is an insult")
                if avgSentiment > 1.75 and avgSentiment < 2.25:
                    print("The average score was "+ str(avgSentiment)+ " This is neutral")
                if avgSentiment >= 2.25:
                    print("The average score was "+ str(avgSentiment)+ " This is a compliment")


            if nu == 3:
                buffer = opt3(lines)
                print("The most positive word was " + str(buffer[[len(buffer)-1][0]][2]) + " with a score of " + str(buffer[[len(buffer)-1][0]][0]) )
                print("The most negative word was " + str(buffer[[0][0]][2]) + " with a score of " + str(buffer[[0][0]][0]) )

            if nu == 4:
                j = 4
        quit = input("type 'quit' to quit, or <enter> to try another .txt file: ")
main()
