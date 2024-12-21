# dbt, Airflow, and Snowflake Integration Project

## Overview

This project demonstrates an end-to-end data pipeline integrating **Apache Airflow**, **dbt**, and **Snowflake** for managing and processing large datasets. It includes features like Slowly Changing Dimensions (SCD Type 2), snapshots, backups, and point-in-time analysis using Snowflake's zero-copy cloning.

## Table of Contents
- [Setup Instructions](#setup-instructions)
- [Features](#features)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)
- [Author](#author)
- [License](#license)

## Setup Instructions

### Prerequisites
- Python 3.8+
- Docker and Docker Compose
- Apache Airflow
- dbt
- Snowflake account

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/username/dbt_airflow_snowflake_project.git
   cd dbt_airflow_snowflake_project
   ```

2. Build and start the Docker containers:
   ```bash
   docker-compose up --build
   ```

3. Set up the Snowflake environment:
   - Create a database and schema.
   - Load data using the `load_data.py` script.

4. Run the Airflow DAGs:
   - Navigate to the Airflow web UI.
   - Trigger the main DAG.

5. Set up dbt:
   - Navigate to the `dbt/` directory.
   - Run the dbt models:
     ```bash
     dbt run
     ```

## Features

- **Data Orchestration**: Airflow manages data ingestion, transformation, and loading.
- **Data Transformation**: dbt models implement SCD Type 2 and snapshots.
- **Point-in-Time Analysis**: Snowflake zero-copy cloning enables historical analysis.
- **Backup and Restore**: Automated backup DAG with retention policies.


## Usage

1. Update the `profiles.yml` file in the `dbt/` directory with your Snowflake credentials.
2. Modify the `docker-compose.yml` file as needed for your environment.
3. Run the pipeline and verify the results in Snowflake.

## Future Enhancements

- Add cloud deployment support for AWS/GCP.
- Integrate data quality checks with automated alerts.
- Implement incremental loading for dbt models.

## Author

**Shubham Naik**

## License

This project is licensed under the MIT License. See the LICENSE file for details.

