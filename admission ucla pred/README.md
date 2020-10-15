# Graduate Admission Prediction

This repository contains all the files related to the project
- Graduate Admission predictor [webbapp](https://admission-predictor-v1.herokuapp.com/)
- Repo of webapp [repo](https://github.com/pranaymohadikar/Admission-predictor-deployment)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Project Overview and data description

This dataset is created for prediction of Graduate Admissions from an Indian perspective.

The dataset contains several parameters which are considered important during the application for Masters Programs.
The parameters included are :

GRE Scores ( out of 340 )
TOEFL Scores ( out of 120 )
University Rating ( out of 5 )
Statement of Purpose and Letter of Recommendation Strength ( out of 5 )
Undergraduate GPA ( out of 10 )
Research Experience ( either 0 or 1 )
Chance of Admit ( ranging from 0 to 1 )


This project is divided into :
- data cleaning
- EDA 
- Visualization
- Feature Engineering
- Model Building
- Prediction

## Visualization

- chances of admission vs GRE score

![chances of admission vs GRE score](https://github.com/pranaymohadikar/Machine-Learning-Projects-/blob/master/admission%20ucla%20pred/readme-resources/coa%20vs%20gre.PNG)

- chances of admission vs Research

![chances of admission vs Research](https://github.com/pranaymohadikar/Machine-Learning-Projects-/blob/master/admission%20ucla%20pred/readme-resources/coa%20vs%20research.PNG)

- chances of admission vs TOEFL

![chances of admission vs TOEFL](https://github.com/pranaymohadikar/Machine-Learning-Projects-/blob/master/admission%20ucla%20pred/readme-resources/coa%20vs%20toefl.PNG)

### Distribution plots

![1](https://github.com/pranaymohadikar/Machine-Learning-Projects-/blob/master/admission%20ucla%20pred/readme-resources/UR_sop.PNG)
![2](https://github.com/pranaymohadikar/Machine-Learning-Projects-/blob/master/admission%20ucla%20pred/readme-resources/gre_toefl.PNG)
![3](https://github.com/pranaymohadikar/Machine-Learning-Projects-/blob/master/admission%20ucla%20pred/readme-resources/lor_cgpa.PNG)
![4](https://github.com/pranaymohadikar/Machine-Learning-Projects-/blob/master/admission%20ucla%20pred/readme-resources/res_coa.PNG)

### Results
Accuracy: **~82%**

## Deployed Webapps
- **Github** : [https://github.com/pranaymohadikar/Admission-predictor-deployment](https://github.com/pranaymohadikar/Admission-predictor-deployment)
- **Web app** : [https://admission-predictor-v1.herokuapp.com/](https://admission-predictor-v1.herokuapp.com/)
