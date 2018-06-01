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

#PATH:
fn = "PATH_TO_DATA/slurm-676069.out"

V = {
    "Time": [],
    "deltaT": [],
    "ExecutionTime": [],
    "ClockTime": [],
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
        except:
            pass

# Plot data:
f1(V) #plot ExecutionTime & ClockTime
f2(V) #plot deltaT
f3(V) #plot Time
pylab.show()

