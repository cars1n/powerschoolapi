# PowerSchool API Python Package

This Python package provides an easy-to-use interface for interacting with the PowerSchool API, allowing users to perform various operations such as retrieving student counts, student details, course counts, and more from a PowerSchool server.

## Features

- Get student count for a specified school.
- Retrieve detailed student information.
- Fetch course counts.
- [More features you might have...]

## Installation

To install the PowerSchool API package, use pip:

```bash
pip install powerschoolapi_cars1n
```

## Usage

Here's a quick start on how to use the PowerSchool API package:

```bash
from PowerSchoolAPI import PS

# Initialize the PowerSchool API client
ps = PS()

# Get the count of students in a school
student_count = ps.get_student_count("school_dcid")
ic("Student Count:", student_count)

# Get detailed information about a student
student_info = ps.get_student("student_id")
ic("Student Information:", student_info)

```

## Configuration

Before using the PowerSchool API, ensure that you have set up the necessary environment variables. Your .env file should look something like this.

CLIENT_ID =
CLIENT_SECRET =
POWERSCHOOL_SERVER_URL = "https://powerschool.example.com:443"

## Contributing

Contributions to the PowerSchool API package are welcome. Please follow these steps to contribute:

 - Fork the repository.
 - Create a new branch for your feature.
 - Add your changes.
 - Submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any queries or issues, please open an issue on the GitHub repository or contact me via email at 14williamsc@gmail.com
