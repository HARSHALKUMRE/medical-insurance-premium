import os, sys
from insurance.exception import InsuranceException
from insurance.logger import logging
from insurance.entity import artifact_entity, config_entity
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler
from sklearn.pipeline import Pipeline

# Missing value imputation
# outlier handling
# imbalanced data handling
# convert categorical data to numerical data


class DataTransformation:
    def __init__(self, data_transformation_config: config_entity.DataTransformationConfig,
    data_ingestion_artifact: artifact_entity.DataIngestionArtifact):
        try:
            logging.info(f"{'=' * 20} Data Transformation {'=' * 20}")
            self.data_transformation_config = data_transformation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise InsuranceException(e, sys)

    
    @classmethod
    def get_data_transformer_object(self,) -> Pipeline: # Create cls class
        try:
            simple_imputer = SimpleImputer(strategy='constant', fill_value=0)
            robust_scaler = RobustScaler()
            pipeline = Pipeline(steps = [
                ('imputer', simple_imputer),
                ('scaler', robust_scaler)
            ])
            return pipeline
        except Exception as e:
            raise InsuranceException(e, sys)


    def initiate_data_transformation(self,) -> artifact_entity.DataTransformationArtifact:
        try:
            pass
        except Exception as e:
            raise InsuranceException(e, sys)