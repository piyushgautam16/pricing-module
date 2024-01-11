# pricing_module
# Pricing Module - README Instructions

## Description

Pricing Module is a Django-based web application for managing and calculating pricing configurations for a transportation service.

## Features

- Store multiple pricing configurations based on distance, time, and other factors.
- Calculate pricing dynamically using a provided API endpoint.
- Flexible management of pricing configurations through the Django Admin interface.

## Formula used for evaluation
 - $Price = (DBP + (Dn * DAP)) + (Tn * TMF) + WC$) *where  D → Additional distance traveled*
  Where:
1. Distance Base Price ***DBP*** e.g. (80rs  Upto 3KMs on (Tue, Wed, Thur), 90rs Upto 3.5KMs (Sat, Mon), 95rs Upto 3.5KMs (Sun))
2. Distance Additional Price ***DAP*** e.g. (30rs/Km after 3KMs, 28rs/KMs)
3. Time Multiplier Factor ***TMF*** e.g. (Under 1 hour - 1x, After the initial hour - 1.25x till 2 hour, After the previous tier calculation 2.2x till 3 hour) 
4. Waiting Charges **WC** e.g. (5rs/3min after initial 3mins)

Business Development team can have multiple pricing configurations stored at any point in time and can enable/disable a particular config.

## Requirements

- Python 3.x
- Django 3.x
- Django Rest Framework

## Setup Instructions

1. **Clone the repository:**

   git clone https://github.com/piyushgautam16/pricing-module.git
   cd pricing-module
   
Create a virtual environment:


python -m venv venv
Activate the virtual environment:

On Windows:

.\venv\Scripts\activate
On macOS/Linux:

source venv/bin/activate
Install dependencies:

]

pip install -r requirements.txt
Apply database migrations:

python manage.py migrate

Create a superuser for the Django Admin:

python manage.py createsuperuser

Run the development server:

python manage.py runserver

Access the Django Admin interface:

Open your browser and go to http://127.0.0.1:8000/admin/

Log in using the superuser credentials created earlier.

**Access the Pricing Module:

Open your browser and go to http://localhost:8000/pricing/pricing-form/**

API Endpoint

Calculate Pricing:
Endpoint: /pricing/calculate-pricing/
Method: POST
Payload: {"distance": 5, "time": 2} (Example)

Project Structure

PRICING_MODULE/
│
├── pricing/
│   ├── __init__.py
│   ├── static/css
│   │   └── styles.css
│   ├── templates
│   │   └── add_or_edit_pricing_config.html
│   │   └── base.html
│   │   └── pricing_config_detail.html
│   │   └── pricing_config_list.html
│   │   └── pricing_form.html
│   ├── admin.py
│   ├── api.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── tests/
│   │   └── __init__.py
│   │   └── test_api.py
│   │   └── test_forms.py
│   │   └── test_models.py
│   │   └── test_serializers.py
│   ├── serializers.py
│   ├── forms.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── pricing_module/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── requirements.txt
└── README.md

Testing
Run tests using the following command:

python manage.py test




License
This project is licensed under the MIT License.
