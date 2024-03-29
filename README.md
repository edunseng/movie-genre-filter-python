# Python Movie Catalogue Assistant

## Project Overview
This Python project provides a simple yet effective way to read and filter a list of movies from a JSON file by category. It's designed to help users interactively select movies based on their preferred genre.

## Features
- Load and parse movie data from JSON.
- Interactive genre selection for users.
- Display movie titles within selected genres.
- Error handling for user input validation.

## Pre-requisites
Before you start using this project, ensure that you have the following packages installed:
- `movie-rec-marking-aicore`

You can install them using the following commands:
```bash
pip install movie-rec-marking-aicore --upgrade --quiet
wget https://aicore-files.s3.amazonaws.com/Movie-Recommendation/movies-head.json --quiet
```

## Usage
To use this project:

- Clone the repository to your local machine.
- Run `python app.py` to load and interact with the movie data.
- Use the interactive prompts to filter movies by genre.

## How It Works
The project is divided into several milestones, each designed to guide you through understanding and interacting with the movie data:

### Milestone 1: Understand the Data
Learn how to count movies, select specific movies, and explore movie attributes.

### Milestone 2: Explore the Data
Display movie titles, calculate the length of movie descriptions, and find the longest movie name.

### Milestone 3: Unique Genres
Identify all unique genres within the dataset.

### Milestone 4: User Interaction
Ask users for their genre preference and display movies that match the selected genre.

### Milestone 5: Error Handling
Implement error handling to validate user inputs when selecting genres.

## Contributing
Feel free to fork this project and submit pull requests with enhancements or fixes.

## License
This project is open-source and unlicensed.
