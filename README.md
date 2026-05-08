# Flight-Ticket-Price-Prediction

### Project Overview

This project builds a Machine Learning model to predict flight ticket prices based on different flight-related factors such as airline, source, destination, duration, travel class, number of stops, and timing details.

The system helps customers identify better booking prices and supports airlines and travel platforms in implementing intelligent pricing strategies.

### Business Objective
* Predict flight ticket prices accurately
* Help customers choose the best booking time
* Support airline dynamic pricing strategies
* Improve customer booking experience
* Enable data-driven pricing decisions

### Dataset Information
* Total Records: 300,261
* Features: 14 (after preprocessing)

#### Key Features:
* Flight Features: Airline, Flight Code, Travel Class
* Route Features: Source, Destination, Number of Stops
* Time Features: Departure Time, Arrival Time, Month Name, Day Type
* Duration Features: Journey Duration
* Target Variable: price (Flight Ticket Price)

### Tech Stack
* Programming: Python
* Libraries:
    pandas, numpy
    scikit-learn
    xgboost
    streamlit
* Deployment: Streamlit + Hugging Face Spaces

### ML Workflow (CRISP-ML(Q))
1) Business Understanding
2) Data Preprocessing
3) Feature Engineering
4) Model Building
5) Evaluation
6) Hyperparameter Tuning
7) Deployment

### Data Preprocessing
* Performed:
    * Combined Economy and Business datasets
    * Handled date and time features
    * Converted duration into minutes
    * Converted stop feature into numerical format
    * Created: day_type, month_name, flight_code
* Encoded categorical features using:
     OneHotEncoder (Nominal)
     OrdinalEncoder (class)
* Applied:
     StandardScaler
     PowerTransformer (Yeo-Johnson)
* Used Pipeline & ColumnTransformer for automation

### Models Implemented
* Linear Regression
* KNN
* Decision Tree
* Random Forest
* Gradient Boosting
* XGBoost

### Final Model: XGBoost (Tuned)
#### Performance:
* Train R²: 0.981
* Test R²: 0.978
* Test RMSE: 3119

### Cross Validation
* Used K-Fold (k=5)
* Achieved stable and consistent performance

### Hyperparameter Tuning
* Method Used: GridSearchCV
* Best Parameters:
   * Learning Rate = 0.1
   * Max Depth = 7
   * Number of Estimators = 300

## Model Deployment
### Streamlit App Features:
### User-friendly UI
* Input fields for:
      Airline
      Source
      Destination
      Stops
      Class
      Duration
      Timing Details
* Outputs:
      Predicted Flight Ticket Price

### Key Insights
* Travel class is the most influential feature
* Flight duration strongly impacts ticket prices
* Airlines and routes significantly affect pricing
* Weekend and seasonal demand increase ticket prices
* Direct flights are generally more expensive

### 🚀 Future Improvements
* Integrate real-time flight APIs
* Add deep learning models (ANN, TabNet)
* Implement real-time fare monitoring
* Add fare trend forecasting
* Deploy cloud-based real-time prediction system
