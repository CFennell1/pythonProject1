import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

survey_data=pd.read_csv("young-people-survey-responses.csv")

# Create count plot of internet usage
sns.catplot(kind="count", x="Internet usage", data=survey_data)


# Show plot
plt.show()

##########################
# Create a bar plot of interest in math, separated by gender

sns.catplot(data=survey_data, kind="bar", x="Gender", y ="Mathematics")


# Show plot
plt.show()

##########################
student_data=pd.read_csv("student-alcohol-consumption.csv")

# Create bar plot of average final grade in each study category

sns.catplot(data=student_data, kind="bar", x="study_time", y="G3")


# Show plot
plt.show()

###########################
# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours",
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories

sns.catplot(data=student_data,kind="box", x="study_time", y = "G3", order = study_time_order)

############################
# Create a box plot with subgroups and omit the outliers

sns.catplot(data=student_data,kind="box", x="internet", y="G3", hue="location", sym="")




# Show plot
plt.show()

#####################
# Set the whiskers to 0.5 * IQR
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box", whis=0.5)

# Show plot
plt.show()

#########################
# Create a point plot of family relationship vs. absences

sns.catplot(kind="point", data=student_data, x="famrel", y="absences")

# Show plot
plt.show()

##########################
# Create a point plot with subgroups

sns.catplot(data = student_data, kind="point", x = "romantic", y = "absences", hue="school")


# Show plot
plt.show()