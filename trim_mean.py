from scipy import stats
e = [1,2,3,4,5,566,123,334,521,12,23,12,4,24,23,12,442,2,31,2,322]
M = stats.trim_mean(e,0.1)
print(M)