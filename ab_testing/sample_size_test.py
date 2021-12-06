# Packages imports
import statsmodels.stats.api as sms
from math import ceil

CURRENT_CONV_RATE = 0.30
TARGET_CONV_RATE = 0.35
POWER = 0.8
CI = 0.95
ALPHA = 1 - CI

# Calculating effect size / lift based on our expected rates
effect_size = sms.proportion_effectsize(CURRENT_CONV_RATE, TARGET_CONV_RATE)    

# Calculating sample size needed
required_n = sms.NormalIndPower().solve_power(
    effect_size, 
    power=POWER, 
    alpha=ALPHA, 
    ratio=1
    )       
                                           
# Rounding up to next whole number
required_n = ceil(required_n)                                                   

print("Required sample size:" + str(required_n))