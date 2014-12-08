#Logic gate python programming exercise from interactivepython.org

class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self,n)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Pin A (%s) -->"%self.getLabel()))
        else:
            return self.pinA.getFrom().getOutput()
            
    def getPinB(self):
        if self.pinB == None:
            return int(input("Pin B (%s) -->"%self.getLabel()))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        elif self.pinB == None:
            self.pinB = source
        else:
            print "Cannot Connect: No Empty Pins"

class UnaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self,n)
        self.pin = None
    
    def getPin(self):
        if self.pin == None:
            return int(input("Pin (%s) -->"%self.getLabel()))
        else:
            return self.pin.getFrom().getOutput()
    
    def setNextPin(self, source):
        if self.pin== None:
            self.pin = source
        else:
            print "Cannot Connect: No Empty Pins"

class AndGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class NandGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 0
        else:
            return 1

class NorGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self,n)
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 0 and b == 0:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 0 and b == 0:
            return 0
        else:
            return 1

class NotGate(UnaryGate):
    def __init__(self, n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPin()
        if a == 1:
            return 0
        else:
            return 1

class XorGate(BinaryGate):
    def __init__(self, n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if (a == 1 and b == 0) or (a == 0 and b == 1):
            return 1
        else:
            return 0

class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate
        
    def getTo(self):
        return self.togate

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        elif self.pinB == None:
            self.pinB = source
        else:
            raise RuntimeError("Error: No Empty Pins!")


def main():
    g1 = AndGate("g1")
    g2 = AndGate("g2")
    g3 = OrGate("g3")
    g4 = NotGate("g4")

    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print g4.getOutput()

    g5 = NandGate("g5")
    g6 = NandGate("g6")
    g7 = AndGate("g7")

    c4 = Connector(g5, g7)
    c5 = Connector(g6, g7)
    print g7.getOutput()

main()
