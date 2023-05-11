def problem01():
    def f(n):
        return 3*n+2
        
    def g(n):	
        return n
            
    c = 5
    n0 = 10

    return f, g, c, n0


def problem02():
    def f(n):
        return 2*n**2+3*n+2
        
    def g(n):	
        return n**2
          
    c = 3
    n0 = 1

    return f, g, c, n0


def problem03():
    def f(n):
        return 2*n**3+3*n**2+3*n+3
        
    def g(n):	
        return n**3
            
    c = 10
    n0 = 5

    return f, g, c, n0


def problem04():
    def f(n):
        return 4*n+5
        
    def g(n):	
        return n
            
    c = 5
    n0 = 1

    return f, g, c, n0


def problem05():
    def f(n):
        return 3*2**n+3*n-1
        
    def g(n):	
        return 2**n
            
    c = 5
    n0 = 2

    return f, g, c, n0