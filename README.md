# Motor Vehicle Death Analysis - What are the factors contributing to fatal car crashes in the US?
For this project, we are going to use the CRoss Industry Standard Process for Data Mining:
## The CRISP-DM Framework
![CRISP-DM](./src/crispdm.png)

## Business Understanding
Analysing socio-economic data to identify factors contributing to reduce MVD in the US and provide actionables. Our typical stakeholder would be municipalities, trying to make roads safer and potentially insurances companies, optimizing their policies.

## Data Understanding
The dataset is issued the result of the collaboration between the [Robert Wood Johnson Foundation](https://www.rwjf.org/) and the [University of Wisconsin Population Health Institute](https://uwphi.pophealth.wisc.edu/) and it uses the 2019 [County Health Ratings](https://www.countyhealthrankings.org/) data.

It comes in the form of an excel spreadsheet with 7 sheets. Only 3 contain data, the other 4 providing context to that data. This data source covers a lot of variables but we have decided to focus on the following:

- Child mortality
- Children eligible for free or reduced price lunch
- Demographics
- Diabetes prevalence
- Disconnected youth
- Drug overdose deaths
- Firearm fatalities
- Food insecurity
- Frequent mental distress
- Frequent physical distress
- HIV prevalence
- Home ownership
- Homicides
- Infant mortality
- Insufficient sleep
- Life expectancy
- Limited access to healthy foods
- Median household income
- **Motor vehicle crash deaths**
- Other primary care providers
- Premature age-adjusted mortality
- Residential segregation
- Severe housing cost burden
- Uninsured adults
- Uninsured children

The dataset summarises 3142 observations, with a granularity down to the county level. Where possible, numbers are broken down to racial background (Black/Hispanic/White) and confidence intervals (95%) are provided for most observations.

## Data Preparation
All merging, cleaning, transformations involved in the preprocessing stage. The [DataPreparation](./DataPreparation.ipynb) notebook details the steps of this process, and contains the python code used during that step. We decided to replace the $NaN$ values with the state average for all the indicators. Most of the missing values were due to the figures not being detailed enough (especially not being linked to the race), so we will have to address the issue on a population level, more than a racial level.

## Modelling
After taking into account various factors (variance inflation factor, multicollinearity and intuition), we have managed to narrow down the amount of features used in our model to 10 features:
- % Physically Inactive
- % Excessive Drinking
- % Alcohol Impaired
- % Uninsured
- % Long Commute - Drives Alone
- Household Income
- Population
- % under 18
- % 65 and over
- % Rural

The baseline model used a simple linear regression without transforming any data (besides the scaling step) and showed an accuracy of about 50%. In order to increase the accuracy, the final (selected) model used a cubic polynomial transformation and it was penalised with a LASSO (least absolute shrinkage and selection operator) method. This combination allowed the accuracy to go up to 56%. Considering our third degree polynomial and the feature expansion subsequent to this transformation, we decided to sacrifice the few extra percent of accuracy offered by an ElasticNet penalisation method for the feature slayer: LASSO.

At the end of the regularisation/penalisation process, we were left with 51 features and interactions.

## Evaluation
After selecting our model, we ran the model on the test dataset and it showed similar performances (slightly better actually), meaning that this model, although not hugely accurate, is robust.

The analysis of the residuals showed that the data is heteroscedatic and biased. This is mainly due to the features selected. A finer tuning of feature selection process would improve the model significantly but we strongly believe interpretability would be handicapped by such a move.

## Deployment
Refer to the [Presentation](./presentation.pdf) slides for a detailed view of our findings.

__Note__

For more details, have a look at the [index](./index.ipynb) notebook. It contains the statistical analysis as well as all the code used in this project.

_Work by Pete and Antoine_