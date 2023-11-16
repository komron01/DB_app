# User Authentication System and Arithmetic Game

This project combines a simple user authentication system and an arithmetic game. The user authentication system allows users to log in, create accounts, and stores user credentials in a MongoDB database. The arithmetic game tests users' addition skills and provides feedback on their answers.

## User Authentication System

### Description

The user authentication system includes the following files:

- `autho.py`: Manages the login functionality, user authentication, and includes a button to redirect to the registration form.
- `reg.py`: Implements a user registration form that adds new users to a MongoDB database.
- `main_W.py`: Implements an arithmetic game that tests users' addition skills.

## Additional Files

### `dashboard.py`

- Manages the user dashboard, displaying user information in a user-friendly format.
- Provides options for viewing and interacting with user information.

### `admin_dashboard.py`

- Manages the admin dashboard, allowing administrators to view, delete, edit, and reset passwords for user accounts.
- Displays a list of users with relevant information in a treeview widget.

### `game.py`

- Implements an arithmetic game where users can test their addition skills.
- Provides a graphical user interface for the game.

### `reg.py`

- Implements a user registration form that adds new users to a MongoDB database.
- Integrates with the user authentication system for a seamless user experience.


### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/komron01/DB_app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd DB_app
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

#### Running the User Authentication System

To run the user authentication system, execute the following command:

```bash
python main_W.py
