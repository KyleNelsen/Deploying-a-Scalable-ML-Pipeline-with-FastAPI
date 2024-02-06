# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
The model is a Random Forest Classifier from scikit-learn. It's random state is set to 42 for consistent results.
## Intended Use
The intended use is to predict whether the income of someone exceeds $50K/yr based on census data.
## Training Data
The data comes from the UC Irvine Machine Learning Repository. It's the census from 1994. It includes 48842 instances and 14 features. The training set uses 80% of the data.
## Evaluation Data
The evaluation set uses 20% of the data. The data is split the same every run because the random state is set to 42.
## Metrics
The metric used were precision, recall and F1 score. The precision was 0.742, the recall was 0.638 and the F1 score was 0.686
## Ethical Considerations
There could be bias in the data and predictions based on how it is split and the amount of data that is availiable.
## Caveats and Recommendations
The data is from the 1994 census, so it would be wise to only make predictions off of data from that year for accuracy.