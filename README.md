# YouTube Playlist Analyzer

YouTube doesn't provide a direct way to filter playlists based on their overall durations, which can be crucial when searching for tutorials, courses, or academic lessons. For instance, you may want to find a lesson with at least 4 hours of content. Moreover, many channels that offer technical and informative content remain undiscovered due to low views. In summary, YouTube's algorithms aren't optimized for academic searching.

## Purpose

To address this limitation, the YouTube Playlist Analyzer project introduces a more convenient way to discover courses and playlists. Playlists are ordered by the ratio of likes/views, ensuring that even small channels have a chance to be discovered. Additionally, a duration filter is implemented, which is currently lacking in YouTube's native search functionality for playlists.

## Features

- **Playlist Duration Filter**: Users can specify the minimum and maximum duration of playlists they're searching for, enabling them to find content of appropriate length.
- **Likes/Views Ratio Sorting**: Playlists are sorted based on their likes/views ratio, allowing users to discover high-quality content regardless of the channel's popularity.
- **Flask Web Interface**: The project provides a minimalistic web interface built with Flask, making it easy for users to search for playlists and view the results.

### Additional Features

- **Calculate Duration of a Given Playlist**: Users can quickly calculate the overall duration of a specific playlist. If a playlist is found, this feature provides a convenient way to determine its total duration.

### Future Enhancements

- **Comment Analysis**: Analyze comments within playlists to provide insights into user feedback, sentiment analysis, and topic relevance.
- **Language and Accent Filtering**: Implement features to filter playlists based on the language of the content and accents of the speakers. This will help users find content in their preferred language or accent.

## Getting Started

### Prerequisites

- Python 3.x
- Google API Key (for accessing YouTube Data API)
- Flask (for running the web interface)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/BlcMed/yt-playlist-analyzer.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Google API Key by following the instructions [here](https://developers.google.com/youtube/registering_an_application).

4. Rename the .env.sample file to .env:

    ```bash
    mv .env.sample .env
    ```

5. Open the .env file and fill in your Google API Key:

    ```bash
    API_KEY=your_google_api_key
    ```

### Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000` to access the application.

3. Enter the tutorial name and specify the desired duration filter (minimum and maximum).

4. Click on the "Search" button to retrieve the results.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

## License

This project is licensed under the terms of the [GNU Lesser General Public License v3.0](LICENSE), a copy of which is included in the repository.

