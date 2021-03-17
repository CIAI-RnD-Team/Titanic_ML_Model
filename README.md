# Titanic_ML_Model
This repository contains all the necessary files to train, test and deploy the ML model. We will be using titanic dataset.
The aim is to build a CI/CD pipeline for our Application pipeline and ML API, and automate the process of training and deploying.

1. **.circleci**
   - **config.yml** -  contains all the jobs and the workflow of the jobs that has to be executed by the CircleCI.
2. **packages**
   - **classification_model**
      - **classification_model**
        - **config**
           - **config.py** - contains all the paths and parameters used for training the model.
           - **logging_config.py** - to log all the steps and messages while working witht model.
        - **data_management.py** - loading your dataset, saving your pipeline file, loading your saved pipeline file and removing the older versions of pipeline file.
        - **errors.py** - checking for errors during validation.
        - **features.py** - to apply feature engineering steps on the features.
        - **preprocessors.py** - the preprocessing steps used in training of the pipeline. They follow the scikit learn pipeline template, fit and transform.
        - **validation.py** - checking inputs if they contain any unprocessable data.
        - **init.py** - configuring logger to use in package and versioning the model.
        - **pipeline.py** - using the scikit-learn pipeline, the model is trained on different transformation steps and one classification algorithm.
        - **train_pipeline.py** - the file where the magic happens. Leveraging the config, preprocessors and the pipeline we generate a pickle file that can be used later to predict data.
        - **predict.py** - once you have trained and generated your pickle file, you predict on new data.
        - **VERSION** - versioning our ML model.  
      - **tests**
        - **test_predict.py** - to make sure our trained model is bugs and issues free. 
      - **MANIFEST.in** - consists of commands for the setuptools, to add or remove files from the source distribution.
      - **requirements.txt** - required python packages and their versions.
      - **setup.py** - is used to install the package and its distribution python modules. 
      - **tox.ini** - is a generic virtualenv management and test command line tool.
   - **ml_api**
     - **api** 
       - **init.py** - versioning the api.
       - **app.py** - creating an api instance for our application.
       - **config.py** - contains configurational parameters for launching/creating an api instance.
       - **controller.py** - creating endpoints for our api.
       - **validation.py** - using the input schema, checking for invalid prediction input values.
     - **tests**
       - **test_differential.py** - this test compares the results of previous tests with present models results.
       - **capture_model_predictions.py** - capturing test data predictions, to be used with differential test.
       - **conftest.py** - is used to load in external plugins and modules, pytest will load in these modules and make them available for its tests.
       - **test_controller.py** - checking our api endpoints for bugs and issues.
       - **test_validation.py** - checking if our input schema in validation is looking for erroneous input prediction data.
       - **diff_test_requirements.txt** - required python packages for test_differential.
       - **requirements.txt** - required python packages for the api.
       - **run.py** - building our api.
       - **run.sh** - a single file to run a few lines of shell commands to deploy a web server gateway for our api.
       - **VERSION** - api version.
3. **scripts**
   - **fetch_kaggle_dataset.sh** - shell file to extract and save our titanic dataset.
   - **input_test.json** - input prediction data.
   - **publish_model.sh** - publish our model to Gemfury, a private repository.
4. **.dockerignore** - tells docker which files to ignore during while generating a build context.
5. **.gitignore** - tell git which files to ignore.
6. **Dockerfile** - contains all the commands required to generate a docker image.
7. **Makefile** - contains commands required to build and push our application on heroku.
8. **Procfile** - building a web gateway server on heroku. 


## Training the model
It's quiet simple to train the model, just run the command-
``` 
python packages/classification_model/classification_model/train_pipeline.py
```
Make sure that there datasets present in the datasets directory.
This command will generate a pickle file which can be used to predict.


## Predicting data
Now that you have trained and generated a pickle file, it time to predict.
In a python file,
```
from classification_model.predict import make_prediction
from classification_model.processing.data_management import load_dataset

test_data = load_dataset(file_name='test.csv') # here you can give your own csv input file for predictions.
predictions = make_prediction(input_data=test_data)
print(predictions)
```
predictions vairable will contain a dictonary with the predictions array and model version.


## Running test on ML model
We have got our ML model, we are gonna run test on training and predict.
You need to install pytest python module.
```
pip install pytest
```
To run the tests, run this command in command line- 
```
pytest packages/classification_model/tests
```
If all the tests have passed, you will see something like this 
![test_predict](https://user-images.githubusercontent.com/70632625/111276500-6638a180-865d-11eb-9330-52033daa6622.PNG)


## Building the API
To run our api,
```
python packages/ml_api/run.py
```
This will generate a ip-address, copy the ip-address and paste it in you web browser-
```
generated_ip_address/health
```
this should show you the message "health status ok". 


## Testing API
To run tests on your api,
```
pytest packages/ml_api/tests
```
Note: while running these tests on local machine, the differential test will fail. This is due to differential test is made to run on CircleCI, not locally.


## Setting up CircleCI, Gemfury and Heroku accounts
1. **CircleCI** - Login to CircleCI using GitHub account> setup project> commit and run.Everytime you create a pull request in your repository, the jobs will get executed.
2. **Gemfury** - You can login with your GitHub account or a email account.
3. **Heroku** - Login using GitHub account> New app> create a app name and select region


## Setting up environmental variables in CircleCI
To set up environment vairables for CircleCI, select your project> project settings> environment variables.
We need to setup a total of 6 environmental variables.
   1. **HEROKU_API_KEY** - click on your heroku profile icon, and go to settings. Scroll down, and you will find the API key.
   2. **HEROKU_APP_NAME** - Your Heroku app name.
   3. **HEROKU_EMAIL** - email used to login to heroku.
   4. **KAGGLE_KEY** - go to your kaggle account> click on your profile> settings> scroll down to find API key.
   5. **KAGGLE_USERNAME** - your kaggle username.
   6. **PIP_EXTRA_INDEX_URL** - go to your gemfury account> tokens> full access token.

Now everytime you create a pull request, the workflow in CircleCI will get executed and the model will be deployed on Heroku.

You can check if your app has been deployed or not by checking https://YOUR-HEROKU-APP-NAME.herokuapp.com/version or https://YOUR-HEROKU-APP-NAME.herokuapp.com/health/

To get a prediction, open your command line and go to scripts directory and use this command -
```
curl --header "Content-Type: application/json" --request POST --data @input_test.json https://YOUR-HEROKU-APP-NAME.herokuapp.com/v1/predict/classification
```
