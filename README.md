# youtube-playlist-to-excel-using-api

This Python script generates an Excel file containing details of all the videos in a specified YouTube playlist. The details include the video ID, title, description, duration, and a link to each video.

## Features

- Fetches video details from a YouTube playlist.
- Converts video duration from ISO 8601 format to a more readable format.
- Generates an Excel file with columns for Video ID, Title, Description, Duration, and Link.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.x**: The script is compatible with Python 3.x.
- **Google API Key**: You need a YouTube Data API key. Obtain it from the [Google Developer Console](https://console.developers.google.com/).
- **Required Python Packages**: Install the necessary Python packages using the following command:

  ```bash
  pip install google-api-python-client pandas openpyxl
  ```

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/youtube-playlist-to-excel.git
   ```

2. Navigate to the project directory:

   ```bash
   cd youtube-playlist-to-excel
   ```

3. Install the required packages:

   ```bash
   pip install google-api-python-client pandas openpyxl
   ```

## Usage

1. Open the `script.py` file in a text editor.

2. Replace the `API_KEY` variable with your YouTube Data API key:

   ```python
   API_KEY = 'YOUR_YOUTUBE_API_KEY'
   ```

3. Replace the `PLAYLIST_ID` variable with the ID of the YouTube playlist you want to extract data from:

   ```python
   PLAYLIST_ID = 'YOUR_PLAYLIST_ID'
   ```

4. Run the script:

   ```bash
   python script.py
   ```

5. The script will generate an Excel file named `youtube_playlist.xlsx` in the project directory. This file will contain the following columns:

   - **Video ID**: The unique identifier for each video.
   - **Title**: The title of the video.
   - **Description**: A brief description of the video.
   - **Duration**: The duration of the video in a readable format (e.g., `1:02:34`).
   - **Link**: A direct link to the video.

## Example

Here’s an example of what the generated Excel file might look like:

| Video ID      | Title                      | Description                            | Duration | Link                                    |
|---------------|----------------------------|----------------------------------------|----------|-----------------------------------------|
| dQw4w9WgXcQ   | Never Gonna Give You Up     | The official music video of Rick Astley | 3:33     | [Watch Now](https://www.youtube.com/watch?v=dQw4w9WgXcQ) |



## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

If you have any questions or suggestions, feel free to reach out.

- **GitHub**: [Arun12311](https://github.com/ArunSadalgekar07)
- **Email**: arunsadalgekar07@gmail.com
