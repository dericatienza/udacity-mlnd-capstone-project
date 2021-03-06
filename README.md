
# Udacity Machine Learning Nanodegree Capstone Project
This project was initiated to fulfill my requirements for graduation of Udacity's Machine Learning Nanodegree program.
## Project
I delved into my thoughts and reasoning behind my approach and decisions for this project in the _report.pdf_ or on my blog posts [part 1](https://medium.com/@dericatienza/predicting-used-car-prices-with-linear-regression-in-amazon-sagemaker-part-1-6cdde61fd365) and [part 2](https://medium.com/@dericatienza/predicting-used-car-prices-with-linear-regression-in-amazon-sagemaker-part-2-c6dfdab7ea5).
## Dataset
This is the dataset that the project will be using. It contains only one file - *vehicle.csv.* It is included in the repository and can be pulled with [Git LFS](https://git-lfs.github.com/) installed or you can opt to download it on [Kaggle](https://www.kaggle.com/austinreese/craigslist-carstrucks-data/version/4).
## Setup
The _linearlearner_model.ipynb_ and _xgboost_model.ipynb_ notebooks need to be run on an Amazon SageMaker notebook instance in order to run properly as these two notebooks use SageMaker's built-in algorithms and tools.

All other notebooks should run fine as long as the below packages are installed:

 - numpy
 - pandas
 - matplotlib
 - seaborn
 - scikit-learn
 - imbalanced-learn
