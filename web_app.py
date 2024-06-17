import numpy as np
import pickle
import streamlit as st

#loading the model
loaded_model = pickle.load(open('Property_acquisition_cost_predictor.sav','rb'))

def house_price_prediction(input_data):

    #changing input data as numpy array
    input_data_numpy = np.asarray(input_data)

    #reshaping the array because if we don't the model thinks we will provide 543 data but we are provided only 1 and so we need to reshape for one instance.
    input_data_numpy_reshape = input_data_numpy.reshape(1,-1)

    prediction1 = loaded_model.predict(input_data_numpy_reshape)
    return prediction1[0]

def hidden_price_prediction(input_data):
    finalPrice = sum(input_data)
    return finalPrice

def main():
    #giving a title to the page
    st.title('Property Acquition Cost Predictor Web App')

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

    # Initialize session state for price and hiddenPrice
    if 'price' not in st.session_state:
        st.session_state.price = 0
    if 'hiddenPrice' not in st.session_state:
        st.session_state.hiddenPrice = 0

    #creating a button
    if st.button('Predict the price of your house'):
        try:
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
            st.session_state.price = house_price_prediction([area,bedrooms,bathrooms,stories,mainroad,guestroom,basement,hotwaterheating,airconditioning,parking,prefarea,furnishingstatus])
            st.success(f'The price of your house is: {st.session_state.price}')
        except ValueError:
            st.error("Please enter valid numerical values for all inputs.")

    st.divider()

    st.subheader('Hidden Costs while buying the house')
    transferFee = st.text_input(" 1 Society Transfer Fee (Cost that goes to society fund)")
    maintainance = st.text_input(" 2 Maintainance Cost (per year)")
    homeInsurance = st.text_input(" 3 Home Insurance (Basic - 3000, Comprehensive - 5000, Premium - 10000")
    propertyTax = st.text_input(" 4 Property Tax (Enter 20.4 for residential & 34.68 for Commercial)")
    brokerFee = st.text_input(" 5 Brokerage")
    st.text(" 6 Sales Deed (Price * 0.06)")

    hiddenPrice = 0

    if st.button('Calculate the hidden costs'):
        try:
            transferFee = int(transferFee)
            maintainance = int(maintainance)
            homeInsurance = int(homeInsurance)
            st.session_state.price = house_price_prediction([area,bedrooms,bathrooms,stories,mainroad,guestroom,basement,hotwaterheating,airconditioning,parking,prefarea,furnishingstatus])
            salesDeed = st.session_state.price * 0.06
            propertyTax = float(propertyTax)
            propertyTax = float(area) * propertyTax
            brokerFee = int(brokerFee)
            st.session_state.hiddenPrice = hidden_price_prediction([transferFee,maintainance,homeInsurance,salesDeed,propertyTax,brokerFee,st.session_state.price])
            st.success(f'The initial cost of your house: {st.session_state.price}')
            st.success(f'The final cost of your house in a year is: {st.session_state.hiddenPrice}')
        except ValueError:
            st.error("Please enter valid numerical values for all inputs.")
    


if __name__ == '__main__':
    main()
