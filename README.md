# Social Media APIs
A set of APIs for a social media application that allows users to share text, images, and videos, interact with each other's content, join groups, and more

## Requirements

To run this project locally, you will need to have the following installed:

- Python 3.8+
- Django 4.0+
- Django Rest Framework 3.12+

You can install these dependencies by running:


pip install -r requirements.txt


## Running Locally

To run the project locally, follow these steps:

1. Clone the repository:


git clone https://github.com/yourusername/social-media-apis.git


2. Navigate to the project directory:


cd social-media-apis


3. Create a virtual environment:


python -m venv env


4. Activate the virtual environment:

On Windows:


env\Scripts\activate


On Unix or Linux:


source env/bin/activate


5. Install the dependencies:


pip install -r requirements.txt


6. Run the migrations:


python manage.py migrate


7. Start the development server:


python manage.py runserver


The API will be available at http://localhost:8000.

## API Documentation

The API documentation can be found at http://localhost:8000/docs/. This documentation is generated automatically by DRF and provides detailed information about each endpoint, including request and response formats, authentication requirements, and more.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.