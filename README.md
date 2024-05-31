# Weather Report Using Python

#### Video Demo: <https://youtu.be/JHXvse_n3Ug>

## Description

This application provides real-time weather information and a brief summary about a city. It is designed for users who want to quickly access both weather details and a brief overview of a city from a single interface. The application utilizes the OpenWeatherMap API to fetch weather data and scrapes Wikipedia to retrieve a summary of the city.

The project is built using Python and leverages the Tkinter library for the graphical user interface (GUI), requests for making API calls, and BeautifulSoup for web scraping. The application is simple to use and provides a user-friendly interface to display the fetched information.

## Files

### `project.py`

This is the main script that contains all the functionalities of the application. Here’s a breakdown of what each part of the script does:

- **Imports**: The script imports necessary libraries such as `tkinter` for GUI, `requests` for API calls, `BeautifulSoup` from `bs4` for web scraping, `re` for regular expression operations, `webbrowser` for opening links, and `datetime` for handling date and time.

- **Functions**:
  - `get_weather(api_key, city)`: Fetches weather data for the specified city using the OpenWeatherMap API. Returns the weather data in JSON format if the request is successful, otherwise returns `None`.
  - `get_wikipedia_info(city)`: Scrapes Wikipedia to get a brief summary about the specified city. Cleans the retrieved text by removing references and parentheses. Returns the summary text and the Wikipedia URL.
  - `open_link(url)`: Opens a URL in a new browser window.
  - `fetch_weather(api_key, root)`: Retrieves the city entered by the user, fetches weather data and Wikipedia summary, and displays the information in a new window. Handles errors and provides links for detailed weather reports and Wikipedia articles.

- **GUI Setup**:
  - Sets up the main application window using Tkinter. Configures the window size, title, and layout. Includes an entry field for the user to input a city name and a button to fetch weather information.

- **Main Function**:
  - Initializes the main Tkinter application loop.

## Design Choices

### Use of Tkinter for GUI

Tkinter was chosen for its simplicity and ease of use. It is a built-in Python library, which means it does not require any additional installations and is sufficient for creating the basic GUI needed for this project.

### API Integration

The OpenWeatherMap API was selected because it provides comprehensive weather data and is free to use with a developer account. The decision to use this API was based on its reliability, ease of integration, and the detailed documentation available.

### Web Scraping with BeautifulSoup

BeautifulSoup was chosen for web scraping due to its simplicity and powerful capabilities in parsing HTML. It allows for easy extraction of data from Wikipedia, which is crucial for the secondary functionality of this application.

### Error Handling

To ensure a robust application, error handling was implemented to manage cases where the API request fails or the city is not found. The user is notified through message boxes, making the application more user-friendly.

## Usage

1. **Enter the City Name**: The user inputs the name of the city they want to get information about.
2. **Fetch Weather**: Clicking the "Fetch Weather" button sends a request to the OpenWeatherMap API and scrapes Wikipedia for city information.
3. **Display Information**: A new window opens displaying the current weather details and a brief summary about the city.
4. **View More**: Users can click on links to view a detailed weather report and read more about the city on Wikipedia.
