import sqlite3
import uuid
from datetime import datetime

class JobManagement:
    def __init__(self):
        # SQLite database connection
        self.conn = sqlite3.connect('jobs.db')
        self.c = self.conn.cursor()
        
        # Create table if it does not exist
        self.c.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
                job_id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                budget REAL NOT NULL,
                deadline TEXT NOT NULL,
                posted_at TEXT NOT NULL,
                status TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def create_job(self, title, description, budget, deadline):
        # Create a new job listing
        job_id = str(uuid.uuid4())
        posted_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        status = 'open'
        
        self.c.execute("INSERT INTO jobs VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (job_id, title, description, budget, deadline, posted_at, status))
        self.conn.commit()
        return job_id

    def update_job(self, job_id, **kwargs):
        for key, value in kwargs.items():
            self.c.execute(f"UPDATE jobs SET {key} = ? WHERE job_id = ?", (value, job_id))
        self.conn.commit()

    def get_job(self, job_id):
        self.c.execute("SELECT * FROM jobs WHERE job_id = ?", (job_id,))
        row = self.c.fetchone()
        if row:
            return {
                'job_id': row[0],
                'title': row[1],
                'description': row[2],
                'budget': row[3],
                'deadline': row[4],
                'posted_at': row[5],
                'status': row[6]
            }
        return None

    def list_jobs(self):
        self.c.execute("SELECT * FROM jobs")
        rows = self.c.fetchall()
        jobs = []
        for row in rows:
            jobs.append({
                'job_id': row[0],
                'title': row[1],
                'description': row[2],
                'budget': row[3],
                'deadline': row[4],
                'posted_at': row[5],
                'status': row[6]
            })
        return jobs

if __name__ == "__main__":
    job_manager = JobManagement()
    new_job_id = job_manager.create_job("Web Development", "Build a website", 1000, "2023-10-30")
    print(f"New Job ID: {new_job_id}")
    
    print("Listing All Jobs:")
    print(job_manager.list_jobs())

    print("Updating Job:")
    job_manager.update_job(new_job_id, budget=1500)
    print(job_manager.get_job(new_job_id))
