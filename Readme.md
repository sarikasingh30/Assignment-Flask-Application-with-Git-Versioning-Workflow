# Assignment: Flask Application with Git Versioning Workflow

## Project Title and Description

This is a small web application built with Python and Flask that lets people vote for
candidates and check the current results. You visit a URL like `/vote/Alice` in your
browser to cast a vote, and `/results` to see how many votes everyone has so far. All
votes are kept in memory while the app is running — no database is needed. There's also
a `/reset` endpoint to clear all votes and start over.

## Installation and Setup Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```
2. (Recommended) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   python3 app.py
   ```
5. Open your browser and go to:
   ```
   http://localhost:5000/
   ```

## API Endpoint Reference

| Endpoint       | Method | Description                                    | Example Response                                                                   |
| -------------- | ------ | ---------------------------------------------- | ---------------------------------------------------------------------------------- |
| `/`            | GET    | Welcome message                                | `Welcome to the App`                                                               |
| `/health`      | GET    | Confirms the app is running                    | `App is running`                                                                   |
| `/vote/<name>` | GET    | Records one vote for `<name>`                  | `{"message": "Vote recorded for Alice", "candidate": "Alice", "current_votes": 1}` |
| `/results`     | GET    | Returns current vote counts for all candidates | `{"Alice": 2, "Bob": 1}`                                                           |
| `/reset`       | GET    | Clears all vote counts                         | `{"message": "All votes have been reset"}`                                         |

## Git Workflow

This project follows a `dev` → `main` branching workflow:

1. All new code is written and tested on the `dev` branch first.
2. Once a feature works correctly, `dev` is pushed to GitHub.
3. `dev` is then merged into `main`, so `main` always contains stable, working code.
4. `main` is pushed to GitHub as the official release.
5. This cycle repeats for every new version.

## Version History

| Version | Branch flow | What was added                                                                     |
| ------- | ----------- | ---------------------------------------------------------------------------------- |
| v1.0    | dev → main  | Base Flask app (`/`, `/health`) plus voting endpoints (`/vote/<name>`, `/results`) |
| v2.0    | dev → main  | `/reset` endpoint to clear all stored votes                                        |

## Screenshots

**1. Application running in the browser (working endpoint):**

![App running screenshot](<images/Screenshot%20(307).png>)
![App running screenshot](<images/Screenshot%20(308).png>)
![App running screenshot](<images/Screenshot%20(309).png>)
![App running screenshot](<images/Screenshot%20(310).png>)
![App running screenshot](<images/Screenshot%20(311).png>)
![App running screenshot](<images/Screenshot%20(312).png>)
