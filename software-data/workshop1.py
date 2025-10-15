# Workshop 1: Data Manipulation with Polars and visualization
import polars as pl 
import matplotlib.pyplot as plt

df = pl.read_parquet('software-data/08102025Endurance1_FirstHalf.parquet') # df data frame
df = df.filter(pl.col("VDM_GPS_Latitude") != 0).filter(pl.col("VDM_GPS_Longitude") != 0) # filters out the rows where the latitude and longitude are 0
df = df.select(["VDM_GPS_SPEED", "VDM_GPS_Latitude", "VDM_GPS_Longitude", "ETC_STATUS_RTDS", "ACC_POWER_PACK_VOLTAGE"]) # selects only the columns we want  

print(df.columns) # prints the column names WOW!

fig = plt.figure() # creates a figure 
ax1 = fig.add_subplot(221) # adds a subplot to the figure
ax2 = fig.add_subplot(222) # adds another subplot to the figure
ax3 = fig.add_subplot(223) # adds another subplot to the figure
ax4 = fig.add_subplot(224) # adds another subplot to the figure

ax1.plot(df["VDM_GPS_SPEED"], label = "Speed") # plots the engine RPM and the data frame comes from the collumn
ax1.plot(df["ETC_STATUS_RTDS"], label = "RTDS") # plots the throttle position and the data frame comes from the collumn
ax1.set_ylabel("Speed (MPH)") # sets the y label for the first subplot
ax1.legend()
# ax1.legend(("Speed", "RTDS"))

ax2.plot(df["VDM_GPS_Latitude"], df["VDM_GPS_Longitude"]) # plots the latitude and longitude and the data frame comes from the collumn

ax3.plot(df["ETC_STATUS_RTDS"]) # plots the throttle position and the data frame comes from the collumn

ax4.plot(df["ACC_POWER_PACK_VOLTAGE"]) # plots the battery voltage and the data frame comes from the collumn

plt.show() # shows the figure with all the subplots 