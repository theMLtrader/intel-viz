import pandas as pd
import matplotlib.pyplot as plt
print # for formatting in ipython only

##ALL THIS WAS DOING IT THE HARD WAY> I CAN USE GROUPBY.SIZE()
metadata = pd.read_csv('metaDB-csv-3-7/meta-3-7.csv')

headers = [header for header in metadata]
df = pd.DataFrame(metadata)

for i in headers:
    print i + " count:"
    print len(df[i].value_counts(normalize=True))
    
print headers    
# various groupby toyings
region_branch = df.groupby(['businessunit','facility']).size()
print "regional branches breakdown"
print region_branch

facility_machine = df.groupby(['facility','machinefunction']).size()
print facility_machine
#facility_machine.to_csv('facility_machine.csv')
#fac_df = pd.DataFrame(facility_machine)
facility_machine.to_csv('facility_machine.csv')

facility_locations = df.groupby(['facility','latitude','longitude']).size()
print "fac locs"
print facility_locations

lat_long = df.groupby(['latitude','longitude'])

#plot lat long on scatter
#this is ugly, there must be a panda function to sort by unique values across 2 cols.
plt.scatter(df['latitude'].unique(), df['longitude'].unique())
plt.show()

#count returns the number of not null records in each column
#this is not particularly useful right now...
#facility_count = df.groupby('facility').count()
#print facility_count

## #unique business units
## facility = df['facility'].unique()

## new_df = pd.DataFrame()
## for f in facility:
##     office = df[df['facility']==f].sort()
##     officetotals = office['machineclass'].value_counts()
##     new_df[f] = officetotals
## tran = new_df.T
## topserver = tran.sort(['server'], ascending=False)
## topserver.head().plot()
## topworkstation = tran.sort(['workstation'], ascending=False)
## topworkstation.head().plot()

## plt.show()

## # latitude longitudes
## # Can put them into scatter plot as a proxy for geo location
## lats = df['latitude'].unique()
## for l in lats:
##     lat_count = df[df['latitude']==l].sort()
##     lat_total = lat_count['


