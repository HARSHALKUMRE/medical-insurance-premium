import os, sys 
from insurance.exception import InsuranceException
from insurance.logger import logging
from insurance.entity import config_entity, artifact_entity
from insurance.utils import load_object, save_object
from insurance.predictor import ModelResolver


class ModelPusher:
    def __init__(self, model_pusher_config: config_entity.ModelPusherConfig,
                 data_transformation_artifact: artifact_entity.DataTransformationArtifact,
                 model_trainer_artifact: artifact_entity.ModelTrainerArtifact):
        try:
            logging.info(f"{'=' * 20} Model Pusher log started. {'=' * 20}")
            self.model_pusher_config = model_pusher_config
            self.data_transformation_artifact = data_transformation_artifact
            self.model_trainer_artifact = model_trainer_artifact
            self.model_resolver = ModelResolver(model_registry=self.model_pusher_config.saved_model_dir)
        except Exception as e:
            raise InsuranceException(e, sys)


    def initiate_model_pusher(self,) -> artifact_entity.ModelPusherArtifact:
        try:
            # load object
            logging.info(f"Loading transformer model and target encoder")
            transformer = load_object(file_path = self.data_transformation_artifact.transform_object_path)
            model = load_object(file_path = self.model_trainer_artifact.model_path)
            target_encoder = load_object(file_path = self.data_transformation_artifact.target_encoder_path)

            # Model Pusher dir
            logging.info(f"Saving model into the model pusher directory")
            save_object(file_path = self.model_pusher_config.pusher_transformer_path, obj = transformer)
            save_object(file_path = self.model_pusher_config.pusher_model_path, obj = model)
            save_object(file_path = self.model_pusher_config.pusher_target_encoder_path, obj = target_encoder)

            # saved model dir
            logging.info(f"Saving model in saved model directory")
            transformer_path = self.model_resolver.get_latest_save_transformer_path()
            model_path = self.model_resolver.get_latest_save_model_path()
            target_encoder_path = self.model_resolver.get_latest_save_target_encoder_path()

            save_object(file_path = transformer_path, obj = transformer)
            save_object(file_path = model_path, obj = model)
            save_object(file_path = target_encoder_path, obj = target_encoder)

            model_pusher_artifact = artifact_entity.ModelPusherArtifact(pusher_model_dir=self.model_pusher_config.pusher_model_dir,
            saved_model_dir=self.model_pusher_config.saved_model_dir)
            logging.info(f"Model Pusher artifact: {model_pusher_artifact}")
            return model_pusher_artifact

        except Exception as e:
            raise InsuranceException(e, sys)

