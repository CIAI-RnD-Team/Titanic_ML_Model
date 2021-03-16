# Titanic_ML_Model
This repository contains all the necessary files to train, test and deploy the ML model. We will be using titanic dataset.
The aim is to build a CI/CD pipeline for our Application pipeline and ML API, and automate the process of training and deploying.

1. **.circleci**
   - config.yml -  contains all the jobs and the workflow of the jobs that has to be executed by the CircleCI.
2. **packages**
   - classification_model
      - classification_model
        - config.py - contains all the paths and parameters used for training the model.
        - logging_config.py - to log all the steps and messages while working witht model.
        - data_management.py - loading your dataset, saving your pipeline file, loading your saved pipeline file and removing the older versions of pipeline file.
        - errors.py - checking for errors during validation.
        - features.py - to apply feature engineering steps on the features.
        - preprocessors.py - the preprocessing steps used in training of the pipeline. They follow the scikit learn pipeline template, fit and transform.
        - validation.py - checking inputs if they contain any unprocessable data.
        - init.py - configuring logger to use in package and versioning the model.
        - pipeline.py - using the scikit-learn pipeline, the model is trained on different transformation steps and one classification algorithm.
        - train_pipeline.py - the file where the magic happens. Leveraging the config, preprocessors and the pipeline we generate a pickle file that can be used later to predict data.
        - predict.py - once you have trained and generated your pickle file, you predict on new data.
        - VERSION - versioning our ML model.  
      - tests
        - test_predict.py - to make sure our trained model is bugs and issues free. 
      - MANIFEST.in - consists of commands for the setuptools, to add or remove files from the source distribution.
      - requirements.txt - required python packages and their versions.
      - setup.py - is used to install the package and its distribution python modules. 
      - tox.ini - is a generic virtualenv management and test command line tool.
   - ml_api
     - api 
       - init.py - versioning the api.
       - app.py - creating an api instance for our application.
       - config.py - contains configurational parameters for launching/creating an api instance.
       - controller.py - creating endpoints for our api.
       - validation.py - using the input schema, checking for invalid prediction input values.
     - tests
       - test_differential.py - this test compares the results of previous tests with present models results.
       - capture_model_predictions.py - capturing test data predictions, to be used with differential test.
       - conftest.py - is used to load in external plugins and modules, pytest will load in these modules and make them available for its tests.
       - test_controller.py - checking our api endpoints for bugs and issues.
       - test_validation.py - checking if our input schema in validation is looking for erroneous input prediction data.
       - diff_test_requirements.txt - required python packages for test_differential.
       - requirements.txt - required python packages for the api.
       - run.py - building our api.
       - run.sh - a single file to run a few lines of shell commands to deploy a web server gateway for our api.
       - VERSION - api version.
   - scripts
     - fetch_kaggle_dataset.sh - shell file to extract and save our titanic dataset.
     - input_test.json - input prediction data.
     - publish_model.sh - publish our model to Gemfury, a private repository.
   - .dockerignore - tells docker which files to ignore during while generating a build context.
   - .gitignore - tell git which files to ignore.
   - Dockerfile - contains all the commands required to generate a docker image.
   - Makefile - contains commands required to build and push our application on heroku.
   - Procfile - building a web gateway server on heroku. 


       -  
