import numpy as np
import pickle
import streamlit as st

#loading the model
loaded_model = pickle.load(open('house_price_prediction.sav','rb'))

def house_price_prediction(input_data):

    #changing input data as numpy array
    input_data_numpy = np.asarray(input_data)

    #reshaping the array because if we don't the model thinks we will provide 543 data but we are provided only 1 and so we need to reshape for one instance.
    input_data_numpy_reshape = input_data_numpy.reshape(1,-1)

    prediction1 = loaded_model.predict(input_data_numpy_reshape)
    return f'The price of your house is :{prediction1}'

def main():
    #giving a title to the page
    st.title('House Price Prediction Web App')

    #getting the input data from the user
    											
    # Getting the input data from the user
    area = st.text_input('Area of the house')
    bedrooms = st.text_input('Number of bedrooms')
    bathrooms = st.text_input('Number of bathrooms')
    stories = st.text_input('Number of stories')
    mainroad = st.text_input('Is there a mainroad? (0 or 1)')
    guestroom = st.text_input('Is there a guestroom? (0 or 1)')
    basement = st.text_input('Is there a basement? (0 or 1)')
    hotwaterheating = st.text_input('Is there hot water heating? (0 or 1)')
    airconditioning = st.text_input('Is there air conditioning? (0 or 1)')
    parking = st.text_input('Number of parking spaces')
    prefarea = st.text_input('Is there a preferred area? (0 or 1)')
    furnishingstatus = st.text_input('Furnishing status (unfurnished-0, semi-furnished-1, or furnished-2)')

    #code for prediction
    price = ''

    #creating a button
    if st.button('Predict the price of your house'):
        area = int(area)
        bedrooms = int(bedrooms)
        bathrooms = int(bathrooms)
        stories = int(stories)
        mainroad = int(mainroad)
        guestroom = int(guestroom)
        basement = int(basement)
        hotwaterheating = int(hotwaterheating)
        airconditioning = int(airconditioning)
        parking = int(parking)
        prefarea = int(prefarea)
        furnishingstatus = int(furnishingstatus)
        price = house_price_prediction([area,bedrooms,bathrooms,stories,mainroad,guestroom,basement,hotwaterheating,airconditioning,parking,prefarea,furnishingstatus])

    st.success(price)

if __name__ == '__main__':
    main()