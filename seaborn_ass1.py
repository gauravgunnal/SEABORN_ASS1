'''Q1'''
'''Seaborn is a versatile Python data visualization library that offers a wide range of plotting functions. Here are five commonly used plots in Seaborn along with their typical use cases:

1. **Scatter Plot (`sns.scatterplot()`)**:
   - **Use**: Scatter plots are used to visualize the relationship between two numeric variables. Each data point is represented as a point on the plot, making it suitable for examining correlations, identifying clusters, or detecting outliers.
   
2. **Histogram (`sns.histplot()`)**:
   - **Use**: Histograms are used to visualize the distribution of a single numeric variable. They display the frequency or density of values within different bins or intervals, helping to identify data patterns, skewness, and central tendency.

3. **Bar Plot (`sns.barplot()`)**:
   - **Use**: Bar plots are used to display and compare categorical data or summary statistics across different categories. They are suitable for showing the relationship between one categorical variable and one numeric variable, such as comparing average values by category.

4. **Box Plot (`sns.boxplot()`)**:
   - **Use**: Box plots are used to visualize the distribution of a numeric variable's summary statistics, including the median, quartiles, and potential outliers. They are helpful for identifying variations and comparing distributions across categories or groups.

5. **Heatmap (`sns.heatmap()`)**:
   - **Use**: Heatmaps are used to display a matrix of data as a grid of colored cells. They are particularly useful for visualizing correlations between variables, creating confusion matrices, and representing data with color-coded intensity values.

These are just a few of the many types of plots you can create using Seaborn. Seaborn also offers additional plot types like violin plots, KDE plots, pair plots, and more, making it a powerful tool for data exploration and visualization across various data types and analysis goals.'''

'''Q2'''
import seaborn as sns
import matplotlib.pyplot as plt

# Load the "fmri" dataset
fmri_data = sns.load_dataset("fmri")

# Create a line plot for different events and regions
sns.set(style="darkgrid")
plt.figure(figsize=(10, 6))

# Customize the plot as needed, including colors and legends
sns.lineplot(data=fmri_data, x="timepoint", y="signal", hue="event", style="region")

# Add labels and a title
plt.xlabel("Timepoint")
plt.ylabel("Signal")
plt.title("FMRI Signal Over Time for Different Events and Regions")

# Show the plot
plt.legend(title="Event", loc="upper right")
plt.show()

'''Q3'''
import seaborn as sns
import matplotlib.pyplot as plt

# Load the "titanic" dataset
titanic_data = sns.load_dataset("titanic")

# Create a figure with two subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

# Create the first box plot for 'pclass' vs. 'age'
sns.boxplot(data=titanic_data, x='pclass', y='age', ax=axes[0])
axes[0].set_title('Box Plot of Age by Passenger Class')
axes[0].set_xlabel('Passenger Class')
axes[0].set_ylabel('Age')

# Create the second box plot for 'pclass' vs. 'fare'
sns.boxplot(data=titanic_data, x='pclass', y='fare', ax=axes[1])
axes[1].set_title('Box Plot of Fare by Passenger Class')
axes[1].set_xlabel('Passenger Class')
axes[1].set_ylabel('Fare')

# Adjust the layout of subplots
plt.tight_layout()

# Show the plots
plt.show()

'''Q4'''
import seaborn as sns
import matplotlib.pyplot as plt

# Load the "diamonds" dataset
diamonds_data = sns.load_dataset("diamonds")

# Create a histogram with hue parameter
plt.figure(figsize=(10, 6))
sns.histplot(data=diamonds_data, x="price", hue="cut", kde=True, palette="Set1")

# Customize the plot
plt.title("Price Distribution by Cut of Diamonds")
plt.xlabel("Price")
plt.ylabel("Count")

# Show the histogram
plt.legend(title="Cut")
plt.show()

'''Q5'''
import seaborn as sns
import matplotlib.pyplot as plt

# Load the "iris" dataset
iris_data = sns.load_dataset("iris")

# Create a pair plot with hue parameter
sns.set(style="ticks")
sns.pairplot(iris_data, hue="species", palette="Set2")

# Show the pair plot
plt.show()

'''Q6'''
import seaborn as sns
import matplotlib.pyplot as plt

# Load the "flights" dataset
flights_data = sns.load_dataset("flights")

# Pivot the dataset to create a matrix suitable for a heatmap
flights_pivot = flights_data.pivot("month", "year", "passengers")

# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(flights_pivot, annot=True, fmt="d", cmap="YlGnBu")

# Customize the plot
plt.title("Passenger Count by Month and Year (1949-1960)")
plt.xlabel("Year")
plt.ylabel("Month")

# Show the heatmap
plt.show()
