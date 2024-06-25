# Flask File Upload Project

This is a simple Flask project that allows users to upload files to a MySQL database. Each uploaded file is stored in the database.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Tnvj/Flask-Form
   cd Flask-Form
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**

   ```bash
   pip install Flask Flask-MySQLdb python-dotenv
   ```

5. **Set up environment variables:**

   Create a `.env` file in the root directory of the project:

   ```plaintext
   MYSQL_HOST=your_mysql_host
   MYSQL_USER=your_mysql_user
   MYSQL_PASSWORD=your_mysql_password
   MYSQL_DB=your_mysql_db
   UPLOAD_FOLDER=uploads
   ```

   Adjust the values according to your MySQL setup.

6. **Initialize the MySQL database:**

   - Create a MySQL database with the name specified in your `.env` file.
   - Update the database configuration in `app.py` if necessary.

7. **Run the application:**

   ```bash
   python app.py
   ```

   The application will start running on `http://localhost:5000`.

## Usage

1. **Upload Files:**


2. **View Uploaded Files:**



## Dependencies

- Flask
- Flask-MySQLdb
- python-dotenv
