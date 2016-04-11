# MYP-PROJECT
personlist=['Toni Braxton','Lee Glath','Phillip Glass','Eubie Blake']
gquestions=["Helo"]
answertoni=['yaaaaaaas']
answerlee=['I was born September 10th, 1902','I died at 66 years old on November 10th, 1968, this is my ghost speaking. Don’t ask why my fingers don’t just go through the computer.','I was born in Baltimore, MD','I used lyrical abstractions and brought a fresh perspective to art, even though you could interpret my art as a bunch of random watercolor shapes','I, according to wikipedia, “paint[ed] the figure and nature “through interwoven patterns of flattened figures,”” a flowery version of saying I made a bunch of shapes out of watercolors','I used different stylistically interesting shapes and drew abstractions from nature in ways nobody had really done before. The way I created my figurative works, I created an innovative oeuvre which blurred the lines between reality and sheer abstraction.','I’m pretty sure I didn’t because I got fame, support, and moolah, so there wasn’t really any struggle for me. Who said no pain, no gain was true?','I don’t know… being dead for almost 50 years takes a toll on this old noggin, eh?
','When I moved to France, I was greatly inspired by the paintings of Andre Derain, Edouard Vuillard, and Pierre Bonnard, and how they created the sense of space. After I married my wife Elsie, we moved to New Jersey, and no, I do not have the accent. Jersey was actually where a lot of my art was inspired from, and that’s where I lived till I died.','I started my formal artistic training at the Maryland Institution of Art, but I thought I was too good for the classes there so I moved to Paris in 1924 to study art at the Académie Modern with Moise Kisling and André Lhote, a cubist academician. After France, I went back to the US and drew inspiration from New Jersey. My paintings became very popular, and in 1965 I received a grant, which is code for moolah, from American Academy of Arts and Letters and then was inducted into the Academy the following year. Moral of the story is, make watery blobs of color and get famous!','I won a good amount of awards and competitions, like the Watson Blair Prize in 1957, Temple Gold Medal in 1960, First Prize at the 27th Biennial, the Corcoran Gallery of Art in 1961, and the National Institute of Arts and Letters in 1967 just to name the important ones.
']
answereubie=[]
answerphillip=[]
helplist=['To start an interview, type “Hello” followed by the name of the person you wish talk to.','To end an interview, type “Goodbye”','Note: The case does not matter, so you don’t have to capitalize or lowercase your inputs']

def interview():
	def goodbye():
                renew=input("If you want to interview another person, then input 'restart'. If you want to exit, input 'exit'.")
                if renew=='restart':
                        interview()
                elif renew=="exit":
                        quit()
                else:
                        print("Wot you tryna say m8")
	def questions():
                for e in q:
                        print(e)
	def menu(letter):
		if letter=="g":#general questions
			questions()
		elif letter=='h':#help
			
		for hel in helplist:
			print(hel)
	else:
		print("I do not know the answer to that question")
    def toni():            #TONIIIIIIIIIII
        print("It Works")
        question=input("What do you wish to ask?")
        if question in gquestions:
                        qnum=gquestions.index(question)
                        answer=answertoni[qnum]
                        for letter in answer:
                                print(letter, end=""),
                                time.sleep(0.5)
        elif question=='goodbye':
                goodbye()
        else:
                menu(question)
    def lee():#LEEEEEEEEEEEEEEEEEE
        print("It Works")
        question=input("What do you wish to ask?")
        if question in gquestions:
                qnum=qquestions.index(question)
                print(answerlist[qnum])
        elif question=='goodbye':
                goodbye()	
        else:
                menu(question)
    def phillip():#PHILLIPPPP
        print("It Works")
        question=input("What do you wish to ask?")
        if question in gquestions:
                qnum=qquestions.index(question)
                print(answerlist[qnum])
        elif question=='goodbye':
                goodbye()	
        else:
                menu(question)
    def eubie():#EUBIEEEEEEEEE
        print("It Works")
        question=input("What do you wish to ask?")
        if question in gquestions:
                qnum=qquestions.index(question)
                print(answerlist[qnum])
        elif question=='goodbye':
                goodbye()	
        else:
                menu(question)
        
        def famouslist():
                for e in personlist:
                        print(e)
        def goodbye():
                renew=input("If you want to interview another person, then input 'restart'. If you want to exit, input 'exit'.")
                if renew=='restart':
                        interview()
                elif renew=="exit":
                        quit()
                else:
                        print("What you tryna say m8")
    name=input("What is your name?-")
    print("Hello "+name+''', and congratulations! You've been given the opportunity to interview four famous artists; Toni Braxton,
    Lee Gatch, Philip Glass, and Eubie Blake. To start the interview with them, just say "Hello _____". To see the list of people you can 
    interview again, input f, to see the list of questions you can ask, input q, and to see a list of specialized questions that vary per
    artist, input s. When you want to end the interview, just say "Goodbye _____", and you will be given the option to either interview 
    another person, or exit."''')
    famous=input()
    if famous=='Hello Toni':
                toni()
    elif famous=='Hello Lee':
                lee()
    elif famous=="Hello Phillip":
                phillip()
    elif famous=="Hello Eubie":
                eubie()
    elif famous=='f':
                famouslist()
    elif famous=='q':
                questions()
    else:
	    print("Please return valid input")
	    interview()
		
interview()		
	
		
