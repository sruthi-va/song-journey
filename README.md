# Song Journey

A music recommendation system that generates a smooth sequence of songs between two selected tracks.

Inspired by the concept of "Boil the Frog," the application finds intermediate songs that create a gradual musical transition from a starting song to a destination song.

## Example

```text
Song A
  ↓
Similar Song
  ↓
Another Song
  ↓
Destination Song
```

The number of intermediate songs is determined automatically based on how different the starting and destination songs are.

## Planned Features

* Search for a starting and destination song
* Analyze song metadata, audio features, and embeddings
* Calculate similarity between songs
* Build a graph of musically related songs
* Generate smooth transitions between two songs
* Automatically determine the required journey length
* Explain why consecutive songs were selected
* Visualize the complete song journey

## Planned Tech Stack

* Python
* FastAPI
* PostgreSQL
* React
* Docker
* Graph algorithms
* Music embeddings and similarity search

## Project Status

Currently in development.
