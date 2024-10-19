from flask import Flask, Blueprint, render_template, redirect, url_for, request
from werkzeug.middleware.proxy_fix import ProxyFix
import sys
from argparse import ArgumentParser
from cvd_model import *

appweb = Blueprint('hello', __name__)

@appweb.route('/')
def home():
    return render_template("index.html")

@appweb.route('/send', methods=['POST'])
def send(predict=predict):
    if request.method == 'POST':
        patient_age = request.form['age']
        patient_sex = request.form['gender']
        patient_chest_pain = request.form['chestpain']
        patient_resting_bp = request.form['trestbps']
        patient_sereum_chol = request.form['chol']
        patient_fasting_bs = request.form['fastingbs']
        patient_resting_egg = request.form['restingegg']
        patient_max_heartrate = request.form['maxheartrate']
        patient_exercise_induced_angina = request.form['exerciseindu']
        patient_oldpeak = request.form['oldpeak']
        patient_slope = request.form['slope']
        patient_number_vessels = request.form['vessels']
        patient_thalassemia = request.form['thal']

        if(patient_sex == "male"):
            patient_sex = 1
        else:
            patient_sex = 0

        if(patient_chest_pain == "Typical_Angina"):
            patient_chest_pain = 0;

        elif(patient_chest_pain == "Atypical_Angina"):
            patient_chest_pain = 1;

        elif(patient_chest_pain == "Non--Anginal_Pain"):
            patient_chest_pain = 2;
        else:
            patient_chest_pain = 3;

        if(patient_fasting_bs == "Yes"):
            patient_fasting_bs = 1
        else:
            patient_fasting_bs = 0

        if(patient_resting_egg == "Normal"):
            patient_resting_egg = 0
        elif(patient_resting_egg == "Having ST-T Wave Abnormality"):
            patient_resting_egg = 1
        else:
            patient_resting_egg = 2

        if(patient_exercise_induced_angina == "Yes"):
            patient_exercise_induced_angina = 1
        else:
            patient_exercise_induced_angina = 0

        if(patient_slope == "Upsloping"):
            patient_slope = 0

        elif(patient_slope == "Flat"):
            patient_slope = 1

        else:
            patient_slope = 2

        if(patient_thalassemia == "Normal"):
            patient_thalassemia = 1
        elif(patient_thalassemia == "Fixed Defect"):
            patient_thalassemia = 2
        else:
            patient_thalassemia = 3


        # Accuracy of Model
        model.fit(x_train, y_train) #<-- this line
        acc = model.score(x_train, y_train)

        predict_real = model.predict([[patient_age,patient_sex,patient_chest_pain,
          patient_resting_bp,patient_sereum_chol,
          patient_fasting_bs,patient_resting_egg,
          patient_max_heartrate,patient_exercise_induced_angina,
          patient_oldpeak,patient_slope,patient_number_vessels,
          patient_thalassemia]])

        if(predict_real == [0]):
            predict = "The result returned with " + str(round(acc,2)*100)  + "% accuracy and you have a lower chance of getting heart disease"
        else:
            predict = "The result returned with " + str(round(acc,2)*100) + "% accuracy and you have a higher chance of getting heart disease"


        return render_template('index.html', predict=predict)

    else:
        return render_template('index.html', predict=predict)



@appweb.route('/about')
def about():
    return render_template("about.html")



if __name__ == '__main__':

    # arg parser for the standard anaconda-project options
    parser = ArgumentParser(prog="home",
                            description="Simple Flask Application")
    parser.add_argument('--anaconda-project-host', action='append', default=[],
                        help='Hostname to allow in requests')
    parser.add_argument('--anaconda-project-port', action='store', default=8086, type=int,
                        help='Port to listen on')
    parser.add_argument('--anaconda-project-iframe-hosts',
                        action='append',
                        help='Space-separated hosts which can embed us in an iframe per our Content-Security-Policy')
    parser.add_argument('--anaconda-project-no-browser', action='store_true',
                        default=False,
                        help='Disable opening in a browser')
    parser.add_argument('--anaconda-project-use-xheaders',
                        action='store_true',
                        default=False,
                        help='Trust X-headers from reverse proxy')
    parser.add_argument('--anaconda-project-url-prefix', action='store', default='',
                        help='Prefix in front of urls')
    parser.add_argument('--anaconda-project-address',
                        action='store',
                        #default='0.0.0.0',
                        help='IP address the application should listen on.')

    args = parser.parse_args()

    app = Flask(__name__)
    app.register_blueprint(appweb, url_prefix = args.anaconda_project_url_prefix)

    app.config['PREFERRED_URL_SCHEME'] = 'https'

    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(host=args.anaconda_project_address, port=args.anaconda_project_port)
