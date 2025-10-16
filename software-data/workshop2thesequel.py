# Workshop #2, Create a more complex Graph (Doing a Heat Map)
import polars as pl 
import matplotlib.pyplot as plt

# reads the provided data file into a data frame 
df = pl.read_parquet('software-data/08102025Endurance1_FirstHalf.parquet') # df data frame
df = df.filter(pl.col("VDM_GPS_Latitude") != 0).filter(pl.col("VDM_GPS_Longitude") != 0) # filters out the rows where the latitude and longitude are 0
df = df.select(["VDM_GPS_SPEED", "VDM_GPS_Latitude", "VDM_GPS_Longitude"])  # selects only the focused columns we want 

print(df.columns) # prints the column names which we selected

# convert the polars (pl) columns to numpy arrays for easier manipulation since matplotlib works better with numpy
Speed = df["VDM_GPS_SPEED"]
Latitude = df["VDM_GPS_Latitude"]
Longitude = df["VDM_GPS_Longitude"]

# creates a figure (just one this time!)
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)  # single subplot

# creates a scatter (sc) plot with longitude and latitude and colors it by speed
sc = ax.scatter(Longitude, Latitude, c=Speed, cmap='viridis', s=4, alpha=0.9)  

# adds a color bar for speed
cb = fig.colorbar(sc, ax=ax)
cb.set_label('Speed (MPH)')

# adds axis labels, title, and a light grid
ax.set_xlabel("Longitude") 
ax.set_ylabel("Latitude") 
ax.set_title("Track Map — Speed Heatmap") 
ax.grid(alpha=0.3)

plt.show()  # displays the figure