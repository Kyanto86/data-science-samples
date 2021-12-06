import numpy as np
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest, proportion_confint

# get data
df = pd.read_csv(FILE_PATH)

#group into control and test group (here by group) and print interesting values
print(df.groupby('group', as_index=False).agg(['sum','count', 'mean', 'std']))

#Now get the number of conversions per group from the converted column. It's 1 for converted and 0 if not.
clicks_cont = df[df['group'] == 'A']['converted']
clicks_test = df[df['group'] == 'B']['converted']

#get ns and conversion sums
n_cont = clicks_cont.count()
n_test = clicks_test.count()
conversions = [clicks_cont.sum(), clicks_test.sum()]
nobs = [n_cont, n_test]

##do the z-test, get p and cis
z_stat, p = proportions_ztest(conversions, nobs = nobs)
(lower_con, lower_test), (upper_con, upper_test) = proportion_confint(conversions, nobs=nobs, alpha=0.05)
cont_ci = [lower_con, upper_con]
test_ci = [lower_test, upper_test]

print(proportion_confint(conversions, nobs=nobs, alpha=0.05))

print(cont_ci)
print(test_ci)

print("p-value: " + str(p))

if p < 0.05:
    print("H0 REJECTED: The two samples are different!")
else:
    print("H0 NOT REJECTED: The two samples don't appear different!")