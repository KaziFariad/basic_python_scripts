from statistics import mean
Estimates = [1000, 1200, 1520, 1300, 100, 256, 300, 420, 140, 100, 300, 255, 960, 1200, 400, 600, 200, 250, 400, 600, 300, 100, 120,
             160, 125, 786, 255, 790, 455, 130, 500, 750, 430, 320, 300, 125, 100, 400, 600, 1500, 600, 350, 360, 120, 100, 123, 150, 600, 300, 250]
trim_point = int(0.1*len(Estimates))
print(trim_point)
Estimates.sort()
print(Estimates)
Estimates = Estimates[trim_point:]
print(Estimates)
Estimates = Estimates[:len(Estimates)-trim_point]
print(Estimates)
m = mean(Estimates)
print(m)
