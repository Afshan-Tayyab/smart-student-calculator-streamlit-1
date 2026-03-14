import streamlit as st

num1 = float(st.number_input("Enter first number: "))
num2 = float(st.number_input("Enter second number: "))

operation = st.text_input("Choose operation (+, -, *, /): ")

if st.button("Calculate"):

    if operation == "+":
        st.write("Result:", num1 + num2)

    elif operation == "-":
        st.write("Result:", num1 - num2)

    elif operation == "*":
        st.write("Result:", num1 * num2)

    elif operation == "/":
        if num2 == 0:
            st.write("Cannot divide by zero")
        else:
            st.write("Result:", num1 / num2)

    else:
        st.write("Invalid operation")