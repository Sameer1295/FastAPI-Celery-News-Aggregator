# News Aggregator Using FastAPI and Celery

Developed a News Aggregator using FastAPI and Celery, which efficiently schedules the fetching of news articles from the NewsAPI service and seamlessly stores them into a MySQL database. The Celery scheduler ensures the system updates every minute, keeping the database current with the latest articles. Get started effortlessly by cloning the repository, configuring your NewsAPI credentials, and running the application.


## Setup Instructions

Follow these steps to set up and run the project:

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>

2. Navigate to the Project Directory:
   ```bash
   cd <project_directory>

3. Install Dependencies:
   ```bash
   pip install -r requirements.txt

4. Install and Start Redis
   ```bash
   redis-server
   
5. Start Celery Beat:
   ```bash
   celery -A main.celery beat

6. Start Celery Worker:
   celery -A main.celery worker --loglevel=info -P solo
