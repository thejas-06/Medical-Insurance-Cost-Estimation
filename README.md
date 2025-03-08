# Medical-Insurance-Cost-Estimation
    
Medical Insurance Cost Estimation:<br>
This project is a web application that predicts medical insurance costs based on user inputs such as age, BMI, number of children, gender, smoking status, and region. The application uses a machine learning model trained on an insurance dataset and provides a user-friendly interface using Streamlit.<br>
<br>Project Overview:
<br>Dataset:<br>
The application uses the insurance.csv dataset which contains information about individuals, including features like age, sex, BMI, number of children, smoking status, region, and the associated insurance charges.

Model:<br>
A Linear Regression model is used to estimate insurance costs. The dataset is preprocessed (with categorical variables encoded), the model is trained, evaluated, and then saved to disk.

Web Application:<br>
The user interface is built using Streamlit. Users can input their personal details via the sidebar, and the app will display the predicted insurance cost.<br>


Setup Instructions:<br>
1.Create a Virtual Environment:

➡️python -m venv env

2.Activate the Virtual Environment:

➡️source env/bin/activate  # for Linux/macOS or

➡️.\env\Scripts\activate for Windows

3.Install Dependencies:

➡️pip install -r requirements.txt

Contributing:<br>
Contributions are welcome! If you have ideas for improvements or additional features, feel free to fork the repository and submit a pull request.<br>
