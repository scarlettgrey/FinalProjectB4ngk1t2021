Step-by-step we used in this project:
1. Download the dataset from https://www.kaggle.com/kaushil268/disease-prediction-using-machine-learning
2. Preprocessing the data using python </br>
a. Change the label from name of the disease to numeric value like Fungal Infection -> 1 </br>
b. Creating Disease Label file for get the disease name after prediction done
3. Creating Model using tensorflow.keras.models.Sequential </br>
a. Our model consisting of 5 layer of dense with input_size equal equal to number of symptoms from the data (132) and output size was 42 </br>
b. 1st, 3rd, 4th layers using relu activation </br>
c. 2nd layers using selu activation </br>
d. 5th layers using softmax activation because it’s not binary prediction </br>
1[](https://github.com/scarlettgrey/FinalProjectB4ngk1t2021/blob/main/Images/model.jpg)
4. Training the model using model.compile </br>
a. Our loss function is sparse_categorical_crossentropy </br>
b. Our optimizer is adam </br>
c. After 50 epoch it’s get 100% acc on training </br>
![](https://github.com/scarlettgrey/FinalProjectB4ngk1t2021/blob/main/Images/Acc.jpg)
d. and 97.6% acc on Validation </br>
![](https://github.com/scarlettgrey/FinalProjectB4ngk1t2021/blob/main/Images/valAcc.jpg)
5. Saving the model using model.save </br>
a. Using model.save(‘./Model’) so it’ll saved as protobuf file with its variables on Model directory
6. Upload the model and DiseaseLabel.csv to Bucket(Google Cloud Platform)
7. Creating Cloud Function so it can be used online using http request
--------------------------------------------------------------------------------------------------------
How to use the model in cloud : 
- Using Python : 
  - https://github.com/scarlettgrey/FinalProjectB4ngk1t2021/blob/main/UseModelOnline.py
