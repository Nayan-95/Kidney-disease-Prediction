 
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache_data()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(age, bp, pc, htn, appet, dm, pe):   
 
    # Pre-processing user input    
    if htn == "no":
        htn = 0
    else:
        htn = 1
 
    if dm == "no":
        dm = 0
    else:
        dm = 1
    if appet == "good":
        appet = 0
    else:
        appet = 1
    if pc == "normal":
        pc = 1
    else:
        pc = 0
    if pe == "yes":
        pe = 1
    else:
        pe = 0
 
      
    # Making predictions 
    prediction = classifier.predict( 
        [[age, bp, pc, htn, appet, dm, pe]])
     
    if prediction == 0:
        pred = 'Kidney Disease not detected'
    else:
        pred = 'Kidny Disease found'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:cyan;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Kidney Disease Prediction</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    htn = st.selectbox('Hypertension',("no","yes"))
    dm = st.selectbox('Diabetes Mellitus',("no","yes")) 
    age = st.number_input("Age") 
    bp = st.number_input("BP") 
    pc = st.selectbox("Pus cell",("normal","abnormal"))
    pe = st.selectbox("Pedal edema",("yes","no"))
    appet = st.selectbox("APPET",("good","poor"))
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(age, bp, pc, htn, appet, dm, pe) 
        st.success('Report Results: {}'.format(result))
        
     
if __name__=='__main__': 
    main()
