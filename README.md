# LLM Prerequisites

---

## 📝 Overview

This repository covers:

1. **Python Fundamentals**
   - Functions and Modules
   - Data Types
   - Error Handling
   - Classes & Object-Oriented Programming (OOP)

2. **Essential Python Libraries for LLM & Data Analysis**
   - **NumPy**: Efficient numerical computations
   - **Pandas**: Data manipulation and analysis
   - **Matplotlib**: Data visualization
   - **Seaborn**: Statistical data visualization

3. **Mini Projects**
   - Practical exercises combining Python basics and library usage to build small projects.

---

## Python Concepts Covered

- **Functions & Modules**: Writing reusable functions, importing and using modules.
- **Data Types**: Strings, lists, dictionaries, tuples, sets, and their operations.
- **Error Handling**: Try-except blocks, custom exceptions.
- **Classes & OOP**: Creating classes, inheritance, encapsulation, and polymorphism.

---

## 📊 Libraries Covered

### NumPy
- Array creation and manipulation
- Mathematical operations
- Linear algebra basics
- Random number generation

### Pandas
- Series and DataFrame creation
- Data cleaning and preprocessing
- Filtering, grouping, and aggregation
- Exporting and importing datasets

### Matplotlib
- Line plots, bar charts, histograms
- Customizing plots (title, labels, colors, styles)
- Saving plots as images

### Seaborn
- Statistical plots: boxplot, violin plot, pairplot
- Visualizing relationships and distributions
- Heatmaps and correlation plots

---

## 🚀 Mini Projects

### 1. **Student Manager**
- File: `Student_manager.py`
- Manage student data using CSV
- Features:
  - Show all students
  - Update student grades
  - Filter top students (A/B) and save to CSV

### 2. **To-Do App**
- File: `todo.py`
- Manage daily tasks using JSON storage
- Features:
  - Show, add, remove tasks
  - Mark tasks as complete

### 3. **Weather Analyzer**
- File: `Weather_analyzer.py`
- Analyze weather data from CSV
- Features:
  - Calculate max, min, and average temperature and humidity
  - Plot daily temperature trends and humidity levels using Matplotlib

---

# 📘 ML_basics

**ML_basics** is a learning resource that focuses on the **mathematical and statistical foundations of Machine Learning**.  
It includes Python scripts that cover **Calculus, Linear Algebra, and Probability & Statistics**—the essential building blocks of ML algorithms.

---
 
## 🚀 Topics Covered

###  Calculus
- Derivatives and their role in ML.
- Gradient Descent basics for cost function minimization.

###  Linear Algebra (Core Foundations)
- Vectors and their operations.
- Dot product and geometric interpretation.
- Matrices and transformations.
- Matrix multiplication and applications in ML.

###  Probability & Statistics
- Conditional probability and Bayes' theorem.
- Discrete and continuous distributions.
- Expectation, variance, and standard deviation.

---

# Machine Learning Examples: Supervised & Unsupervised Learning

This repository contains practical examples and implementations of **Supervised** and **Unsupervised Learning** concepts in Python. It is designed for learners to understand core ML algorithms from scratch and using libraries like scikit-learn.

---

## Table of Contents

- [Supervised Learning](#supervised-learning)
  - [Classification](#classification)
  - [Regression](#regression)
  - [Loss Functions](#loss-functions)
  - [Train Test Split](#train-test-split)
- [Unsupervised Learning](#unsupervised-learning)
  - [Clustering](#clustering)
  - [Dimensionality Reduction](#dimensionality-reduction)
- [Prerequisites](#prerequisites)
- [How to Run](#how-to-run)
- [Folder Structure](#folder-structure)
- [References](#references)

---

## Supervised Learning

Supervised learning involves training models using **labeled data**. The goal is to predict outputs for new, unseen data based on prior examples.

### Classification

Classification models categorize input data into predefined classes.

- **`iris_classifier.py`**: Classifies Iris flowers based on features like petal and sepal length/width.

### Regression

Regression models predict continuous values based on input features.

- **`linear_regression_scratch.py`**: Implements linear regression from scratch using numpy.  
- **`linear_regression_sklearn.py`**: Linear regression implementation using scikit-learn.  
- **`polynomial_regression.py`**: Demonstrates polynomial regression for non-linear relationships.

### Loss Functions

Loss functions measure how well a model predicts the target output.

- **`cross_entropy_loss.py`**: Cross-entropy loss for classification tasks.  
- **`mse_loss.py`**: Mean squared error (MSE) for regression tasks.

### Train Test Split

- **`train_test_split.py`**: Custom implementation to divide dataset into training and testing sets.

---

## Unsupervised Learning

Unsupervised learning involves training models on **unlabeled data** to discover patterns, clusters, or lower-dimensional representations.

### Clustering

Clustering groups similar data points together.

- **`customer_segmentation.py`**: Clusters customers based on purchasing behavior.  
- **`hierarchical_clustering.py`**: Demonstrates hierarchical clustering techniques.  
- **`kmeans_basic.py`**: Basic K-Means clustering example.  
- **`kmeans_iris.py`**: Applies K-Means clustering to the Iris dataset.

### Dimensionality Reduction

Dimensionality reduction simplifies high-dimensional data while retaining important information.

- **`pca_basics.py`**: Introduction to Principal Component Analysis (PCA).  
- **`pca_on_iris.py`**: PCA applied to the Iris dataset for visualization and analysis.  

---
