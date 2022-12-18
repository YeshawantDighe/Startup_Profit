import pickle
import json
import config
import numpy as np

class StartupProfit():
    
    def __init__(self, user_data):
        self.model_file_path = config.MODEL_FILE_PATH
        self.user_data = user_data

    def load_saved_data(self):
        with open(self.model_file_path, "rb") as f:
            self.model = pickle.load(f)

        with open(config.PROJECT_DATA_FILE_PATH, "r") as f:
            self.proj_data = json.load(f)

    def get_predicted_profit(self):

        self.load_saved_data()


        State = "State_"+self.user_data["State"]

        State_index = self.proj_data["Columns"] == State

        col_count = len(self.proj_data["Columns"])
        test_array = np.zeros(col_count)
        test_array[0] = eval(self.user_data["R&D Spend"])
        test_array[1] = eval(self.user_data["Administration"])
        test_array[2] = eval(self.user_data["Marketing Spend"])
        test_array[State_index] = 1
        print(test_array)
        Profit_Prediction = np.around(self.model.predict([test_array])[0],2)
        print("Predicted Profit :", Profit_Prediction)

        return Profit_Prediction

if __name__ =="__main__":
    ins = StartupProfit()
    ins