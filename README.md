
README.md,

# Go Game Score Calculation API

This is a Flask web API that calculates the maximum number of draws in a series of Go games played by three friends, given their points.

## Setup

1. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the Flask app:
    ```bash
    python app.py
    ```

3. Access the endpoint:
    ```
    http://localhost:5000/<p1>/<p2>/<p3>
    ```

## Example

Request: http://localhost:5000/10/10/20


Response:
```json
{
  "max_draws": 20
}


TESTING,

python test_app.py

Typesript is, 


### Explanation

1. **app.py**:
   - This file contains the Flask application. The `calculate_draws` function handles the logic to calculate the maximum number of draws or returns `-1` if the scores are invalid. It ensures that the points are in non-decreasing order, calculates the total points and games played, and checks for valid game configurations before computing the maximum number of draws.

2. **test_app.py**:
   - This file contains the unit tests for the API. It uses the `unittest` framework to test various scenarios and edge cases to ensure the API behaves as expected.

3. **requirements.txt**:
   - This file lists the dependencies required for the project, specifically Flask.

4. **README.md**:
   - This file provides instructions for setting up and running the project, including examples of how to use the API and how to run the tests.

To run this project, follow these steps:

1. Create a directory named `go_game_api` and navigate into it.
2. Create the four files (`app.py`, `test_app.py`, `requirements.txt`, `README.md`) with the content provided above.
3. Install the dependencies by running `pip install -r requirements.txt`.
4. Run the Flask application by executing `python app.py`.
5. Access the API endpoint in your browser or use a tool like `curl` or Postman.
6. Run the tests by executing `python test_app.py`.

This setup ensures you have a working API with the required functionality and tests to validate it.