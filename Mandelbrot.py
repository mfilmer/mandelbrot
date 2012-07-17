from __future__ import division
import Image
import datetime
#http://code.google.com/p/mpmath/

FILENAME = 'mandelbrot' + str(datetime.datetime.now()) + '.png'
FILENAME = FILENAME.replace(' ','_')
FILENAME = FILENAME.replace(':','.')

class mandelbrot(object):
    def __init__(self):
        pass
    
    def genImage(self,(l,t,w,h),res,fileName=FILENAME,mode='Gray'):
        if not mode in ['Binary','Gray','Color']:
            error('invalid mode')
        setImage = Image.new('RGB',(int(w*res),int(h*res)))
        setAccess = setImage.load()
        #complex numbers represented as a + bj
        for a in self.__frange(l,l+w,1/res):        #real part
            for b in self.__frange(t,t-h,-1/res):    #imag part
                val = self.getPointCount(complex(a,b))
                loc = self.__locToPix((l,t,w,h),res,(a,b))
                if mode == 'Binary':
                    if val == 26:
                        loc = tuple(map(int,loc))
                        setAccess[loc] = (0,)*3
                    else:
                        setAccess[loc] = (255,)*3
                elif mode == 'Gray' or mode == 'Color':
                    setAccess[loc] = ((256-val),)*3
                    if mode == 'Color':
                        #colorize the gray image
                        pass
        setImage.save(fileName,'PNG')
    
    def checkPoint(self,c,iterations=26,radius=2):
        count = self.getPointCount(c,iterations,radius)
        if count == iterations:
            return True
        else:
            return False
    
    def getPointCount(self,c,iterations=256,radius=2):
        z = 0
        for i in xrange(iterations):
            z = z**2 + c
            if abs(z) >= 2:
                break
        else:
            return iterations
        return i
    
    def __locToPix(self,(l,t,w,h),res,(x,y)):
        return ((x-l)*res,-(y-t)*res)
    
    def __frange(self,start,stop=None,step=1):
        if step == 0:
            error('step cannot be 0')
        if stop is None:
            stop = start
            start = 0
        count = int((stop - start)/step)
        a = start
        for i in xrange(count):
            yield a
            a += step
