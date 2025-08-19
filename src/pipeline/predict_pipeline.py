import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features: pd.DataFrame):
        try:
            # Handle missing/None values before transformation
            features = features.fillna("Unknown")  

            model_path = 'artifacts/model.pkl'
            preprocessor_path = 'artifacts/preprocessor.pkl'

            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            # Debug: check incoming features
            print("\n[DEBUG] Features before transform:\n", features)

            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys) 


class CustomData:
    def __init__(
        self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int
    ):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender or "Unknown"],
                "race_ethnicity": [self.race_ethnicity or "Unknown"],
                "parental_level_of_education": [self.parental_level_of_education or "Unknown"],
                "lunch": [self.lunch or "Unknown"],
                "test_preparation_course": [self.test_preparation_course or "Unknown"],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score]
            }

            df = pd.DataFrame(custom_data_input_dict)

            # Debug: check DataFrame before returning
            print("\n[DEBUG] CustomData as DataFrame:\n", df)

            return df
        
        except Exception as e:
            raise CustomException(e,sys)
