import streamlit as st
import re

st.set_page_config(page_title="Password strength Checker", page_icon="🔒")

st.title("🔐Password strength Checker")
st.markdown(""" ## welcome to the ultimate password strength checker!
            use this simple tool to check the strength of your password and get suggestic
            we will give you helpful tips to create your Strong password 🔑 """) 

password = st.text_input("Enter your password", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌Your password should be at least 8 characters long")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌Your password should contain both upper and lower case letters")

    if re.search(r"\d", password):
            score += 1
    else:
            feedback.append("❌Your password should contain at least one number")

    if re.search(r"[!@#$%&*]", password): 
        score += 1
    else:
        feedback.append("❌Your password should contain at least one special character (!@#$%&*)")
    if score == 4:
        st.success("✅ Your password is strong")
    elif score == 3:
        feedback.append("⚠️ Your password is medium strength it could be stronger")
    else:
        feedback.append("❌ Your password is weak please make it stronger")

    if feedback:
        st.markdown("### improve your password :")
        for tip in feedback:
            st.write(tip)

else:
     st.info("please Enter your password to get started") 


           


            



