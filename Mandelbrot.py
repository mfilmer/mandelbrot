

class mandelbrot(object):
    def __init__(self):
        pass
    
    def genImage(self,window,resolution,fileName):
        pass
    
    def genColorImage(self,window,resolution,fileName):
        pass
    
    def checkPoint(self,c,iterations=25,radius=2):
        count = self.getPointCount(c,iterations,radius)
        if count == iterations:
            return True
        else:
            return False
    
    def getPointCount(self,c,iterations=25,radius=2):
        z = 0
        for i in xrange(iterations):
            z = z**2 + c
            if abs(z) >= 2:
                break
        else:
            return iterations
        return i
    
    def __frange(self, start, stop=None, step=1):
        if stop == None:
            stop = start
            start = 0
        i = start
        while True:
            yield i
            i += step
            if i >= stop:
                break
