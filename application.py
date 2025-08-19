from flask import Flask, render_template, request
import numpy as np
import pandas as pd

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        # Use "Unknown" as fallback if field is empty/None
        data = CustomData(
            gender=request.form.get('gender') or "Unknown",
            race_ethnicity=request.form.get('race_ethnicity') or "Unknown",
            parental_level_of_education=request.form.get('parental_level_of_education') or "Unknown",
            lunch=request.form.get('lunch') or "Unknown",
            test_preparation_course=request.form.get('test_preparation_course') or "Unknown",
            reading_score=float(request.form.get('reading_score') or 0),
            writing_score=float(request.form.get('writing_score') or 0),
        )

        pred_df = data.get_data_as_data_frame()
        print("\n[DEBUG] DataFrame passed to model:\n", pred_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        return render_template('home.html', results=results[0])


if __name__ == '__main__':
    app.run(host="0.0.0.0")
