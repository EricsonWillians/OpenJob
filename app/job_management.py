import json
import uuid
from datetime import datetime

class JobManagement:
    def __init__(self):
        self.jobs = []  # List to store job listings

    def create_job(self, title, description, budget, deadline):
        # Create a new job listing
        job_id = str(uuid.uuid4())
        job = {
            'job_id': job_id,
            'title': title,
            'description': description,
            'budget': budget,
            'deadline': deadline,
            'posted_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'status': 'open'  # Job status can be 'open', 'in_progress', 'completed', 'closed'
        }
        
        self.jobs.append(job)
        return job_id

    def update_job(self, job_id, **kwargs):
        # Update an existing job listing
        for job in self.jobs:
            if job['job_id'] == job_id:
                for key, value in kwargs.items():
                    if key in job:
                        job[key] = value
                return True
        return False

    def get_job(self, job_id):
        # Retrieve job by job_id
        for job in self.jobs:
            if job['job_id'] == job_id:
                return job
        return None

    def list_jobs(self):
        # Return all job listings
        return self.jobs

    def serialize_jobs(self):
        # Serialize job listings to JSON
        return json.dumps(self.jobs)

    def deserialize_jobs(self, job_data):
        # Load job listings from JSON data
        self.jobs = json.loads(job_data)

if __name__ == "__main__":
    job_manager = JobManagement()
    new_job_id = job_manager.create_job("Web Development", "Build a website", 1000, "2023-10-30")
    print(f"New Job ID: {new_job_id}")
    
    print("Listing All Jobs:")
    print(job_manager.list_jobs())

    print("Updating Job:")
    job_manager.update_job(new_job_id, budget=1500)
    print(job_manager.get_job(new_job_id))
