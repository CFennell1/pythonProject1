# # Change to use relplot() instead of scatterplot()
# sns.relplot(x="absences", y="G3",
#                 data=student_data)
#
#
# # Show plot
# plt.show()
#
# #############################
# # Change to make subplots based on study time
# sns.relplot(x="absences", y="G3",
#             data=student_data,
#             kind="scatter", col="study_time")
#
# # Show plot
# plt.show()
#
# #################################
# # Change this scatter plot to arrange the plots in rows instead of columns
# sns.relplot(x="absences", y="G3",
#             data=student_data,
#             kind="scatter",
#             row="study_time")
#
# # Show plot
# plt.show()
#
# ###################################
# ## Create a scatter plot of G1 vs. G3
# sns.relplot(x="G1", y ="G3", data =student_data, kind = "scatter")
#
#
#
# # Show plot
# plt.show()
#
#
# ####################################
#
# # Adjust to add subplots based on school support
# sns.relplot(x="G1", y="G3",
#             data=student_data,
#             kind="scatter",col="schoolsup", col_order=["yes","no"])
#
# # Show plot
# plt.show()
#
# ###################################
# # Adjust further to add subplots based on family support
# sns.relplot(x="G1", y="G3",
#             data=student_data,
#             kind="scatter",
#             col="schoolsup",
#             col_order=["yes", "no"],row="famsup", row_order=["yes","no"])
#
# # Show plot
# plt.show()
#############################

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

mpg=pd.read_csv("mpg.csv")
# Create scatter plot of horsepower vs. mpg
sns.relplot(kind="scatter", x ="horsepower", data=mpg, y="mpg", size ="cylinders",hue="cylinders")



# Show plot
plt.show()

#################################
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of acceleration vs. mpg
sns.relplot(data=mpg, x="acceleration", y ="mpg",hue="origin", style = "origin",kind="scatter")



# Show plot
plt.show()

#############################
###look here
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot
sns.relplot(kind="line", data=mpg,x="model_year", y = "mpg")


# Show plot
plt.show()

################
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot
sns.relplot(kind="line", data=mpg,x="model_year", y = "mpg")


# Show plot
plt.show()

###########################
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot of model year vs. horsepower
sns.relplot(x="model_year", y="horsepower", data = mpg, kind = "line", ci=None)



# Show plot
plt.show()