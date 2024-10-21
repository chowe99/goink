# Goink: Visualizing Open Source Datasets

## Overview

Goink is a web application designed to help users visualize data retrieved from open-source datasets, such as those available on [data.gov](https://www.data.gov) and [World Bank](https://data.worldbank.org). With Goink, users can access and view visual representations of various public datasets, making it easier to explore and understand important statistics like crime rates, average income, or other socio-economic indicators for a specific area. 

See [data tools](https://resources.data.gov/categories/data-tools/) for useful tools and a preexisting data visualiser.

The application aims to simplify the exploration of public data by offering an intuitive interface to view the data and gain insights that can help users make data-driven decisions.

## Features

- **Dataset Scraping**: Automatically scrapes data from data sources like [data.gov](https://www.data.gov) and [World Bank](https://data.worldbank.org), storing the data in a PostgreSQL database.
- **Data Visualization**: Presents visual representations of the data, making it easy to compare different metrics, such as crime statistics and average income.
- **REST API**: Provides RESTful API endpoints via Django REST Framework for accessing datasets programmatically.

## Application Structure

The Goink project is a Django application and follows a standard Django project structure:

- **goink/**: The main application directory containing Django settings, URL configuration, and WSGI/ASGI setup.
- **scraper/**: Contains the logic for scraping public datasets from external sources. It also defines models to store datasets and views to interact with them.
- **Docker setup**: The application is containerized using Docker, making it easy to deploy.

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Python 3.9+
- PostgreSQL (for local development)
- Node.js and npm (for frontend development)

To install Node.js and npm:
```bash
# On Ubuntu/Debian
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# On macOS (using Homebrew)
brew install node
```

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/chowe99/goink.git
   ```

2. Build and start the application using Docker Compose:
   ```
   docker-compose up --build
   ```
   This will set up the web service along with a PostgreSQL database.

3. Access the application by navigating to `http://localhost:3000` in your web browser.

### Running the Scraper

The application includes a scraper to gather data from open-source datasets. To initiate data scraping, navigate to `/scraper/scrape/` in your browser or execute the scraping logic through Django views.

### Running Tests

To run unit tests:
```bash
python manage.py test
```

## Configuration

- **Database Configuration**: The project uses a PostgreSQL database configured via Docker. Adjust the settings in `goink/settings.py` if using a different database setup.
- **Environment Variables**: Sensitive information such as the database password is set in `docker-compose.yml`. Modify these values accordingly for your environment, or leave them and they will default to my GitHub Secrets.

## Development

### Installing Dependencies

To install the required dependencies, run:
```bash
pip install -r requirements.txt
```

### Starting the Development Server

To start the development server locally without Docker:
```bash
python manage.py runserver
```
The server will be accessible at `http://127.0.0.1:8000/`.

## Deployment

Goink can be deployed using Docker. The provided `docker-compose.yml` file includes all necessary configurations for running the Django application alongside a PostgreSQL database.

For deploying to production:

- Ensure `DEBUG = False` in `goink/settings.py`.
- Set appropriate values for `ALLOWED_HOSTS`.

## Contributing

We welcome contributions from the community. Please see the [CONTRIBUTING.md](./CONTRIBUTING.md) for more information on how to get involved.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Contact

For any inquiries please find us on [Discord](https://discord.gg/JrKb8x534M).

We hope you enjoy using Goink and look forward to your contributions!
