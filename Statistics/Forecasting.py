'''
This script gives forecast based on former records.
Input:
    1. Former time stamps and corresponding values
    2. Wanted time stamp
Output: Forecasted value corresponding to wanted time stamp
'''

# TODO: insert real time stamps and corresponding values instead of demo data below
x = [-12, -8, -4, 0]
y = [6000, 8000, 10000, 3000]

# TODO: modify wanted time stamp below
wanted_time = int(input("Please enter the time to forecast: "))

# process data
xa = float(0)
ya = float(0)
w1 = float(0)
w2 = float(0)
w3 = float(0)
w4 = float(0)
for i in range(len(x)):
    xa = xa + x[i]
    ya = ya + y[i]
xa = float(xa / len(x))
ya = float(ya / len(x))

r2 = float(0)
afinal = float(0)
bfinal = float(0)
w1final = float(0)
w2final = float(0)
w3final = float(0)
w4final = float(0)

for w1 in range(0, 10):
    for w2 in range(0, 10 - w1):
        if w1 + w2 < 10:
            for w3 in range(0 , 10 - w1 - w2):
                w4 = 10 - w1 - w2 - w3
                wxy = float((w1 * x[0] * y[0] + w2 * x[1] * y[1] + w3 * x[2] * y[2] + w4 * x[3] * y[3]) / 4) / 10
                wxx = float((w1 * x[0] * x[0] + w2 * x[1] * x[1] + w3 * x[2] * x[2] + w4 * x[3] * x[3]) / 4) / 10
                wx = float((w1 * x[0] + w2 * x[1] + w3 * x[2] + w4 * x[3]) / 4) / 10
                wy = float((w1 * y[0] + w2 * y[1] + w3 * y[2] + w4 * y[3]) / 4) / 10
                if int(wxx - wx * wx) != 0:
                    a = float((wxy - wy * wx / 0.25) / float((wxx - wx * wx / 0.25) + 0.001))
                    b = float((wy - a * wx) / 0.25)

                    u1 = float((y[0] - a * x[0] - b) * (y[0] - a * x[0] - b))
                    u2 = float((y[1] - a * x[1] - b) * (y[1] - a * x[1] - b))
                    u3 = float((y[2] - a * x[2] - b) * (y[2] - a * x[2] - b))
                    u4 = float((y[3] - a * x[3] - b) * (y[3] - a * x[3] - b))
                    d1 = float((y[0] - ya) * (y[0] - ya))
                    d2 = float((y[1] - ya) * (y[1] - ya))
                    d3 = float((y[2] - ya) * (y[2] - ya))
                    d4 = float((y[3] - ya) * (y[3] - ya))

                    temp1 = float((w1 * u1 + w2 * u2 + w3  * u3 + w4 * u4) / 10)
                    temp2 = float((w1 * d1 + w2 * d2 + w3 * d3 + w4 * d4) / 10)
                    rtemp = float(1 - temp1 / temp2)
                    if rtemp > r2:
                        r2 = rtemp
                        afinal = a
                        bfinal = b
                        w1final = w1
                        w1fina2 = w2
                        w1fina3 = w3
                        w1fina2 = w4
forecast = float(afinal * wanted_time + bfinal)

# TODO: take output here
if forecast <= 0:
    print("No valid forecast value")
else:
    print("The forecast value is: ", forecast)