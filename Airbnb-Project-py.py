#!/usr/bin/env python
# coding: utf-8

# # Project Final Submission Template

# ### Step 1a: Planning 
# #### Identify the information in the file your program will read
# 
# Describe (all) the information that is available. Be sure to note any surprising or unusual features. (For example, some information sources have missing data, which may be blank or flagged using values like -99, NaN, or something else.)

# <font color="blue">
#     
# The airbnb subset contains the following information:
#     
#     host_id (represents the id of the host) 
#     
#     host_name (The name of the host) 
#     
#     host_since_year (since what year has the host being in Airbnb) (This is in range [2007, ...]) ( Not that the dataset is form: [2008, 2015])
#     
#     host_since_anniversary (Since which anniversary has the host been hosting)
#     (note that this is a date of the form yyyy-mm-dd)
#     
#     id (The id of the host) 
#     
#     neighbourhood_cleansed
#     city (The city of the unit) 
#     
#     state (state of the unit) 
#     
#     zipcode (zipcode of the unit) 
#     (note that there are some empty as well as some with letters at the end of the zipcode number 
#     
#     country (country of the unit) 
#     
#     latitude (latitude of of the unit) 
#     
#     longitude (longitude of the unit) 
#     
#     property_type (property type) 
#     (note that this is a pre defined type, such as apartment, loft, house, boat...) 
#     
#     room_type (room type) (note that this is a pre defined type, Entire home/apt or Private room) 
#     
#     accommodates (number of accomodates) 
#     
#     bathrooms (number of bathrooms of the unit)
#     
#     bedrooms (number of bathrooms of the unit) 
#     
#     beds (number of beds of the unit) 
#     
#     bed_type (number of bed_type of the unit)
#     
#     price (price of the unit)
#     
#     guests_included	(number of guests_included of the unit)
#     
#     extra_people	(number of extra_people of the unit)
#     
#     minimum_nights	(number of minimum_nights of the unit)
#     
#     host_response_time	 ( Note that this can be N/A )
#     
#     host_response_rate	( Note that this can be N/A )
#     
#     number_of_reviews	( Number of reviews, note that if empty is 0 ) 
#     
#     review_scores_rating
#     (overall review score rating)( this is an int in range [0, 100])( Note that this can be empty ('') )
#     
#     review_scores_accuracy 
#     ( this is an int in range [0, 100]) ( Note that this can be empty ('') )
#     
#     review_scores_cleanliness	
#     ( this is an int in range [0, 100]) ( Note that this can be empty ('') )
#     
#     review_scores_checkin	
#     ( this is an int in range [0, 100]) ( Note that this can be empty ('') )
#     
#     review_scores_communication	
#     ( this is an int in range [0, 100]) ( Note that this can be empty ('') )
#     
#     review_scores_location	
#     ( this is an int in range [0, 100]) ( Note that this can be empty ('') )
#     
#     review_scores_value 
#     ( this is an int in range [0, 100]) ( Note that this can be empty ('') )
#         
# We are going to be using since_year_host which does not seem to have any unusual features and is filled in for every listing. We are also going to be using review_scores_rating which has some unfilled columns, these collumns are simply left blank. The review_score_rating range is from 0-100 and the since_year_host range is from 2008 - 2015.
# 
# </font>

# ### Step 1b: Planning 
# #### Brainstorm ideas for what your program will produce
# #### Select the idea you will build on for subsequent steps
# 
# You must brainstorm at least three ideas for graphs or charts that your program could produce and choose the one that you'd like to work on. You can choose between a line chart, histogram, bar chart, scatterplot, or pie chart.
# 
# If you would like to change your project idea from what was described in the proposal, you will need to get permission from your project TA. This is intended to help ensure that your new project idea will meet the requirements of the project. Please see the project proposal for things to be aware of when communicating with your project TA.

# <font color="blue">
#  
#   Idea 1. 
#         Produce a line chart that uses the average of review score rating and compare it to each city. 
#     
#   Idea 2. 
#         Produce a line chart that uses the average of the review score rating and compare it to the number of bedrooms. 
#     
#   Idea 3. 
#         Produce a bar chart that compares the average of the review score rarting and a range of price, so for example, 
#     in the range under "200" a night what is the average rating, then for "300" and so on. 
#     
#     
# 
#    Our program would produce the most readable information if we used either a line chart, histogram or a scatterplot.
#     
# We believe the best out of these three options is the line chart because it will best present the relationship of how the rating changes based on the year of the host.
#     
# 
# </font>

