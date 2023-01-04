import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')

  # Create scatter plot
  y = df['CSIRO Adjusted Sea Level']
  x = df['Year']
  fig, ax = plt.subplots()
  plt.scatter(x, y)

  # Create first line of best fit
  result = linregress(x, y)
  print(result)
  x_pred = pd.Series([i for i in range(1880, 2050)])
  y_pred = result.slope * x_pred + result.intercept
  plt.plot(x_pred, y_pred, 'r')

  # Create second line of best fit
  new_df = df.loc[df['Year'] >= 2000]
  new_x = new_df['Year']
  new_y = new_df['CSIRO Adjusted Sea Level']
  result_2 = linregress(new_x, new_y)
  x_pred2 = pd.Series([i for i in range(2000, 2050)])
  y_pred2 = result_2.slope * x_pred2 + result_2.intercept
  plt.plot(x_pred2, y_pred2, 'r')
  # Add labels and title
  ax.set_xlabel('Year')
  ax.set_ylabel('Sea level indicator')
  ax.set_title('Rise in Sea Level')

  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
