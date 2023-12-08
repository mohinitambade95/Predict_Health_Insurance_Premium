Project to predict Health Insurance Premium
1. Initializ a git repository
2. Create readme.md and .gitignore file.
3. Add linsense
4. Create init_setup.sh
5. execute init_setup.sh commad - bash init_setup.sh (create project env)
6. Create template.py (Python script to create project structure)
8. Create setup.py file
7. To install local packages -- pip install . or include -e . in the requirements.txt file or install local packages from setup.py -- python setup.py install

Project structure
Components of pipelines :
1. data ingestion
2. EDA
3. Feature engineering
4. Model building
5. evaluation

Pipelines (Collection of components):
1. Training Pipeline
2. Prediction Pipeline

Other files:
1. Logger file (to log every information about execution)
2. exception file
3. Utils file
4. setup.py -- to install local packages
5. requirement.txt

Other folders
1. Create .github folder under root directory.
   .github --> workflow -> main.yaml file  (Used for CI/CD pipeline), .gitkeep file (allow us to push empty folder to git )
2. Notebooks
3. src / projectName 
         / Components [dataingestion.py preprocessing.py, modeltraining.py]
         / Pipelines [training.py, prediction.py]
         / exeception.py
         / logger.py
         / utils.
4. create __init__.py file inside each folder (src,projectName,components,pipeline) to make it a local package




                    