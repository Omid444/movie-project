🎬 Movie Project
A Python-based application that fetches movie data from an API, stores it in a SQLite database, and generates a static HTML website to display the movies.

📂 Project Structure
css
Copy
Edit
movie-project/
├── _static/
│   ├── index_template.html
│   └── style.css
├── data/
│   └── movies.db
├── __pycache__/
├── api_fetcher.py
├── main.py
├── movie_storage_sql.py
├── movie_web_generator.py
├── movies.py
├── requirement.txt
└── README.md
🚀 Features
API Integration: Fetches movie data from an external API.

Database Storage: Stores movie information in a SQLite database.

HTML Generation: Creates a static HTML page to display the movies.

Modular Design: Organized into separate modules for clarity and maintainability.

🛠️ Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/Omid444/movie-project.git
cd movie-project
Create a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the required packages:

bash
Copy
Edit
pip install -r requirement.txt
📈 Usage
Run the main script:

bash
Copy
Edit
python main.py
This will:

Fetch movie data from the API.

Store the data in the SQLite database located at data/movies.db.

Generate a static HTML page using the template in _static/index_template.html.

View the generated website:

Open the generated HTML file in your web browser to see the list of movies.

🧩 Modules Overview
api_fetcher.py: Handles fetching data from the external movie API.

movie_storage_sql.py: Manages interactions with the SQLite database.

movie_web_generator.py: Generates the static HTML page using the template.

movies.py: Contains the Movie class definition.

main.py: Orchestrates the overall workflow by utilizing the above modules.

📝 License
This project is licensed under the MIT License. See the LICENSE file for details.
