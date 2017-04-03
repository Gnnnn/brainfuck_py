# coding:utf-8

import os
import sys


def log(*args, **kwargs):
    print("log: ", *args, **kwargs)


class Tape():
    def __init__(self):
        self.position = 0
        self.bflist = [0]

    def next(self):
        self.position += 1
        if self.position == len(self.bflist):
            self.bflist.append(0)

    def last(self):
        self.position -= 1

    def addnum(self):
        self.bflist[self.position] += 1

    def subnum(self):
        self.bflist[self.position] -= 1

    def outputnum(self):
        return self.bflist[self.position]

    def inputnum(self, data):
        # data = input()
        self.bflist[self.position] = ord(data)


def loopdict(filecontent):
    lpdict = {}
    # content = []
    left = -1
    pc = 0
    for char in filecontent:
        if char in ('[', ']', '<', '>', '+', '-', ',', '.'):
            # content.append(char)
            if char == '[':
                left = pc
            elif char == ']':
                lpdict[left] = pc
                lpdict[pc] = left
        pc += 1
    # log(filecontent,lpdict)
    return filecontent, lpdict


def finalloop(filecontent, lpdict):
    tape = Tape()
    pc = 0
    while pc < len(filecontent):
        if filecontent[pc] == '+':
            tape.addnum()
        elif filecontent[pc] == '-':
            tape.subnum()
        elif filecontent[pc] == '>':
            tape.next()
        elif filecontent[pc] == '<':
            tape.last()
        elif filecontent[pc] == '.':
            # os.write(1, chr(tape.outputnum()))
            print(chr(tape.outputnum()), end='')
        elif filecontent[pc] == ',':
            data = input()
            tape.inputnum(data)
        elif filecontent[pc] == '[' and tape.outputnum() == 0:
            pc = lpdict[pc]
        elif filecontent[pc] == ']' and tape.outputnum() != 0:
            pc = lpdict[pc]
        pc += 1
        # log("pc: ",pc,filecontent[pc])
        # log(tape.position,' ',tape.bflist)


def readfiles(file):
    f = open(file, 'r')
    Gnfile = f.read()
    f.close()
    return Gnfile


def test1():
    tape = Tape()
    log(tape.position, tape.bflist)
    tape.backward()
    log(tape.position, tape.bflist)
    tape.addnum()
    log(tape.position, tape.bflist)
    tape.subnum()
    log(tape.position, tape.bflist)
    tape.forward()
    log(tape.position, tape.bflist)
    tape.outputnum(1)
    tape.inputnum(0)
    tape.outputnum(0)
    log(tape.position, tape.bflist)


def test2():
    filename = sys.argv[1]
    Gnfile = readfiles(filename)
    d, f = loopdict(Gnfile)
    log(d, f)


def main():
    filename = sys.argv[1]
    Gnfile = readfiles(filename)
    d, f = loopdict(Gnfile)
    finalloop(d, f)


if __name__ == "__main__":
    main()
