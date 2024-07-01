# Car Inventory Management System

This project is a simple car inventory management system built with Django. It allows users to view a list of locally available cars, along with their details and images. The system also supports image carousels for each car.

## Features

- List all cars with details such as name, make, model, year of manufacture, trim level, and price.
- Display images for each car with a carousel feature for easy navigation.
- Filter cars based on availability.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/KigoJomo/Cars.git
    cd Cars
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

- Visit `http://127.0.0.1:8000/` in your web browser to view the car inventory.
- Log in to the admin panel at `http://127.0.0.1:8000/admin/` to add or edit car details and images.

## API Endpoints

- **Get list of locally available cars**:

    ```http
    GET /local_cars/
    ```

    Response:

    ```json
    [
        {
            "name": "Car Name",
            "make": "Car Make",
            "model": "Car Model",
            "yearMfct": 2020,
            "price": 20000,
            "trimlevel": "Trim Level",
            "images": [
                "/media/car_images/image1.jpg",
                "/media/car_images/image2.jpg"
            ]
        },
        ...
    ]
    ```

## Contributing

1. Fork the repository.
2. Create a new branch:

    ```bash
    git checkout -b feature-name
    ```

3. Make your changes and commit them:

    ```bash
    git commit -m 'Add some feature'
    ```

4. Push to the branch:

    ```bash
    git push origin feature-name
    ```

5. Create a pull request.

### Resolving Merge Conflicts

If you encounter merge conflicts, follow these steps:

1. Fetch the latest changes:

    ```bash
    git fetch origin
    ```

2. Checkout the master branch:

    ```bash
    git checkout master
    ```

3. Merge the branch:

    ```bash
    git merge origin/alvins_branch
    ```

4. Resolve conflicts in the files:

    ```bash
    git add <conflicted-file>
    git commit
    ```

5. Push the changes:

    ```bash
    git push origin master
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
