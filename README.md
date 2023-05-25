# Kaggle Playground Competition - Season 3, Episode 15

## Description
This README provides an overview of my submission for the Season 3, Episode 15 of the Kaggle Playground Competition. The goal of this competition is to impute the missing values of the feature x_e_out, which represents the equilibrium quality of a pressurized water reactor.

## Data Analysis
To begin, I performed a basic analysis of the dataset and discovered that the dataset contained a significant number of missing values.Therefore, through exploratory data analysis, I looked for correlations between certain features in order to impute missing values. Once I had succesfully cleaned the data and filled in all missing values, I was ready to move onto model building. 

## Modelling Approach
Since x_e_out was our feature that the competition would be evaluated on, I treated this as a regression problem aimed at predicting the missing values for this feature. I used a machine learning approach and trained several models using the available data, and evaluated these using root mean squared error (RMSE). 

## Results
After thorough data analysis and model training, my submission achieved promising results in imputing the missing values of the equilibrium quality. The model performed well, achieving a root mean square error (RMSE) score of 0.075928.

The features that played a crucial role in accurately predicting the missing values were the author (Weatherhead or Peskov), the experimental critical heat flux, and the heated length. Leveraging these important features allowed for a deeper understanding of the pressurized water reactor's behavior and enabled accurate imputations.

## Conclusion
In conclusion, my submission for the Kaggle Playground Competition Season 3, Episode 15 successfully addressed the task of imputing missing values in the equilibrium quality of a pressurized water reactor. The competition provided valuable insights into how to approach a dataset that contains a lot of missing values and I definitely gained a lot of experience in learning different ways to approach this sort of problem. 