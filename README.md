<div style="text-align: center;">
  <img src="frontend/public/logo.svg" alt="MeteoGlobe Logo">
</div>

MeteoGlobe is a web application built with Django and Vue.js that allows users to visualize meteorite data on a 3D globe. The application uses the three-globe to display a 3D globe and NASA's meteorites dataset to show meteorite landings on the Earth's surface. Users can apply various filters to explore meteorites based on their year of discovery, country of discovery, chemical composition, and more.

## Features

- 3D Globe Visualization: MeteoGlobe uses three-globe to render a 3D representation of the Earth, making it an engaging and interactive experience for users.

- Meteorite Data: The application fetches meteorite data from NASA's dataset, providing comprehensive information about meteorite landings, including location, year, mass, and composition.

- Custom Filters: Users can apply filters to the meteorite data, allowing them to narrow down their search based on criteria such as the year the meteorite was found, the country of discovery, and the chemical composition.

## Getting Started

Follow these steps to get the MeteoGlobe project up and running on your local machine:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/ImadSaddik/MeteoGlobe.git
   cd MeteoGlobe
   ```

2. **Create a Python Virtual Environment:**

   It's recommended to use a virtual environment to manage project dependencies.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. **Install Python Dependencies:**

   Use pip to install the required Python packages.

   ```bash
   cd backend
   pip install -r requirements.txt
   ```

4. **Install JavaScript Dependencies:**

   Navigate to the `frontend` directory and install JavaScript dependencies.

   ```bash
   cd frontend
   npm install
   ```

5. **Run the Development Servers:**

   In one terminal, start the Django backend server.

   ```bash
   cd backend
   python manage.py runserver
   ```

   In another terminal, start the Vue.js development server.

   ```bash
   cd frontend
   npm run serve
   ```

6. **Access the Application:**

   Open your web browser and visit `http://localhost:8080` to access the MeteoGlobe application.

## Usage

1. Visit the MeteoGlobe website.
2. Explore the 3D globe and use the filter options to narrow down meteorite data based on your preferences.

## Contributing

If you'd like to contribute to the project, please follow these guidelines:

1. Fork the repository on GitHub.
2. Create a new branch and make your changes.
3. Submit a pull request, explaining the purpose of your changes.

## Acknowledgments

- Thanks to NASA for providing the meteorite dataset.
- Three.js: https://threejs.org/
- Three globe: https://github.com/vasturiano/three-globe
- Django: https://www.djangoproject.com/
- Vue.js: https://vuejs.org/

## Contact

If you have any questions or feedback, feel free to reach out to the project owner:
Email: simad3647@gmail.com

Happy exploring meteorites with MeteoGlobe! 🌍💫
