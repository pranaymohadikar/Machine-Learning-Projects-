# Airplane Accident Prediction

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Project Overview and data description

An aviation accident is defined by the Convention on International Civil Aviation Annex 13 as an occurrence associated with the operation of an aircraft, which takes place from the time any person boards the aircraft with the intention of flight until all such persons have disembarked, and in which a) a person is fatally or seriously injured, b) the aircraft sustains significant damage or structural failure, or c) the aircraft goes missing or becomes completely inaccessible. Annex 13 defines an aviation incident as an occurrence, other than an accident, associated with the operation of an aircraft that affects or could affect the safety of operation

This dataset was obtained from the kaggle Airplane accidents severity Dataset

- Accident_ID:                unique id assigned to each row
- Accident_Type_Code:           the type of accident (factor, not numeric)
- Cabin_Temperature:            the last recorded temperature before the incident, measured in degrees fahrenheit
- Turbulence_In_gforces:      the recorded/estimated turbulence experienced during the accident
- Control_Metric:               an estimation of how much control the pilot had during the incident given the factors at play
- Total_Safety_Complaints:     number of complaints from mechanics prior to the accident
- Days_Since_Inspection:        how long the plane went without inspection before the incident
- Safety_Score:                 a measure of how safe the plane was deemed to be
- Severity:                    a description (4 level factor) on the severity of the crash (target)

This project is devided into 
- Data cleaning
- EDA 
- Visualization
- Feature Engineering
- Model Building
- Prediction

### Visualization
- Severity in airplane accidents


![Severity](https://github.com/pranaymohadikar/Machine-Learning-Projects-/blob/master/Airplane%20accidents%20severity%20Dataset/readme-resources/severity.PNG)

- severity occurence

![occurence](https://github.com/pranaymohadikar/Machine-Learning-Projects-/blob/master/Airplane%20accidents%20severity%20Dataset/readme-resources/type%20of%20severity%20with%20counts.png)

- cabin temperature vs accidents

![ct](https://github.com/pranaymohadikar/Machine-Learning-Projects-/blob/master/Airplane%20accidents%20severity%20Dataset/readme-resources/cabin%20temp%20vs%20severity.png)

It looks like for all the accidents cabin temperature remains almost same.

- Maximum elevation vs accidents

![me](https://github.com/pranaymohadikar/Machine-Learning-Projects-/blob/master/Airplane%20accidents%20severity%20Dataset/readme-resources/max%20elevation%20vs%20severity.png)

hence most types of accidents occur at the height of 30k ft.

### Model building

- Random forest classifier with classification report

![rfc](https://github.com/pranaymohadikar/Machine-Learning-Projects-/blob/master/Airplane%20accidents%20severity%20Dataset/readme-resources/random%20forest%20with%20classification%20report.png)

It look like the AUC score for the model is 0.95

- heatmap

![hm](https://github.com/pranaymohadikar/Machine-Learning-Projects-/blob/master/Airplane%20accidents%20severity%20Dataset/readme-resources/heatmap%20of%20classification%20report.png)

Heatmap looks promising as it give best result

### Prediction with accuracy
Accuracy : **~95%**

![pred](https://github.com/pranaymohadikar/Machine-Learning-Projects-/blob/master/Airplane%20accidents%20severity%20Dataset/readme-resources/prediction.png)

This model gives pretty accurate predictions

