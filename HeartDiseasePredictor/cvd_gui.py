import tkinter as tk
from cvd_model import *


class CVD_GUI:
    def __init__(self):

        # Create the main window.
        self.main_window = tk.Tk()
        self.main_window.title("Heart Disease Predictor")

        # Create two frames to group widgets.
        self.one_frame = tk.Frame()
        self.two_frame = tk.Frame()
        self.three_frame = tk.Frame()
        self.four_frame = tk.Frame()
        self.five_frame = tk.Frame()
        self.six_frame = tk.Frame()
        self.seven_frame = tk.Frame()
        self.eight_frame = tk.Frame()
        self.nine_frame = tk.Frame()
        self.ten_frame = tk.Frame()
        self.eleven_frame = tk.Frame()
        self.twelve_frame = tk.Frame()
        self.thirteen_frame = tk.Frame()
        self.fourteen_frame = tk.Frame()
        self.fifteen_frame = tk.Frame()

        # Create the widgets for one frame. (title display)
        self.title_label = tk.Label(self.one_frame, text='HEART DISEASE PREDICTOR',fg="Blue", font=("Helvetica", 18))
        self.title_label.pack()


        # Create the widgets for two frame. (age input)
        self.age_label = tk.Label(self.two_frame, text='Age:')
        self.age_entry = tk.Entry(self.two_frame, bg="white", fg="black", width = 10)
        #self.age_entry.insert(0,'50')
        self.age_label.pack(side='left')
        self.age_entry.pack(side='left')



        # Create the widgets for three frame. (sex/gender input)
        self.sex_label = tk.Label(self.three_frame, text='Sex:')
        self.click_sex_var = tk.StringVar()
        self.click_sex_var.set("Male")
        self.sex_inp = tk.OptionMenu(self.three_frame,self.click_sex_var, "Male", "Female")
        self.sex_label.pack(side='left')
        self.sex_inp.pack(side='left')


        # Create the widgets for four frame. (chest pain input)
        self.cp_label = tk.Label(self.four_frame, text='Chest Pain:')
        self.click_cp_var = tk.StringVar()
        self.click_cp_var.set("Typical Angina")
        self.cp_inp = tk.OptionMenu(self.four_frame, self.click_cp_var, "Typical Angina", "Atypical Angina", "Non--Anginal Pain", "Asymptotic")
        self.cp_label.pack(side='left')
        self.cp_inp.pack(side='left')

        # Create the widgets for five frame. (trestbp (resting blood pressure)input)
        self.trestbp_label = tk.Label(self.five_frame, text='Resting Blood Pressure:')
        self.trestbp_entry = tk.Entry(self.five_frame, bg="white", fg="black")
        #self.trestbp_entry.insert(0,'150')
        self.trestbp_label.pack(side='left')
        self.trestbp_entry.pack(side='left')


        # Create the widgets for six frame. (serum cholesterol  input)
        self.chol_label = tk.Label(self.six_frame, text='Serum cholesterol:')
        self.chol_entry = tk.Entry(self.six_frame, bg="white", fg="black")
        #self.chol_entry.insert(0,250)
        self.chol_label.pack(side='left')
        self.chol_entry.pack(side='left')

        # Create the widgets for seven frame. (fasting blood sugar)  input)
        self.fbs_label = tk.Label(self.seven_frame, text='Fasting blood sugar (>120 mg/dl):')
        self.click_fbs_var = tk.StringVar()
        self.click_fbs_var.set("No")
        self.fbs_inp = tk.OptionMenu(self.seven_frame, self.click_fbs_var, "No", "Yes")
        self.fbs_label.pack(side='left')
        self.fbs_inp.pack(side='left')

        # Create the widgets for eight frame. (resting ecg)  input)
        self.recg_label = tk.Label(self.eight_frame, text='Resting ECG results:')
        self.click_recg_var = tk.StringVar()
        self.click_recg_var.set("Normal")
        self.recg_inp = tk.OptionMenu(self.eight_frame, self.click_recg_var,"Normal", "Having ST-T wave abnormality", "left ventricular hyperthrophy")
        self.recg_label.pack(side='left')
        self.recg_inp.pack(side='left')

        # Create the widgets for nine frame. (thalach -maximum heart rate achieved input)
        self.thalach_label = tk.Label(self.nine_frame, text='Max heart rate achieved:')
        self.thalach_entry = tk.Entry(self.nine_frame, bg="white", fg="black")
        #self.thalach_entry.insert(0,'150')
        self.thalach_label.pack(side='left')
        self.thalach_entry.pack(side='left')


        # Create the widgets for ten frame. (exang -exercise indiced angina  input)
        self.exang_label = tk.Label(self.ten_frame, text='Exercise induced angina:')
        self.click_exang_var = tk.StringVar()
        self.click_exang_var.set("No")
        self.exang_inp = tk.OptionMenu(self.ten_frame, self.click_exang_var,"Yes", "No")
        self.exang_label.pack(side='left')
        self.exang_inp.pack(side='left')


        #Create the widgets for eleven frame= oldpeak = ST depression induced by exercise relative to rest
        self.oldpeak_label = tk.Label(self.eleven_frame, text='ST depression:')
        self.oldpeak_entry = tk.Entry(self.eleven_frame, bg="white", fg="black")
        #self.oldpeak_entry.insert(0,'4.0')
        self.oldpeak_label.pack(side='left')
        self.oldpeak_entry.pack(side='left')


        #Create the widgets for twelve frame = slope - the slope of the peak exercise ST segment
        self.slope_label = tk.Label(self.twelve_frame, text='Slope of peak exercise ST segment:')
        self.click_slope_var = tk.StringVar()
        self.click_slope_var.set("Upsloping")
        self.slope_inp = tk.OptionMenu(self.twelve_frame, self.click_slope_var, "Upsloping", "Flat", "Downsloping")
        self.slope_label.pack(side='left')
        self.slope_inp.pack(side='left')

        #Create the widgets for thirteen frame =ca: number of major vessels (0-3) colored by flouroscopy
        self.ca_label = tk.Label(self.thirteen_frame, text='Major vessels colored by flouroscopy:')
        self.click_ca_var = tk.StringVar()
        self.click_ca_var.set(0)
        self.ca_inp = tk.OptionMenu(self.thirteen_frame, self.click_ca_var, 0,1,2,3)
        self.ca_label.pack(side='left')
        self.ca_inp.pack(side='left')


        #Create the widgets for fourteen frame = thal: 3 = normal; 6 = fixed defect; 7 = reversable defect
        self.thal_label = tk.Label(self.fourteen_frame, text='Thalassemia:')
        self.click_thal_var = tk.StringVar()
        self.click_thal_var.set("Normal")
        self.thal_inp = tk.OptionMenu(self.fourteen_frame, self.click_thal_var,"Normal","Fixed Defect", "Reversible Defect")
        self.thal_label.pack(side='left')
        self.thal_inp.pack(side='left')

        #Create the widgets for fifteen frame = hd (prediction of heart disease)
        self.hd_predict_ta = tk.Text(self.fifteen_frame,height = 10, width = 25,bg= 'light blue')

        #Create predict button and quit button
        self.btn_predict = tk.Button(self.fifteen_frame, text='Predict Heart Disease', command=self.predict_hd)
        self.btn_quit = tk.Button(self.fifteen_frame, text='Quit', command=self.main_window.destroy)


        self.hd_predict_ta.pack(side='left')
        self.btn_predict.pack()
        self.btn_quit.pack()

        # Pack the frames.
        self.one_frame.pack()
        self.two_frame.pack()
        self.three_frame.pack()
        self.four_frame.pack()
        self.five_frame.pack()
        self.six_frame.pack()
        self.seven_frame.pack()
        self.eight_frame.pack()
        self.nine_frame.pack()
        self.ten_frame.pack()
        self.eleven_frame.pack()
        self.twelve_frame.pack()
        self.thirteen_frame.pack()
        self.fourteen_frame.pack()
        self.fifteen_frame.pack()


        # Enter the tkinter main loop.
        tk.mainloop()

    def predict_hd(self):
        result_string = ""

        self.hd_predict_ta.delete(0.0, tk.END)
        patient_age = self.age_entry.get()
        patient_sex = self.click_sex_var.get()
        if(patient_sex == "Male"):
            patient_sex = 1
        else:
            patient_sex = 0

        patient_chest_pain = self.click_cp_var.get()
        if(patient_chest_pain == "Typical Angina"):
            patient_chest_pain = 0;
        elif(patient_chest_pain == "Atypical Angina"):
            patient_chest_pain = 1;
        elif(patient_chest_pain == "Non--Anginal Pain"):
            patient_chest_pain = 2;
        else:
            patient_chest_pain = 3;

        patient_resting_bp = self.trestbp_entry.get()
        patient_sereum_chol = self.chol_entry.get()
        patient_fasting_bs = self.click_fbs_var.get()
        if(patient_fasting_bs == "Yes"):
            patient_fasting_bs = 1
        else:
            patient_fasting_bs = 0


        patient_resting_ecg = self.click_recg_var.get()
        if(patient_resting_ecg == "Normal"):
            patient_resting_ecg = 0
        elif(patient_resting_ecg == "Having ST-T wave abnormality"):
            patient_resting_ecg = 1
        else:
            patient_resting_ecg = 2

        patient_max_heartrate = self.thalach_entry.get()
        patient_exercise_induced_angina = self.click_exang_var.get()
        if(patient_exercise_induced_angina == "Yes"):
            patient_exercise_induced_angina = 1
        else:
            patient_exercise_induced_angina = 0

        patient_oldpeak = self.oldpeak_entry.get()
        patient_slope = self.click_slope_var.get()
        if(patient_slope == "Upsloping"):
            patient_slope = 0
        elif(patient_slope == "Flat"):
            patient_slope = 1
        else:
            patient_slope = 2

        patient_number_vessels = self.click_ca_var.get()
        #assuming 1 = normal, 2 = fixed and 3 = reversible defect
        patient_thalassemia = self.click_thal_var.get()
        if(patient_thalassemia == "Normal"):
            patient_thalassemia = 1
        elif(patient_thalassemia == "Fixed Defect"):
            patient_thalassemia = 2
        else:
            patient_thalassemia = 3

        result_string += "===Patient Diagnosis=== \n"
        patient_info = (patient_age,patient_sex,patient_chest_pain, patient_resting_bp,patient_sereum_chol,\
                         patient_fasting_bs,patient_resting_ecg,\
                         patient_max_heartrate, patient_exercise_induced_angina,\
                         patient_oldpeak,patient_slope,patient_number_vessels, patient_thalassemia)


        hd_prediction =  best_model.predict([patient_info])
        disp_string = ("This prediction has an accuracy of:", str(model_accuracy))

        result = hd_prediction

        if(hd_prediction == [0]):
            result_string = (disp_string, '\n', "0 - You have lower risk of heart disease")
        else:
            result_string = (disp_string, '\n'+ "1 - You have higher risk of heart disease, please consult your GP soon")
        self.hd_predict_ta.insert('1.0',result_string)

        #Predicted:  1 Actual:  1 Data:  (16, 0, 1, 14, 74, 0, 1, 61, 0, 11, 2, 0, 2)
        #Predicted:  0 Actual:  0 Data:  (26, 0, 0, 34, 87, 0, 0, 56, 0, 25, 1, 2, 3)



my_cvd_GUI = CVD_GUI()

