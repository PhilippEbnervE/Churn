import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
# Streamlit UI
st.title('Customer Churn Prediction App')
st.write('Enter the following information to predict customer churn.')

# loading the first trained model
pickle_in = open('churn_model_5.pkl', 'rb') 
classifier = pickle.load(pickle_in)

scaler_file_path = 'scaler_churn_5.pkl'  

@st.cache_data()

# defining the function which will make the prediction using the data which the user inputs 
def prediction(Call_Failure, Complains, Subscription_Length, Frequency_of_use, Frequency_of_SMS, Distinct_Called_Numbers, Age, dtype='object'):   


    # Making predictions 
    prediction = classifier.predict( 
        [[Call_Failure, Complains, Subscription_Length, Frequency_of_use, Frequency_of_SMS, Distinct_Called_Numbers, Age]])
     
    if prediction == 0:
        pred = 'Not Churn'
    else:
        pred = 'Churn'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
   
    """
     
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    
    Call_Failure = st.number_input("Number of Call Failures")
    Complains = st.radio('Complaint Made by Customer?', ['Yes', 'No'])
    Subscription_Length = st.number_input("Customer Subscription Length in years")
    Frequency_of_use = st.number_input("Number of Phone Calls Made by Customer")
    Frequency_of_SMS = st.number_input("Number of SMS sent by Customer")
    Distinct_Called_Numbers = st.number_input("Number of Distinct Numbers Called by Customer")
    Age = st.number_input("Age of Customer")
    result =""

    # Convert categorical values to numerical
    Complains = 1 if Complains == 'Yes' else 0

    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict Churn"): 
        result = prediction(Call_Failure, Complains, Subscription_Length, Frequency_of_use, Frequency_of_SMS, Distinct_Called_Numbers, Age) 
        st.success('The customer will {}'.format(result))

if __name__=='__main__': 
    main()