<header>
Introduction to Time Series (TS) Forecasting
============
</header>

**Microsoft-Trinity Mentoring Program: February, 2020**

<main>

- [Introduction to Time Series (TS) Forecasting](#introduction-to-time-series-ts-forecasting)
- [1. Input Data](#1-input-data)
- [2. Visualization of Time-Series](#2-visualization-of-time-series)
- [3. Decomposition of Time-Series](#3-decomposition-of-time-series)
  - [3.1. Practical Examples in Python](#31-practical-examples-in-python)
- [4. Best Practices for Training Forecasting Models](#4-best-practices-for-training-forecasting-models)
- [5. List of Forecasting Models](#5-list-of-forecasting-models)
  - [5.1. Common Univariate Time Series Forecasting Models for Regression](#51-common-univariate-time-series-forecasting-models-for-regression)
  - [5.2. Common Multivariate Time Series Forecasting Models for Regression](#52-common-multivariate-time-series-forecasting-models-for-regression)
- [6. Performance Measures for Time Series Models](#6-performance-measures-for-time-series-models)
- [7. Popular Libraries in `Python`](#7-popular-libraries-in-python)
- [8. Vanilla Examples of Forecasting Tasks](#8-vanilla-examples-of-forecasting-tasks)
- [9. Interesting Reading](#9-interesting-reading)
- [10. Useful Github Repos and Blogs](#10-useful-github-repos-and-blogs)

This document provides information about the steps required to perform Time Series forecasting as part of the Microsoft-Trinity mentoring program. Before certain terminologies are introduced it is important to familiarize yourself with some key concepts:

* **What is time series**: A time series is a series of data points indexed (or listed or graphed) in time order. Most commonly, a time series is a sequence taken at successive equally spaced points in time. Thus it is a sequence of discrete-time data. Examples of time series are heights of ocean tides, counts of sunspots, and the daily closing value of the Dow Jones Industrial Average. (source: [Wikipedia](https://en.wikipedia.org/wiki/Time_series))
* **What is the difference between univariate and multivariate time series forecasting**: 
    * **Univariate Time Series**: The term "univariate time series" refers to a time series that consists of single (scalar) observations recorded sequentially over equal time increments. Some examples are monthly CO2 concentrations and southern oscillations to predict el nino effects.
    *  **Multivariate Time Series**: The multivariate model is a popular statistical tool that uses multiple variables to forecast possible outcomes. Research analysts use multivariate models to forecast investment outcomes in different scenarios in order to understand the exposure that a portfolio has to particular risks.
* **What are the most common types of time series forecasting scenarios**: There two main times of time series forecasting methods. Time series **regression** and time series **classification**. The following articles are very helpful to understand the key differences:
    * Regression and Classification Machine Learning: What's the Difference? ([link](https://medium.com/quick-code/regression-versus-classification-machine-learning-whats-the-difference-345c56dd15f7))
    * Regresssion vs. Classification Algorithms ([link](https://blogs.oracle.com/datascience/regression-vs-classification-algorithms))

**Suggestions from the Mentors**:
1. Start simple! Pick your dataset and try to identify the problem. Answer the following questions:
   * Is this a TS regression or classification problem?
   * Is it a univariate or multivariate TS problem?
   * Do I need to forecast one step or multiple steps ahead?
2. Try to understand your data by computing simple statistics and creating data visualization charts
3. **If it is a univariate time series problem**, then try to find ways to extract information from your univariate TS by answering the following questions:
   * Is the TS stationary?
   * Do the TS exhibit seasonality?
   * Are there any trends?
   * Can I use lags of my time series to influence my model predictions?
   * Are there any other characteristics (e.g. weekly peaks etc.) I can extract from the TS?
   * Is there any other way I can capture the seasonality in my data?
   * What is the simplest model I can train?
   * What steps I need to take to train my model efficiently? What is training, validation and test error? ([link](https://otexts.com/fpp2/basic-steps.html))
   * How can I measure the performance of my model?
   * How can I calculate a confidence interval of my prediction?
   * Is there any way I can improve the model?
4. **If it is a multivariate time series problem** then try to:
   * Understand if there any relationships between the target variable and the available features
   * Which features do I need to incorporate in my analysis?
   * Are there any seasonal patterns in my data I should take into consideration?
   * What is the simplest model I can train?
   * What steps I need to take to train my model efficiently? What is training, validation and test error? ([link](https://otexts.com/fpp2/basic-steps.html))
   * How can I measure the performance of my model?
   * How can I calculate a confidence interval of my prediction?
   * Is there any way I can improve the model?
 
# 1. Input Data

- **Appliances Electricity Usage Prediction** - The appliances electricity usage prediction data set contains data averaged every 10 minutes and contains: the timestamp, electricity in Wh used by appliances and lights, temperature and humidity in several rooms in the house as measured by sensors and weather data from a nearby weather station showing temperature, pressure, relative humidity, wind speed, visibility and dewpoint. There are also 2 random values added at the end for testing the models.
- **Electric Devices** - The electric devices data set was recorded as part of a UK government sponsored study whose intention was to collect behavioural data about how consumers use electricity within the home to help reduce the country's carbon footprint. The data has already been preprocessed and contains readings from 251 households, sampled in two-minute intervals over approximately one month. The data consists of an unlabelled table in three formats (.txt, typescript and weka) whose columns (96) are electric devices, the rows are the time of the record (8926 for training and 7711 for testing) and there are 7 different classes.

# 2. Visualization of Time-Series

1. Simplistic Examples of TS Visualization in Python: ([link](https://machinelearningmastery.com/time-series-data-visualization-with-python/))
2. Interactive Time Series Visualization with `Plotly` and Python: ([link](https://towardsdatascience.com/introduction-to-interactive-time-series-visualizations-with-plotly-in-python-d3219eb7a7af))
3. Time Series Visualization using Python `Pandas`: ([link](https://www.dataquest.io/blog/tutorial-time-series-analysis-with-pandas/))
4. Time Series Analysis with `Pandas`: ([link](https://ourcodingclub.github.io/2019/01/07/pandas-time-series.html))
5. Plotting Time Series Videos ([link](https://www.youtube.com/watch?v=jV24N7SPXEU), [link](https://campus.datacamp.com/courses/visualizing-time-series-data-in-python/work-with-multiple-time-series?ex=5))
6. Visualization of Time Series using `plotly` ([link](https://plot.ly/python/time-series/))

# 3. Decomposition of Time-Series

## 3.1. Practical Examples in Python

1. Seasonal-Trend decomposition using LOESS (STL) ([link](https://www.statsmodels.org/dev/examples/notebooks/generated/stl_decomposition.html))
2. Time Series decomposition in `Python` ([link](https://www.machinelearningplus.com/time-series/time-series-analysis-python/))
3. Time Series decomposition (examples in `R`) ([link](https://otexts.com/fpp2/decomposition.html))

# 4. Best Practices for Training Forecasting Models

Introduction to cross validation for TS:
1. Examples with code in `Python`: ([link](https://towardsdatascience.com/time-series-machine-learning-regression-framework-9ea33929009a))
2. Cross validation for TS models: ([link](https://campus.datacamp.com/courses/machine-learning-for-time-series-data-in-python/validating-and-inspecting-time-series-models?ex=6), [link](https://medium.com/eatpredlove/time-series-cross-validation-a-walk-forward-approach-in-python-8534dd1db51a))

# 5. List of Forecasting Models

## 5.1. Common Univariate Time Series Forecasting Models for Regression

* `AR`: Autoregressive model ([link](https://www.statsmodels.org/stable/generated/statsmodels.tsa.ar_model.AR.html))
* `(S)ARIMA`: (Seasonal )Autoregressive Integrated Moving Average ([link](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima_model.ARIMA.html#statsmodels.tsa.arima_model.ARIMA), [link](http://alkaline-ml.com/pmdarima/0.9.0/modules/generated/pyramid.arima.auto_arima.html)) ([link](https://wngaw.github.io/auto-arima-with-pyramid/))

## 5.2. Common Multivariate Time Series Forecasting Models for Regression

* `Linear Regression` (including L1 and L2 regression models): ([link]([)](https://scikit-learn.org/stable/modules/linear_model.html))
* `Support Vector Regression`: ([link](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html))
* `Random Forest`: ([link](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html))
* `Gradient Boosting Regression`: ([link](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html))

# 6. Performance Measures for Time Series Models

* Time Series Performance Measures with Python: ([link](https://machinelearningmastery.com/time-series-forecasting-performance-measures-with-python/))
* This is an implementation in `R` but it will give you a lot insights that you can use in Python ([link](https://otexts.com/fpp2/accuracy.html))

# 7. Popular Libraries in `Python`

**Univariate Setting**
1. `statsmodels`: ([link](https://www.statsmodels.org/dev/examples/index.html#time-series-analysis))
2. `PROPHET`: ([link](https://facebook.github.io/prophet/docs/quick_start.html)
3. `pyramid`: ([link](http://alkaline-ml.com/pmdarima/0.9.0/index.html))

**Multivariate Setting**:
1. Machine Learning Techniques using: `scikit-learn`: ([link](https://scikit-learn.org/))
   * TS split using `scikit-learn`: ([link](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html))
2. Deep Learning Techniques using: `keras`: ([link](https://keras.io/))

# 8. Vanilla Examples of Forecasting Tasks

* Code Implementation in the teams repo: Forecasting Monthly Sunspots using a Multivariate TS Approach ([link]()) (**not available yet**)

# 9. Interesting Reading

1. Stanford: TS Sales Forecasting: ([link](http://cs229.stanford.edu/proj2017/final-reports/5244336.pdf))
2. Stanford: TS Forecasting using Deep Learning ([link](http://cs230.stanford.edu/projects_spring_2019/reports/18680194.pdf))

# 10. Useful Github Repos and Blogs

1. Backtesting TS models: ([link](https://machinelearningmastery.com/backtest-machine-learning-models-time-series-forecasting/))
2. Robust TS decomposition: ([link](https://github.com/LeeDoYup/RobustSTL))
3. GluonTS: Probabilistic Time Series Modeling in Python: ([link](https://github.com/awslabs/gluon-ts)) - (**not priority**)
4. Examples of Machine Learning models: ([link](https://github.com/maxim5/time-series-machine-learning/tree/master/models))
5. Univariate TS forecasting (Blog): ([link](https://towardsdatascience.com/an-overview-of-time-series-forecasting-models-a2fa7a358fcb))
6. Azure ML learning paths (contains several learning modules) ([link]( https://docs.microsoft.com/en-us/learn/paths/ml-crash-course/) [link](https://docs.microsoft.com/en-us/learn/paths/intro-to-ml-with-python/)):
7. Azure ML learning modules ([link](https://docs.microsoft.com/en-us/learn/modules/interactive-deep-learning/), [link](https://docs.microsoft.com/en-us/learn/modules/train-local-model-with-azure-mls/))