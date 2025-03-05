# TeamTracker: Employee Dashboard

## Installation

1. Clone the repository:
```bash
git clone 
```

2. Navigate to the project directory:
```bash
cd team-tracker
```

4. Install required packages:
```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the root directory:
```env
.env create as per .env.template
```

## Running Migrations

1. Apply migrations:
```bash
python manage.py migrate
```

## Create Superuser

1. create super user to access django admin:
```bash
python manage.py createsuperuser
```

## Running the Server

1. Run the server:
```bash
python manage.py runserver
```
