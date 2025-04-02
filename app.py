import streamlit as st
from textcase import case, convert

st.header("Welcome to Case Conversion Service")
userInput=st.text_area("Enter your text here for Case Conversion")
caseDescription = {
    "CaseCase": "Converts the first letter of the first word to uppercase and the rest to lowercase (similar to Capitalize).",
    "UpperCase": "Converts all the characters to uppercase.",
    "LowerCase": "Converts all the characters to lowercase.",
    "TitleCase": "Converts the first letter of each word to uppercase.",
    "CamelCase": "Converts the text into camelCase (no spaces, first word lowercase).",
    "PascalCase": "Converts the text into PascalCase (no spaces, each word starts with uppercase).",
    "KebabCase": "Converts the text into kebab-case (hyphen-separated lowercase words).",
    "SnakeCase": "Converts the text into snake_case (underscore-separated lowercase words).",
    "SentenceCase": "Converts the text into sentence case (first letter of the first word capitalized, the rest lowercase).",
    "ConstantCase": "Converts the text into CONSTANT_CASE (uppercase with underscores)."
}

userChoice=st.selectbox("Select the Desire Case for Conversion",sorted(["---","CaseCase","UpperCase","LowerCase","TitleCase","CamelCase","PascalCase","KebabCase","SnakeCase","SentenceCase","ConstantCase"]))
if userChoice!="---":
    st.write({"Description: ":caseDescription.get(userChoice)})
button=st.html("<button style=background-color:blue;aligin-items:center;color:white;>Convert the Case</button>")
if button:
    if userChoice=="---":
        st.info("Please Select any Desire case for Conversion")
    else:
        userChoiceFunction={
            "CaseCase":case.Case,
            "UpperCase": case.UPPER,
            "LowerCase": case.LOWER,
            "TitleCase": case.TITLE,
            "CamelCase": case.CAMEL,
            "PascalCase": case.PASCAL,
            "KebabCase": case.KEBAB,
            "SnakeCase": case.SNAKE,
            "SentenceCase": case.SENTENCE,
            "ConstantCase": case.CONSTANT,
        }
        st.success(convert(userInput,userChoiceFunction.get(userChoice)))
