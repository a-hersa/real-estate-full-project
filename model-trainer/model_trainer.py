import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


if __name__=='__main__':
    obj=DataIngestion('venta')
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    data_transformation = DataTransformation('venta')
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)
    model_trainer=ModelTrainer('venta')
    model_trainer.initiate_model_training(train_arr,test_arr)

    obj=DataIngestion('alquiler')
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    data_transformation = DataTransformation('alquiler')
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)
    model_trainer=ModelTrainer('alquiler')
    model_trainer.initiate_model_training(train_arr,test_arr)