# ### Step 1c: Planning 
# #### Write or draw examples of what your program will produce
# 
# You must include an image that shows what your chart or plot will look like. You can insert an image using the Insert Image command near the bottom of the Edit menu.

# ![Untitled.png](attachment:Untitled.png)

# ### Step 2a: Building
# #### Document which information you will represent in your data definitions
# 
# Before you design data definitions in the code cell below, you must explicitly document here which information in the file you chose to represent and why that information is crucial to the chart or graph that you'll produce when you complete step 2c.

# <font color="blue">
#     
# We will be representing the data review_score_rating and since_year_host. These two pieces of data are all we need to make our graph as it will use the since_year_host as the year on the x-axis, and it will use the average review_score_rating of every year as it's y-axis
# 
# </font>

# #### Design data definitions

# In[5]:


import matplotlib.pyplot as pyplot
from cs103 import *
from typing import List
from typing import NamedTuple
import csv


# In[6]:


##################
# Data Definitions

Airbnb = NamedTuple('Airbnb', [('year', int), # in range [2007, ...]
                              ('rating', int)]) # in range [0,100]

# interp. Information about Airbnb, including the year which represents the year_since_host,
# note that the year is in the range 2007 because Airbnb was founded in 2007 so it will not have prior data and 
# it is open to new updates. Additionally, the rating represents the review_score_rating, note that the rating
# is from 0 to 100, or none for a column with no rating, with 0 being the lowest rating and 
# 100 being the highest rating.

A0 = Airbnb(2008, 0)
A1 = Airbnb(2008, 100)
A2 = Airbnb(2015, 84)
A3 = Airbnb(2015, 84)

# Template form Compound with 2 fields.

@typecheck
def fn_for_airbnb (a:Airbnb) -> ... :
    return ...(a.year, a.rating)


# List[Airbnb]
# interp. A list of Airbnb

LOA0 = []
LOA1 = [A0]
LOA2 = [A0, A1]
LOA3 = [A0, A1, A2]
LOA4 = [A0, A1, A2, A3]

# Template form arbitrary sized and reference rule. 
@typecheck
def fn_for_loa(loa: List[Airbnb]) -> ...:
   
    # description of the accumulator acc = ... # type: ...
    for a in loa:
        acc = ...(fn_for_airbnb(a), acc)
    return ...(acc)


# ### Step 2b and 2c: Building
# #### Design a function to read the information and store it as data in your program
# #### Design functions to analyze the data
# 
# 
# Complete these steps in the code cell below. You will likely want to rename the analyze function so that the function name describes what your analysis function does.
# 
# Unless approved by your project TA, you **cannot** use libraries such as `numpy` or `pandas`. The project is meant as a way for you to demonstrate your knowledge of the learning goals in this course. While it is convinent to use external libraries, it will do all the work and will not help us gauge your mastery of the concepts.
# 
# You also cannot use built in list functions (e.g., `sum` or `average`) when writing code to do your substantial computation. Normally we encourage you to make use of what is already available but in this case, the final project involves demonstrating skills from class (e.g., how to work with a list). Using pre-built functions for this does not enable you to demonstrate what you know.
# 
# If you wish to change your project idea, you must **first** obtain permission from your TA. When contacting your TA, please provide a valid reason for why you want to change your project. Each time you change your topic idea, your TA will have to evaluate it to see if it will meet all of the project requirements. This is non-trivial task during one of the busiest times of the semester. As such, the deadline for project idea changes will be 3 business days before the deadline. Note that the deliverable deadline will not be extended and there is no compensation for the time you spent on the previous idea.

# In[ ]:





# In[7]:


@typecheck
def main(filename: str) -> None:
    """
    Reads information from given filename and returns a graph comparing
    the average review_score_rating over the years
    """
    # Template from HtDAP, based on function composition
    return analyze(read(filename))

@typecheck
def is_reliable(row_data: List[str]) -> bool:
    """
    Returns True if all of there exist a value in ratings and False otherwise.
    """
    # return True # stub

    # no template used

    if row_data[26] == '':
        return False # not reliable
    else:
        return True
   
    # this is a more simple way
    # return row_data[4] != "0" or row_data[5] != "0"

@typecheck
def read(filename: str) -> List[Airbnb]:
    """    
    reads information from the specified file and returns a list of airbnb
    hosts' data
    """
    #return []  #stub
    # Template from HtDAP
    # loa contains the result so far
    loa = [] # type: List[Airbnb]

    with open(filename) as csvfile:
       
        reader = csv.reader(csvfile)
        next(reader) # skip header line

        for row in reader:
            if is_reliable(row):
                a = Airbnb(parse_int(row[2]),parse_int(row[26]))
                loa.append(a)
   
    return loa

