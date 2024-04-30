CREATE TABLE Users (
    userID UUID PRIMARY KEY,
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255)
);

CREATE TABLE Workout (
    workoutID UUID PRIMARY KEY,
    userID UUID REFERENCES Users(userID),
    name VARCHAR(255),
    date TIMESTAMP
);

CREATE TABLE Exercise (
    exerciseID SERIAL PRIMARY KEY,
    workoutID INT REFERENCES Workout(workoutID),
    exerciseName VARCHAR(255)
);

CREATE TABLE Set (
    setID SERIAL PRIMARY KEY,
    exerciseID INT REFERENCES Exercise(exerciseID),
    weight INT,
    rpe INT,
    note TEXT,
    reps INT,
    imageID INT 
);

CREATE TABLE Meal (
    meal_name VARCHAR(255) PRIMARY KEY,
    userID UUID REFERENCES Users(userID),
    FoodID VARCHAR(255), -- Assuming this should be a foreign key
    date TIMESTAMP
);

CREATE TABLE Food (
    FoodID SERIAL PRIMARY KEY,
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
