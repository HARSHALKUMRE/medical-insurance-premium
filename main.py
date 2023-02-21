from insurance.logger import logging
from insurance.exception import InsuranceException
import os, sys
from insurance.utils import get_collection_as_dataframe
from insurance.entity.config_entity import DataIngestionConfig
from insurance.entity import config_entity
from insurance.component.data_ingestion import DataIngestion

#def test_logger_and_exception():
    #try:
        #logging.info(f"Starting the test_logger_and_exception")
        #result = 3 / 10
        #print(result)
        #logging.info(f"Ending point of the test_logger_and_exception")
    #except Exception as e:
        #logging.debug(str(e))
        #raise InsuranceException(e, sys)


if __name__ == "__main__":
    try:
        #test_logger_and_exception()
        #get_collection_as_dataframe(database_name = "INSURANCE", collection_name = "INSURANCE_PROJECT")
        training_pipeline_config = config_entity.TrainingPipelineConfig()
        data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        print(data_ingestion_config.to_dict())
        data_ingestion = DataIngestion(data_ingestion_config = data_ingestion_config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
    except Exception as e:
        print(e)