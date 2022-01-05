import matplotlib.pyplot as p
import statistics
Estimates = [1000, 1200, 1520, 1300, 100, 256,
             300, 420, 140, 100, 300, 255, 960, 1200, 400, 600, 200,
             250, 400, 600, 300, 100, 120, 160, 125, 786,
             255, 790, 455, 130, 500, 750, 430, 320, 300,
             125, 100, 400, 600, 1500, 600, 350, 360, 120,
             100, 123, 150, 600, 300, 250]
y = []
Estimates.sort()
l = len(Estimates)
trim_point = int(0.1 * l)
Estimates = Estimates[trim_point:]
Estimates = Estimates[:l-trim_point]
l = len(Estimates)
for i in range(l):
    y.append(5)
p.plot(Estimates, y, 'g--')
p.plot(statistics.mean(Estimates), 5, 'r^')
p.plot(statistics.median(Estimates), [5], 'bs')
p.plot(420, 5, 'yo')
