overfitting: data less too many predictor variables

min sample size for regressions : 
    50 for each term
additional 8 observations per predictor variable
for 1 term and 3 predictor variables:
    50 + (8*3) = 74 observations
ways to avoid overfitting:
    cross validation:
        partitions the given data and generalises the model, choosing the model which works the best.
        works on predicted sq(R) values.
        more reliable meashure of the model's quality.


K Nearest Neighbour:
    assumes similarity b/w new data and the available data and aligns them in the same category