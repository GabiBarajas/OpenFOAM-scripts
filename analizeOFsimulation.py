#barajasg@unican.es
#24/Feb/2017

import pylab
import numpy as np 

#Time
def f3(V):
    # Plot:
    pylab.figure(3, figsize=(16,9))

    X = range(len(V["Time"]))
    pylab.plot(X, V["Time"], label="Time",linewidth=3)

    #sum all deltaT
    Xacc = range(0, len(V["deltaT"]), 30)
    acc = [ sum(V["deltaT"][:i]) for i in Xacc ]
    pylab.plot(Xacc, acc, "o", label="sum(deltaT)" )

    pylab.xlabel(" Iteraciones")
    pylab.ylabel(" t (s)")
    pylab.title(" ihFOAM Time ")
    pylab.legend(bbox_to_anchor=(0.10, 1), loc=2, borderaxespad=1.5)
    pylab.draw()

    cadena = fn+'.figure3.png'
    pylab.savefig(cadena)


#ExecutionTime & ClockTime
def f1(V):
    # Plot:
    pylab.figure(1, figsize=(16,9))

    X = range(len(V["ExecutionTime"]))
    pylab.plot(X, V["ExecutionTime"], label="ExecutionTime")

    X = range(len(V["ClockTime"]))
    pylab.plot(X, V["ClockTime"], label="ClockTime")

    pylab.xlabel(" Iteraciones")
    pylab.ylabel(" t (s)")
    pylab.title(" ihFOAM ExecutionTime & ClockTime ")
    pylab.legend(bbox_to_anchor=(0.10, 1), loc=2, borderaxespad=1.5)
    pylab.draw()

    cadena = fn+'.figure1.png'
    pylab.savefig(cadena)


#deltaT
def f2(V):
    # Plot:
    pylab.figure(2, figsize=(16,9))

    X = range(len(V["deltaT"]))
    pylab.plot(X, V["deltaT"], label="deltaT")

    amin = min(V["deltaT"])
    amax = max(V["deltaT"])
    pylab.ylim([amin-0.1*amin,amax+0.1*amax])
    pylab.xlabel(" Iteraciones")
    pylab.ylabel(" t (s)")
    pylab.title(" ihFOAM deltaT ")
    pylab.legend(bbox_to_anchor=(0.10, 1), loc=2, borderaxespad=1.5)
    pylab.draw()

    cadena = fn+'.figure2.png'
    pylab.savefig(cadena)


#LoopTime
def f4(V):
    # Plot:
    pylab.figure(4, figsize=(16,9))

    X = range(len(V["LoopTime"]))
    pylab.plot(X, V["LoopTime"], label="LoopTime")

    amin = min(V["LoopTime"])
    amax = max(V["LoopTime"])
    amean = np.mean(V["LoopTime"])
    Xmean=[min(X), max(X)]
    Ymean=[amean, amean]
    pylab.plot(Xmean, Ymean, label=" mean LoopTime",linewidth=3)

    Ymax=[amax, amax]
    pylab.plot(Xmean, Ymax, label=" max LoopTime",linewidth=3)

    Ymin=[amin, amin]
    pylab.plot(Xmean, Ymin, label=" min LoopTime",linewidth=3)

    pylab.ylim([amin-0.2*amin,amax+0.2*amax])

    pylab.ylabel(" t (s)")
    pylab.xlabel("Iteraciones")
    pylab.title(" ihFOAM LoopTime ")
    pylab.legend(bbox_to_anchor=(0.10, 1), loc=2, borderaxespad=1.5)
    pylab.draw()

    cadena = fn+'.figure4.png'
    pylab.savefig(cadena)


#PATH:
fn = "/home/gabi/slurm-679071.out"

V = {
    "Time": [],
    "deltaT": [],
    "ExecutionTime": [],
    "ClockTime": [],
    "LoopTime": [],
}

# Read .out data:
with open(fn) as f:
    for line in f:
        try:
            if line[:7] == "Time = ":
                _, _, t = line.split()
                V["Time"].append(float(t))
            if line[:9] == "deltaT = ":
                _, _, dt = line.split()
                V["deltaT"].append(float(dt))
            if line[:16] == "ExecutionTime = ":
                _, _, et, _, _, _, ct, _ = line.split()
                V["ExecutionTime"].append(float(et))
                V["ClockTime"].append(float(ct))
            if line[:11] == "LoopTime = ":
                _, _, lt, = line.split()
                V["LoopTime"].append(float(lt))
        except:
            pass

# Plot data:
f1(V) #plot ExecutionTime & ClockTime
f2(V) #plot deltaT
f3(V) #plot Time
f4(V) #plot LoopTime
pylab.show()

