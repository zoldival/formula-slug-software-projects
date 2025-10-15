# Workshop #2, Create a more complex Graph (Doing a Heat Map)
import polars as pl 
import matplotlib.pyplot as plt
import numpy as np

# reads the provided data file into a data frame 
df = pl.read_parquet('software-data/08102025Endurance1_FirstHalf.parquet') # df data frame
df = df.filter(pl.col("VDM_GPS_Latitude") != 0).filter(pl.col("VDM_GPS_Longitude") != 0) # filters out the rows where the latitude and longitude are 0
df = df.select(["VDM_GPS_SPEED", "VDM_GPS_Latitude", "VDM_GPS_Longitude", "ETC_STATUS_RTDS", "ACC_POWER_PACK_VOLTAGE"])  # selects only the focused columns we want 

print(df.columns) # prints the column names which we selected

# convert the polars (pl) colymns to numpy arrays for easier manipulation since matplotlib works better with numpy

Speed = df["VDM_GPS_SPEED"].to_numpy()
Latitude = df["VDM_GPS_Latitude"].to_numpy()
Longitude = df["VDM_GPS_Longitude"].to_numpy()
RTDS = df["ETC_STATUS_RTDS"].to_numpy()
V_Pack = df["ACC_POWER_PACK_VOLTAGE"].to_numpy()

# figure creator similar to workshop 1 

fig = plt.figure() # creates a figure 
ax1 = fig.add_subplot(221) # adds a subplot to the figure
ax2 = fig.add_subplot(222) # adds another subplot to the figure
ax3 = fig.add_subplot(223) # adds another subplot to the figure
ax4 = fig.add_subplot(224) # adds another subplot to the figure

# top-left plot: speed signal (how i had it on workshop 1)

ax1.plot(Speed, label = "Speed") # plots the engine RPM and the data frame comes from the collumn
ax1.plot(RTDS, label = "RTDS") # plots the throttle position and the data frame comes from the collumn
ax1.set_ylabel("Speed (MPH)") # sets the y label for the first subplot
ax1.set_title("Speed and RTDS") # sets the title for the first subplot
ax1.legend() # adds a legend to the first subplot
ax1.grid() # adds a grid to the first subplot
# wow im abusing the word subplot but this is for my own clarity 

# top-right plot: tracks the heatmap colored by speed where the car is fast or slow
sc = ax2.scatter(Longitude, Latitude, c=Speed, cmap='viridis', s=1) # creates a scatter (sc) plot with the longitude and latitude and colors it by speed
cb = fig.colorbar(sc, ax=ax2) # adds a color bar to the scatter plot
cb.set_label('Speed (MPH)') # sets the label for the color bar
ax2.set_xlabel("Longitude") # sets the x label for the second subplot
ax2.set_ylabel("Latitude") # sets the y label for the second subplot
ax2.set_title("Track Map — Speed Heatmap") # sets the title for the heatmap
ax2.grid(alpha=0.3) # adds a grid to the second subplot with some transparency (thats what alpha does)


plt.show()