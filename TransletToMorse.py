import time
import RPi.GPIO as gpio

red = 3 
def init():
#    gpio.setwarnings(False)
    gpio.setmode(gpio.BOARD)
    gpio.setup(red,gpio.OUT)
    gpio.output(red,gpio.LOW)
def poit():
    gpio.output(red,gpio.HIGH)
    time.sleep(0.5)
    gpio.output(red,gpio.LOW)
    time.sleep(0.5)
def dash():
    gpio.output(red,gpio.HIGH)
    time.sleep(1.5)
    gpio.output(red,gpio.LOW)
    time.sleep(0.5)
    
def caseA():
    poit()
    dash()
def caseB():
    dash()
    poit()
    poit()
    poit()
def caseC():
    dash()
    poit()
    dash()
    poit()
def caseD():
    dash()
    poit()
    poit()
def caseE():
    poit()
def caseF():
    poit()
    poit()
    dash()
    poit()
def caseG():
    dash()
    dash()
    poit()
def caseH():
    poit()
    poit()
    poit()
    poit()
def caseI():
    poit()
    poit()
def caseJ():
    poit()
    dash()
    dash()
    dash() 
def caseK():
    dash()
    poit()
    dash()
def caseL():
    poit()
    dash()
    poit()
    poit()
def caseM():
    dash()
    dash()
def caseN():
    dash()
    poit()
def caseO():
    dash()
    dash()
    dash()
def caseP():
    poit()
    dash()
    dash()
    poit()
def caseQ():
    dash()
    dash()
    poit()
    dash()
def caseR():
    poit()
    dash()
    poit()
def caseS():
    poit()
    poit()
    poit()
def caseT():
    dash()
def caseU():
    poit()
    poit()
    dash()
def caseV():
    poit()
    poit()
    dash()
def caseW():
    poit()
    dash()
    dash()
def caseX():
    dash()
    poit()
    poit()
    dash()
def caseY():
    dash()
    poit()
    dash()
    dash()
def caseZ():
    dash()
    dash()
    poit()
    poit()
def case1():
    poit()
    dash()
    dash()
    dash()
    dash()
def case2():
    poit()
    poit()
    dash()
    dash()
    dash()
def case3():
    poit()
    poit()
    poit()
    dash()
    dash()
def case4():
    poit()
    poit()
    poit()
    poit()
    dash()
def case5():
    poit()
    poit()
    poit()
    poit()
    poit()
def case6():
    dash()
    poit()
    poit()
    poit()
    poit()
def case7():
    dash()
    dash()
    poit()
    poit()
    poit()
def case8():
    dash()
    dash()
    dash()
    poit()
    poit()
def case9():
    dash()
    dash()
    dash()
    dash()
    poit()
def case0():
    dash()
    dash()
    dash()
    dash()
    dash()

switch={
    'A' : caseA,
    'B' : caseB,
    'C' : caseC,
    'D' : caseD,    
    'E' : caseE,    
    'F' : caseF,    
    'G' : caseG,    
    'H' : caseH,    
    'I' : caseI,    
    'G' : caseG,    
    'K' : caseK,    
    'L' : caseL,    
    'M' : caseM,    
    'N' : caseN,    
    'O' : caseO,    
    'P' : caseP,    
    'Q' : caseQ,    
    'R' : caseR,    
    'S' : caseS,    
    'T' : caseT,    
    'U' : caseU,    
    'V' : caseV,    
    'W' : caseW,    
    'X' : caseX,    
    'Y' : caseY,    
    'Z' : caseZ,
    'a' : caseA,
    'b' : caseB,
    'c' : caseC,
    'd' : caseD,    
    'e' : caseE,    
    'f' : caseF,    
    'g' : caseG,    
    'h' : caseH,    
    'i' : caseI,    
    'g' : caseG,    
    'k' : caseK,    
    'l' : caseL,    
    'm' : caseM,    
    'n' : caseN,    
    'o' : caseO,    
    'p' : caseP,    
    'q' : caseQ,    
    'r' : caseR,    
    's' : caseS,    
    't' : caseT,    
    'u' : caseU,    
    'v' : caseV,    
    'w' : caseW,    
    'x' : caseX,    
    'y' : caseY,    
    'z' : caseZ,
    '0' : case0,    
    '1' : case1,
    '2' : case2,    
    '3' : case3,    
    '4' : case4,    
    '5' : case5,    
    '6' : case6,    
    '7' : case7,
    '8' : case8,    
    '9' : case9
    }

    
def translate(str):
    for s in str:
        switch[s]()
            
    
def main():
    init()
    string = raw_input('Enter your original worlds: ')
    translate(string)
    gpio.cleanup()

if __name__ == "__main__":
    main()
    
