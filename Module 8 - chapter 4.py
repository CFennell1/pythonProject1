import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
#
# survey_data=pd.read_csv("young-people-survey-responses.csv")
#
# # Set the style to "whitegrid"
# sns.set_style="whitegrid"
#
# # Create a count plot of survey responses
# category_order = ["Never", "Rarely", "Sometimes",
#                   "Often", "Always"]
#
# sns.catplot(x="Parents' advice",
#             data=survey_data,
#             kind="count",
#             order=category_order)
#
# # Show plot
# plt.show()
#
# #############################
# # Set the context to "paper"
# sns.set_context = "paper"
#
# # Create bar plot
# sns.catplot(x="Number of Siblings", y="Feels Lonely",
#             data=survey_data, kind="bar")
#
# # Show plot
# plt.show()
#
# ######################
# # Set the style to "darkgrid"
# sns.set_style = "darkgrid"
#
# # Set a custom color palette
# sns.set_palette(["#39A7D0","#36ADA4"])
#
# # Create the box plot of age distribution by gender
# sns.catplot(x="Gender", y="Age",
#             data=survey_data, kind="box")
#
# # Show plot
# plt.show()

###########################
mpg=pd.read_csv("mpg.csv")

# Create scatter plot
g = sns.relplot(x="weight",
                y="horsepower",
                data=mpg,
                kind="scatter")

# Identify plot type
type_of_g = type(g)

# Print type
print(type_of_g)

##############################
# Create scatter plot
g = sns.relplot(x="weight",
                y="horsepower",
                data=mpg,
                kind="scatter")

# Add a title "Car Weight vs. Horsepower"
g.fig.suptitle("Car Weight vs. Horsepower")

# Show plot
plt.show()

########################
# mpg_mean=pd.read_csv("mpg.csv")
#
# # Create line plot
# g = sns.lineplot(x="model_year", y="mpg_mean",
#                  data=mpg_mean,
#                  hue="origin")
#
# # Add a title "Average MPG Over Time"
# g.figsuplot("Average MPG Over Time")
#
# # Show plot
# plt.show()

#################
# Create point plot
sns.catplot(x="origin",
            y="acceleration",
            data=mpg,
            kind="point",
            join=False,
            capsize=0.1)

# Rotate x-tick labels

plt.xticks(rotation = 90)
# Show plot
plt.show()