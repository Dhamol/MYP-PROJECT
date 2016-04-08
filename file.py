# MYP-PROJECT
personlist=['Toni Braxton','Lee Glath','Phillip Glass','Eubie Blake']
gquestions=["Helo"]
answertoni=['yaaaaaaas']
answerlee=[]
answereubie=[]
answerphillip=[]
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
		sdfsd
	elif letter=='h':#help
		helplist=['To start an interview, type “Hello” followed by the name of the person you wish talk to.','To end an interview, type “Goodbye”','Note: The case does not matter, so you don’t have to capitalize or lowercase your inputs']
		for hel in helplist:
			print(hel)
	else:
		print("I do not know the answer to that question")
def special():
	gsgsg
def interview():
    def toni():            #TONIIIIIIIIIII
        print("It Works")
        question=input("What do you wish to ask?")
        if question in gquestions:
                        qnum=qquestions.index(question)
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
	
		
