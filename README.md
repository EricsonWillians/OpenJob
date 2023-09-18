# OpenJob: Fair Freelancing for All

## Manifesto Against Standard Freelancing Platforms

In a world ever more connected, freelancing platforms have become the go-to solution for remote work opportunities. They promise freedom, flexibility, and an ocean of talent, but often they deliver none of these. Instead, they've created ecosystems that perpetuate inequality:

1. **Gatekeeping**: The idea of freelancing is to liberate talent from the traditional constraints of employment. However, the presence of gatekeepers in these platforms limits the number of job opportunities a newcomer can access.
   
2. **Unfair Competition**: A few established freelancers, often those who joined the platform early, dominate most of the job markets. It leaves little room for newcomers, who often have to undervalue their skills to secure even a single job.

3. **High Fees**: These platforms take a significant cut from freelancers' earnings, making it difficult to sustain a decent income. Sometimes the fees go up to 20%, which is outrageous for a platform that provides only a meeting ground.

4. **Lack of Transparency**: The algorithms behind job matching and profile visibility are often opaque. Freelancers are left in the dark about why they might not be getting offers, even when they meet all criteria for a job.

OpenJob is our stand against these inequalities. It's more than a project; it's a movement towards fair freelancing for all, regardless of your experience or geographic location. OpenJob aims to democratize the freelancing world, leveling the playing field and making it accessible and fair for everyone.

## Features

- **Equal Opportunities**: Randomized job matching to give everyone a fair chance.
- **Transparent Fee Structure**: Low, straightforward fees that make sense.
- **Decentralized Architecture**: No central authority or single point of failure.
- **PayPal Integration**: Secure and trusted payment system.
- **Milestone-based Escrow Service**: Payment guaranteed upon completion of milestones.

## Project Structure

```plaintext
OpenJob/
|-- app/
|   |-- __init__.py
|   |-- main.py               # Main app logic
|   |-- node.py               # P2P Node logic using py-libp2p
|   |-- peer_discovery.py     # Peer discovery methods
|   |-- job_management.py     # Job listing, matching logic
|   |-- payment/
|   |   |-- __init__.py
|   |   |-- paypal.py         # PayPal API integration
|   |-- identity/
|   |   |-- __init__.py
|   |   |-- decentralized_id.py  # Decentralized Identity handling
|
|-- templates/
|   |-- index.html            # Main dashboard
|   |-- job_list.html         # List of jobs
|   |-- job_detail.html       # Detailed job view
|
|-- static/
|   |-- css/
|   |   |-- main.css
|   |-- js/
|   |   |-- main.js
|
|-- tests/
|   |-- __init__.py
|   |-- test_node.py          # Tests for node.py
|   |-- test_job_management.py  # Tests for job_management.py
|
|-- config/
|   |-- settings.py           # Config settings, API keys, etc.
|
|-- README.md
|-- requirements.txt          # Required Python packages
|-- run.py                    # Entry point, launches the app
```

## Getting Started

1. **Clone the Repository**
    ```bash
    git clone https://github.com/YourUsername/OpenJob.git
    ```

2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**
    ```bash
    python run.py
    ```

4. Navigate to `http://localhost:5000/` to access the OpenJob platform.

## How to Contribute

Please read our [CONTRIBUTING.md](CONTRIBUTING.md) guide for details on how to submit pull requests, and the process for submitting bugs, feature requests, etc.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

Join us in redefining what freelancing means and making it fair and accessible for everyone. We believe in a world where talent speaks louder than algorithms or centralized power. Be a part of the change. Be a part of OpenJob.