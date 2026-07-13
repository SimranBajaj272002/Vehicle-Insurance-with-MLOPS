# from src.logger import logging

# logging.debug("Starting the Vehicle Insurance Prediction with MLOps demo script.")

# --------------------------------------------------------------------------------

# # below code is to check the exception config
# from src.logger import logging
# from src.exception import MyException
# import sys

# try:
#     a = 1+'Z'
# except Exception as e:
#     logging.info(e)
#     raise MyException(e, sys) from e



# -------------------------run pipeline-----------------------------------
from src.pipline.training_pipeline import TrainPipeline

pipline = TrainPipeline()
pipline.run_pipeline()