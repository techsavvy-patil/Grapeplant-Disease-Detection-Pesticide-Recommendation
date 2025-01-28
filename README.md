# Grapeplant Disease Detection and Pesticide Recommendation

## Overview
This project is designed to detect diseases in grape plants using advanced machine learning techniques and recommend the appropriate pesticides to address the detected issues. The aim is to assist farmers and agricultural experts in maintaining healthy crops and improving yield.

## Features
- **Disease Detection**: Accurately identify common grape plant diseases using images of grape leaves.
- **Pesticide Recommendation**: Suggest suitable pesticides based on the detected disease.
- **User-Friendly Interface**: Easily upload images and get results through a streamlined workflow.
- **Scalable Architecture**: Built to handle large datasets and multiple disease categories.

## Technologies Used
- **Programming Language**: Python
- **Machine Learning**: TensorFlow, PyTorch, Scikit-Learn
- **Image Processing**: OpenCV
- **Web Framework**: Flask
- **Dataset**: Publicly available grape leaf disease datasets

## Getting Started
Follow these steps to set up and run the project:

### Prerequisites
- Python 3.8+
- Virtual environment tools (e.g., `venv`, `conda`)
- Libraries: Install dependencies

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Grapeplant-Disease-Detection-Pesticide-Recommendation.git
   cd Grapeplant-Disease-Detection-Pesticide-Recommendation
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. Launch the application:
   ```bash
   python app.py
   ```
2. Open your web browser and navigate to `http://localhost:5000`.
3. Upload a grape leaf image and receive disease detection results along with pesticide recommendations.

## Dataset
The project uses a dataset of grape leaf images, annotated with labels for healthy leaves and various diseases. If you are using a public dataset, include details such as the source, size, and license.

## Model Training
To train the model:
1. Prepare the dataset by organizing it into training, validation, and test sets.
2. Run the training script:
   ```bash
   python train.py
   ```
3. The trained model will be saved in the `models/` directory.

``
## Future Enhancements
- Expand disease detection to include more grape plant diseases.
- Incorporate real-time detection using smartphone cameras.
- Provide multilingual support for global usability.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature/bugfix.
3. Submit a pull request with a detailed description of your changes.
