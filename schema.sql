CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE Users (
    userID UUID PRIMARY KEY,
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255)
    name VARCHAR(255), 
    age INT, 
    height VARCHAR(10),  
    weight INT, 
    goal VARCHAR(50) 
);

CREATE TABLE Workout (
                         workoutID UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                         userID UUID REFERENCES Users(userID),
                         name VARCHAR(255),
                         date TIMESTAMP
);

CREATE TABLE Exercise (
                          exerciseID SERIAL PRIMARY KEY,
                          workoutID UUID REFERENCES Workout(workoutID),
                          exerciseName VARCHAR(255)
);




CREATE TABLE Set (
                     setID SERIAL PRIMARY KEY,
                     exerciseID INT REFERENCES Exercise(exerciseID),
                     weight INT,
                     rpe INT,
                     note TEXT,
                     reps INT
);


CREATE TABLE Meal (
    meal_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    meal_name VARCHAR(255),
    userID UUID REFERENCES Users(userID),
    FoodID VARCHAR(255),
    date TIMESTAMP
);

CREATE TABLE Food (
    FoodID UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    createdByID UUID REFERENCES Users(userID),
    Name VARCHAR(255) UNIQUE,
    Calories VARCHAR(255),
    Total_Fat VARCHAR(255),
    saturated_fat VARCHAR(255),
    trans_fat VARCHAR(255),
    cholesterol VARCHAR(255),
    sodium VARCHAR(255),
    carbohydrates VARCHAR(255),
    sugars VARCHAR(255),
    protein VARCHAR(255)
);

CREATE TABLE comments (
                          id SERIAL PRIMARY KEY,
                          comment_text TEXT,
                          date_posted DATE,
                          user_id UUID REFERENCES users(userID),
                          food_id UUID REFERENCES food(FoodID)
);