import pandas as pd
import matplotlib.pyplot as plt
print # for formatting in ipython only

# THIS ONLY LOOKS AT DATAFRACTION.CSV which is a data subset
data = pd.read_csv('metaDB-csv-3-7/datafraction.csv')

headers = [header for header in data]
df = pd.DataFrame(data)

for i in headers:
    print i + " count:"
    print len(df[i].value_counts(normalize=True))

print df['numconnections']

# statistical measures
print 'max connections'
print df['numconnections'].max()
print 'average connections'
print df['numconnections'].mean()
print 'std dev'
print df['numconnections'].std()

# look at the df broken down by machine.
# then see the variance of numconnections, policy status
## uniqueip = df['ipaddr'].unique()
## for ip in uniqueip:
##     print ip
##     print df[df['ipaddr']==ip]['numconnections'].var()

# proportion of machines with policy status 5
policy_status = df['policystatus'].value_counts()
policy_status.plot(kind='bar')
plt.title('policy status counts')
plt.savefig('output_chart/proportion_status.png')

# occuring times for policy statuses
policy_stat = pd.DataFrame()
for i in df['policystatus'].unique():
    status = df[df['policystatus']==i]['healthtime'].value_counts()
    policy_stat[i] = status
policy_stat.plot()
plt.title('live policy status')
plt.savefig('output_chart/policystatuscomparo.png')

#policy status 5
## policy_status_time = df[df['policystatus']==5]['healthtime'].value_counts()
## policy_status_time.plot()
## plt.title('times for status 5')
## plt.savefig('output_chart/status5.png')

#machines with highest status 5 counts
is_status_5 = df['policystatus']==5
machine_status_5 = df[is_status_5]
machine_status_5['ipaddr'].value_counts()
print machine_status_5

#proportion flags
flag_counts = df['activityflag'].value_counts()
flag_counts.plot(kind='bar')
plt.title('activityflag proportions')
plt.savefig('output_chart/proportion_flag')

#activity flag breakdown
flag_stat = pd.DataFrame()
for i in df['activityflag'].unique():
    status = df[df['activityflag']==i]['healthtime'].value_counts()
    flag_stat[i] = status
#leaving out flag one as it drowns out the others
flag_stat[[2,3,4,5]].plot()
plt.title('live activity flag status')
plt.savefig('output_chart/flagstatuscomparo.png')


############# TODOs #############

#machines with highest connections
#max_connect = df['numconnections'].max()

#per machine statistics - mean, std dev. flag if usage falls outside of past usage history.
## mach_conn = pd.DataFrame()
## for i in df['ipaddr'].unique():
##     machine_stats = df[df['ipaddr']==i]['numconnections'].value_counts()

#machine_connect = df.groupby(['ipaddr','numconnections']).size()

#machines with highest variability in connections

#is there a correlation between connections amongst machines
