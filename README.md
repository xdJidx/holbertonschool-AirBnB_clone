# AirBnB Clone Project - The Console
![hbnb](https://user-images.githubusercontent.com/91517809/176107896-998e3280-f565-4e09-a801-c609984bfed6.png)

## Description
The AirBNB Clone project aims to replicate the functionality of the popular accommodation booking platform, Airbnb. It provides a framework for managing various classes such as User, Place, City, State, and Review, allowing users to interact with the system through a console interface.

## Compilation/Installation
To compile and install the AirBNB Clone project, please follow these steps:

1. Clone the repository from GitHub:
"""
git clone https://github.com/Spark4545/holbertonschool-AirBnB_clone.git
"""

2. Navigate to the project directory:
"""
cd holbertonschool-AirBnB_clone
"""

## Requirements
The AirBNB Clone project requires the following dependencies:

Python 3.x
Pip (Python package installer)
Other dependencies specified in the requirements.txt file
Examples
Here are some examples of how to use the AirBNB Clone project:

1. Creating a BaseModel object from a dictionary:
"""
from models.base_model import BaseModel

data = {
    'id': '123',
    'created_at': '2023-01-01T12:00:00',
    'updated_at': '2023-01-01T12:00:00'
}

obj = BaseModel(**data)
"""

2. Storing the first object:
"""
from models import storage

obj.save()  # The object will be saved in the file storage
"""

3. Interacting with the console:
"""
python console.py
(hbnb) help
"""

4. Creating a User object:
"""
from models.user import User

user = User()
user.name = "John Doe"
user.email = "john.doe@example.com"
user.save()
"""

## Testing
To run the tests for the AirBNB Clone project, execute the following command from the project directory:
"""
python -m unittest discover tests
"""
The tests will validate the functionality of different components and classes within the project.

Please note that these instructions assume you have a basic understanding of Python and its development environment. If you encounter any issues, refer to the project's documentation or seek assistance from the project maintainers.

Enjoy using the AirBNB Clone project!