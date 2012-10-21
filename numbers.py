#!/usr/bin/env python
import random

def evaluate(code, guess):
    feedback = []
    codecp = [x for x in code]
    for i in xrange(len(guess)):
        if guess[i] ==  codecp[i]:
            feedback.append("1")
            guess[i] = "."
            codecp[i] = ","
    for i in xrange(len(guess)):
        if guess[i] in codecp:
            feedback.append("0")
            codecp[i] = ","
    feedback.sort()
    return "".join(feedback) 
            
def main():
    correct = False
    code = []
    for i in xrange(6):
        code.append(str(random.randint(1,6)))
    print """Guess the code. It contains the numbers 1-6 and is 6 numbers long. For each number you guess correctly, you'll get a "1" if it's in the correct position, and a "0" if it isn't."""
    while not correct:
        guess = list(raw_input(">> "))
        if len(guess) != len(code):
            print "Your guess needs to be %s numbers long" % len(code)
            continue
        feedback = evaluate(code, guess)
        if feedback == "111111":
            correct = True
        else:
            print feedback
    print "Well, I guess you found out that the code is %s." % "".join(code)

if __name__ == "__main__":
    main()
