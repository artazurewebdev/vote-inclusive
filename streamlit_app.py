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
    st.warning("Not available until November 5, 2024 at 7:00AM")

st.sidebar.title("VoteInclusive 2024")
st.sidebar.subheader("Everybody deserves a vote")
st.sidebar.image("White Navy Blue Modern American Veteran Company Logo.png", width=250)

st.text_input("State Full Name")

st.number_input("Age", min_value=0)

if st.number_input("Zip Code", min_value=0):
    st.subheader("Nov. 5, 2024 - GENERAL ELECTION")
    st.write("Precinct HAD-014 | St. Louis County, Missouri ZIP: 63105")
    st.error("THIS IS NOT A VALID BALLOT!!! THIS IS A VOTING SIMULATOR!!!")

    st.multiselect("Are you with a School District?", ("Not with a School District", "Clayton School District", "Ladue School District", "Pattonville School District", "Other District Near Me"))

    st.radio("U.S. President and Vice President", ("Donald J. Trump and JD Vance (REPUBLICAN)", "Kamala D. Harris and Tim Walz (DEMOCRATIC)", "Chase Oliver and Mike Ter Maat (LIBERTARIAN)", "Jill Stein and Rudolph Ware (GREEN)"))

    st.radio("U.S. Senator", ("Josh Hawley (REPUBLICAN)", "Lucas Kunce (DEMOCRATIC)", "W. C. Young (LIBERTARIAN)", "Jared Young (BETTER)", "Nathan Kline (GREEN)"))

    st.radio("Missouri Governor", ("Mike Kehoe (REPUBLICAN)", "Crystal Quade (DEMOCRATIC)", "Bill Slantz (LIBERTARIAN)"))

    st.radio("Attorney General", ("Andrew Bailey (REPUBLICAN)", "Elad Jonathan Gross (DEMOCRATIC)", "Ryan L. Munro (LIBERTARIAN)"))

    st.radio("State Representative", ("Ian Mackey (DEMOCRATIC)", "OTHER CANDIDATE"))

    if st.button("Submit Ballot"):

        st.success("CURRENT POLLS (Open)")

        with st.expander("U.S. President and Vice President"):

            st.markdown("<span style='color:red'> DOMINANT CANDIDATE: Donald J. Trump and JD Vance (REPUBLICAN) </span>", unsafe_allow_html=True)

            st.subheader("Live Percentages")
            col1, col2, col3, col4 = st.columns(4)
            col1.metric(label="% Dominant Candidate", value=49.23, delta=0.78)
            col2.metric(label="% DC in Missouri", value=66.21, delta=0.30)
            col3.metric(label="% DC in STL Cty.", value=32.10, delta=-2.13)
            col4.metric(label="% DC in CSD", value=0.12, delta=0.03)

            st.error("Donald J. Trump and JD Vance")

        with st.expander("U.S Senator"):

            st.markdown("<span style='color:red'> DOMINANT CANDIDATE: Josh Hawley (REPUBLICAN) </span>", unsafe_allow_html=True)

            st.subheader("Live Percentages")
            col1, col2, col3 = st.columns(3)
            col1.metric(label="% DC in Missouri", value=66.21, delta=0.30)
            col2.metric(label="% DC in STL Cty.", value=45.22, delta=-6.17)
            col3.metric(label="% DC in CSD", value=36.23, delta=-0.12)

            st.error("Josh Hawley")

        with st.expander("Missouri Governor"):

            st.markdown("<span style='color:blue'> DOMINANT CANDIDATE: Crystal Quade (DEMOCRATIC) </span>", unsafe_allow_html=True)

            st.subheader("Live Percentages")
            col1, col2, col3 = st.columns(3)
            col1.metric(label="% DC in Missouri", value=69.55, delta=0.04)
            col2.metric(label="% DC in STL Cty.", value=82.49, delta=0.61)
            col3.metric(label="% DC in CSD", value=89.23, delta=-0.01)

            st.info("Crystal Quade")
