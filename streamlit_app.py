import streamlit as st

st.markdown(
    """
    <style>
    /* Background color */
    .stApp {
        background-color: #222f62;
    }

    /* Sidebar background color */
    .css-1d391kg {
        background-color: #0e1117;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("VoteInclusive 2024")

with st.expander("VoteInclusive Polling Centers"):
    st.write("These Polling Centers are valid national vote centers")

st.sidebar.title("VoteInclusive 2024")
st.sidebar.subheader("Everybody deserves a vote")

st.text_input("State Full Name")

st.number_input("Age", min_value=0)

if st.number_input("Zip Code", min_value=0):
    st.subheader("Nov. 5, 2024 - GENERAL ELECTION")
    st.write("Precinct HAD-014 | St. Louis County, Missouri ZIP: 63105")
    st.error("THIS IS NOT A VALID BALLOT!!! THIS IS A VOTING SIMULATOR!!!")

    st.radio("U.S. President and Vice President", ("Donald J. Trump and JD Vance (REPUBLICAN)", "Kamala D. Harris and Tim Walz (DEMOCRATIC)", "Chase Oliver and Mike Ter Maat (LIBERTARIAN)", "Jill Stein and Rudolph Ware (GREEN)"))

    st.radio("U.S. Senator", ("Josh Hawley (REPUBLICAN)", "Lucas Kunce (DEMOCRATIC)", "W. C. Young (LIBERTARIAN)", "Jared Young (BETTER)", "Nathan Kline (GREEN)"))

    st.radio("Missouri Governor", ("Mike Kehoe (REPUBLICAN)", "Crystal Quade (DEMOCRATIC)", "Bill Slantz (LIBERTARIAN)"))

    st.radio("Attorney General", ("Andrew Bailey (REPUBLICAN)", "Elad Jonathan Gross (DEMOCRATIC)", "Ryan L. Munro (LIBERTARIAN)"))

    st.radio("State Representative", ("Ian Mackey (DEMOCRATIC)", "OTHER CANDIDATE"))