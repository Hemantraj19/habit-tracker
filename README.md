# Habit Tracker Using Pixela API Integration

This Python script integrates with the Pixela API to track and visualize study hours on a custom graph.

## Prerequisites

Before running the script, make sure you have the following:

- Python installed on your machine
- `requests` library installed (you can install it using `pip install requests`)
- Pixela account (visit [Pixela](https://pixe.la/) to create one)
- Obtain your Pixela API token

## Configuration

Replace the following variables in the script with your Pixela account details:

- `USERNAME`: Your Pixela username
- `TOKEN`: Your Pixela API token
- `GRAPHID`: Unique identifier for your graph

## Usage

1. Run the script to create a user on Pixela (uncomment the user creation code block).
2. Uncomment the graph creation code block to create a graph for studying.
3. Enter the number of study hours when prompted.
4. Check the response to ensure successful pixel creation.

You can also update and delete pixels by uncommenting the relevant code blocks.

## Code Structure

- `user_params`: Parameters for creating a Pixela user.
- `graph_config`: Configuration for the study graph.
- `post_pixel_parameters`: Parameters for creating a pixel (study entry).
- `update_pixel_parameters`: Parameters for updating a pixel.

## Endpoints

- User creation: `POST /v1/users`
- Graph creation: `POST /v1/users/{username}/graphs`
- Pixel creation: `POST /v1/users/{username}/graphs/{graphID}`
- Pixel update: `PUT /v1/users/{username}/graphs/{graphID}/{YYYYMMDD}`
- Pixel deletion: `DELETE /v1/users/{username}/graphs/{graphID}/{YYYYMMDD}`

## References

- [Pixela API Documentation](https://docs.pixe.la/)

Feel free to customize and extend the script based on your requirements.
