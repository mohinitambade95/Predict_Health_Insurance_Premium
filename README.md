<h1> Health Insurance Premium Prediction </h1>
<h2> Problem Statement</h2>
The Insurance Premium prediction project aims to leverage machine learning algorithms to predict the health insurance premium. 
The goal of this project is to give people an estimate of how much they need based on their individual health situation. After that, customers can work with any health insurance carrier and its plans and perks while keeping the projected cost from our study in mind. This can assist a person in concentrating on the health side of an insurance policy rather than the ineffective part.


<h2> Project Demo Link </h2>
Checkout the project demo at https://drive.google.com/file/d/1HNTcZ-eTq_2GpukDmht6rBxv1YG6vHkO/view?usp=sharing
<h2> Deployed App Link </h2>
Access the deployed application at
https://ja3mktausj.ap-south-1.awsapprunner.com
<h2> Data </h2>
Get the data from https://www.kaggle.com/datasets/noordeen/insurance-premium-prediction
<h2> Project Flow </h2>

![architechture](https://github.com/mohinitambade95/Predict_Health_Insurance_Premium/assets/32614334/9dea3a93-f786-44c4-8735-6789da54e438)

<h2> Programming Language used </h2>
Python 3.8
<h2> Python Libraries and tools Used </h2>
GIT numpy pandas
<h2> Project Setup </h2>
<h4> Clone the Project <h4>
  
  ```
  git clone https://github.com/mohinitambade95/Predict_Health_Insurance_Premium.git
  ```
<h4> Create conda environment </h4>

  ```
  conda create -n env_name python=3.8
  ```
<h4> Activate the conda environment </h4>

  ```
  conda activate env_name
  ```
<h4> Intstall Dependencies</h4>

  ```
  pip install -r requirements.txt
  ```
<h4> Execute training pipeline </h4>

  ```
  python training_pipeline.py
  ```

<h4> Run the application </h4>

  ```
  python app.py
  ```
<h4> Visualize the metrics for different experiments using mlflow </h4>

  ```
  mlflow ui
  ```

<h2> CI/CD Pipeline </h2>

 The CI/CD pipeline is created using github actions to automate the project deployment.

<h2> AWS Deployment </h2>
Delpoyed the application on AWS App Runner to ensure scalability and accessibility of application.
