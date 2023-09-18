import streamlit as st
from app.job_management import JobManagement  # Import the JobManagement class

def main():
    st.title('OpenJob: Fair Freelancing for Everyone')
    
    # Initialize JobManagement class
    job_manager = JobManagement()
    
    # Sidebar for creating a new job
    st.sidebar.header("Create New Job")
    new_title = st.sidebar.text_input("Title", "Job Title")
    new_description = st.sidebar.text_area("Description", "Job Description")
    new_budget = st.sidebar.number_input("Budget", min_value=0)
    new_deadline = st.sidebar.date_input("Deadline")
    
    if st.sidebar.button('Post New Job'):
        new_job_id = job_manager.create_job(new_title, new_description, new_budget, str(new_deadline))
        st.sidebar.success(f"Job Created Successfully with ID: {new_job_id}")

    # Display available jobs
    st.subheader('Available Jobs')
    jobs = job_manager.list_jobs()  # Call the list_jobs method from JobManagement

    for job in jobs:
        st.write(f"**{job['title']}**")
        st.write(f"Budget: {job['budget']}")
        st.write(f"Deadline: {job['deadline']}")
        st.write(job['description'])

        if st.button('Apply', key=job['job_id']):
            # Trigger your job application logic
            st.success(f"You've applied for {job['title']}")

if __name__ == '__main__':
    main()
