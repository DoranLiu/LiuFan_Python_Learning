from random import gauss

def calcEm(height):
    N = len(height)
    gp = 0.5 #girl probability
    bp = 0.5 #boy probability
    gmu,gsigma=min(height),1 #先验:直接取最大和最小值
    bmu,bsigma=min(height),1
    ggamma = range(N)
    bgamma = range(N)
    cur = [gp,bp,gmu,gsigma,bmu,bsigma]
    now = []

    times = 0
    while times < 100:
        i = 0
        for x in  height:
            ggamma[i]=gp*gauss(x,gmu,gsigma)
            bgamma[i]=bp*gauss(x,bmu,bsigma)
            s = ggamma[i]+bgamma[i]
            ggamma[i]/=s
            bgamma[i]/=s
            i +=1

        gn = sum(ggamma)
        gp = float(gn)/float(N)
        bn = sum(bgamma)
        bp = float(bn)/float(N)
        gmu = averageWeight(height,ggamma,gn)
        gsigma = varianceWeight(height,ggamma,gn)
        bmu = averageWeight(height,bgamma,bn)
        bsigma = varianceWeight(height,bgamma,bmu,bn)

        now = [gp,bp,gmu,gsigma,bmu,bsigma]
        if isSame(cur,now):
            break
        cur = now
        print "Times:\t",times
        print "Girl mean/gsigma:\t",gmu,gsigma
        print "boy mean/bsigma:\t",bmu,bsigma
        print "Boy/Girl:\t",bn.gn,bn+gn
        print "\n\n"
        times +=1
    return now
