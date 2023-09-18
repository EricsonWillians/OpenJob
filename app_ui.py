import streamlit as st
from app.job_management import JobManagement  # Import the JobManagement class

def main():
    st.title('OpenJob: Fair Freelancing for Everyone')
    
    # Initialize JobManagement class
    job_manager = JobManagement()
    
    # Display jobs
    st.subheader('Available Jobs')
    jobs = job_manager.list_jobs()  # Call the list_jobs method from JobManagement
    for job in jobs:
        st.write(f"**{job['title']}**")
        st.write(job['description'])
        if st.button('Apply', key=job['job_id']):
            # Trigger your job application logic
            pass

if __name__ == '__main__':
    main()