@typecheck 
def is_year(a: Airbnb, y:int)-> bool: 
    """
    Return true if year of Airbnb is equal to y, else return Flase. 
    """
    # return True # Stub 
    #temlplate from Airbnb with additional parameter y. 
    return a.year == y
    

start_testing()
expect(is_year(A0, 2000), False)
expect(is_year(A0, 2008), True)
expect(is_year(A1, 2008), True)
expect(is_year(A1, 2000), False)
expect(is_year(A2, 2020), False)
expect(is_year(A2, 2015), True)
summary()

@typecheck
def year_avg(loa: List [Airbnb], y: int) -> float:
    """
    Return a list with the average rating for the year
    """
    # return 0 #stub
    # template from List[Airbnb] with additional parameter y
    counter = 0
    acc = 0 # type: float
    for a in loa:
        if is_year(a,y):
            acc = acc + a.rating
            counter += 1
    if counter == 0:
        return 0
    else:
        return acc / counter
    

@typecheck 
def get_y(loa: List[Airbnb])-> List[float]: 
    """
    return a list of the average rating for each year form 2008 to 2015
    """
    # return List[] #Stub
    #Template from composition

    return [year_avg(loa, 2008), year_avg(loa, 2009), year_avg(loa, 2010), year_avg(loa, 2011), year_avg(loa, 2012), year_avg(loa, 2013), year_avg(loa, 2014), year_avg(loa, 2015)]


start_testing()
expect(get_y(LOA0),[0,0,0,0,0,0,0,0])
expect(get_y(LOA2), [50, 0,0,0,0,0,0,0])
summary()

@typecheck 
def get_x() -> List[int]:
    """
    returns a list of years from 2008 to 2015
    """
    # return [] #stub
    # No template used. 
    
    return [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]

start_testing()
expect(get_x(),[2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015])

summary()

@typecheck
def analyze(loa: List[Airbnb]) -> None:
    """
    return a graph comparing review rating and the year
    """  
    # x_vals = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015] this is also valid, but you will need to change  pyplot.plot to pyplot.plot(x_vals, get_y(loa))
    
    # return none #stub
    # Template based on visualization
    # set the x-axis label, y-axis label, and plot title
    pyplot.xlabel('Year')
    pyplot.ylabel('Average Rating')
    pyplot.title('Average rating of airbnb hosts over years')

    pyplot.plot(get_x(), get_y(loa))

    # show the plot
    pyplot.show()
   
    return None





# Begin testing
start_testing()

# examples and tests for read
expect(read("air_bnb_subset-test.csv"),  
       [Airbnb(2011, 96),
        Airbnb(2013, 70)])

expect(read("air_bnb_subset-test-2.csv"), [Airbnb(2014, 100)])

# examples and tests for main
expect(main("air_bnb_subset.csv"), None)
expect(main("air_bnb_subset-test-2.csv"), None)

# examples and tests for is_reliable
expect(is_reliable(["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27"]), True)
expect(is_reliable(["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "", "27"]), False)

# examples and tests for analyze
expect(analyze([A1, A3]), None)
expect(analyze([A1]), None)
expect(analyze([A3]), None)

# examples and tests for year_avg
expect(year_avg([A1, A3], 2004), 0)
expect(year_avg([A1, A3], 2009), 0)
expect(year_avg([A1, A3], 2008), 100)
expect(year_avg([A1, A3], 2015), 84)

# show testing summary
summary()


# ### Final Graph/Chart
# 
# Now that everything is working, you **must** call `main` on the intended information source in order to display the final graph/chart:

# In[8]:


main('air_bnb_subset.csv')


# In[9]:


# Be sure to select ALL THE FILES YOU NEED (including csv's) 
# when you submit. As usual, you cannot edit this cell.
# Instead, run this cell to start the submission process.
from cs103 import submit

COURSE = 123409
ASSIGNMENT = 1615244 # Final submission

submit(COURSE, ASSIGNMENT)

# If your submission fails, SUBMIT by downloading your files and uploading them 
# to Canvas. You can learn how on the page "How to submit your Jupyter notebook" 
# on our Canvas site.


# # Please double check your submission on Canvas to ensure that the right files (Jupyter file + CSVs) have been submitted and that the files do not contain unexpected errors.
# 
# <font color="red">**You should always check your submission on Canvas. It is your responsibility to ensure that the correct file has been submitted for grading.**</font> Regrade or accomodation requests using reasoning such as "I didn't realize I submitted the wrong file"/"I didn't realize the submission didn't work"/"I didn't realize I didn't save before submitting so some of my work is missing" will not be considered.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




