import streamlit as st

def find_largest(num1, num2, num3):
    # Check if any of the numbers are equal
    if num1 == num2 == num3:
        return "All numbers are equal"
    elif num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

def main():
    st.title("Find the largest number")

    # User input for three numbers
    num1 = st.number_input("Enter the first number")
    num2 = st.number_input("Enter the second number")
    num3 = st.number_input("Enter the third number")

    # Button to find the largest number
    if st.button("Find Largest Number"):
        if num1 or num2 or num3:
            largest = find_largest(num1, num2, num3)
            st.write(f"The largest number is: {largest}")
        else:
            st.write("Please enter at least one number")

if __name__ == "__main__":
    main()
