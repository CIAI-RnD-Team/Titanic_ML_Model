#from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from classification_model.processing import preprocessors as pp
from classification_model.config import config
from classification_model.processing import features

titanic_pipe = Pipeline(
    [
        ('categorical_imputer',
         pp.CategoricalImputer(variables=config.CATEGORICAL_VARS)),

        ('missing indicator',
            pp.MissingIndicator(variables=config.NUMERICAL_VARS)),

        ('numerical_inputer',
            pp.NumericalImputer(variables=config.NUMERICAL_VARS)),
         
        ('cabin_variable',
            pp.ExtractFirstLetter(
                variables=config.CABIN)),
         
        ('rare_label_encoder',
            pp.RareLabelCategoricalEncoder(
                tol=0.05,
                variables=config.CATEGORICAL_VARS)),
        ('categorical_encoder',
            pp.CategoricalEncoder(variables=config.CATEGORICAL_VARS)),
        ('drop_features',
            pp.DropUnecessaryFeatures(variables_to_drop=config.DROP_FEATURES)),     
        ('scaler', StandardScaler()),
        ('Random_Forest_Model', RandomForestClassifier(n_estimators=100))
    ]
)