# Path 2 Data Set
The data set that will be discussed and analyzed within this report is data set 2: Bike Traffic.  The data given through this path is a csv file including sensor data in 8 different categories separated by date.  These categories of data include high temperature of the day, low temperature of the day amount of precipitation, the total number of bikers on the Brooklyn bridge, Manhattan bridge, Williamsburg bridge, and Queensboro bridges respectively, and the total number of bikers on all four bridges during the one-day period combined.  This amount of sensor data will be used to answer analysis questions 1-3 and make predictions regarding the behavior of bikers around the bridge.

## Question 1: Top 3 Bridges
### Analysis Methods
The first analysis question discussed in this path asks if sensors were installed on three out of the four bridges, which three bridges would give us the best estimate of overall traffic amongst the four.   In order to answer this question, we need to know what the average number of riders per day on all four bridges is, and which three bridges represent this data the best.  The method created to determine this information begins with taking the total number of riders per day and dividing it by four to take the average number of riders per day amongst all four bridges.  In order to determine which bridge best represents this number during one day, the model takes the distance from the number of riders per day on each bridge from the average number of riders per day.  The bridge that is the closest to the average for that day is assessed a ‘point’ to its score.  This process is repeated every day, each day adding a ‘point’ to the count for the bridge that best represents the average.  At the end of the process the bridges with the highest three scores are proved to be the ones that best represent the average amount of bike traffic for that day.  
### Results
The scores given to each bridge using the above discussed analysis method are as follows: Brooklyn Bridge: 41, Manhattan Bridge: 33, Williamsburg Bridge: 0, Queensboro Bridge: 140.  Since the score for the Queensboro Bridge is the highest, we can say that the Queensboro Bridge is the best representation of overall bridge traffic data.  We can deduce similarly for the Brooklyn Bridge which placed second and the Manhattan Bridge which placed third.  The Williamsburg Bridge finished with a score of zero.  We can very clearly deduce from this that the Williamsburg Bridge is the least accurate representation of the total amount of bikers per day amongst all bridges.  The sensors should be installed on the Queensboro, Brooklyn, and Manhattan Bridges.  

## Question 2: Weather Prediction
### Analysis Method
The second analysis question answered with the model asks to use data regarding weather on different days to predict the number of total bikers that will be seen on all four bridges in one day.  In order to do this, a linear regression model is created using the data given to us regarding high temperatures, low temperatures, and amount of precipitation in a day.  Since there are three data points considered when determining the expected number of riders on the bridge in one day, the model uses multiple regression to consider each data point rather than just one, providing a more accurate result.  The linear regression equation created will be of the form represented in Equation 1.  
$$ f(x) = a_1 x_1 + a_2 x_2 + a_3 x_3 + b
Equation 1: Form of the Desired Multiple Regression Equation
x_1represents the high temperature for the day in question, x_2 represents the low temperature for the day, and x_3 represents the amount of precipitation.  The model is trained using the given data for these conditions.  

### Results
The equation created by the model is represented in Equation 2.

$$ f(x) = 390.918x_1-162.320x_2-7951.48x_3+178.21

Equation 2: Resulting Multiple Regression Equation
In order to test the model, a percentage of the data is set aside as testing data and run through this derived equation.  From the results of this testing data, the mean squared error can be calculated, giving an estimate on the model’s accuracy.  The resulting mean squared error is 4024.73.  A high mean squared error means that the accuracy of the model cannot be perfectly guaranteed.  However, the model provides a good starting estimate as to the general number of bikers one can expect within a day. 
