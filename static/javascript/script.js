// ---------------------- add workout page -----------------------------------


function submitForm() {
  document.getElementById('dateForm').submit();
}

function submitForm() {
  document.getElementById('dateForm').submit();
}


// adds a new container for an exercise
const addExerciseBtn = document.querySelector(".d-flex.justify-content-center.align-items-center");

const allExercisesContainer = document.querySelector(".all-exercises-container");

// event listener added to the addExercise button
addExerciseBtn.addEventListener("click", function (e) {

  const exerciseNumber = allExercisesContainer.querySelectorAll(".exercise-container").length + 1;
  // variable pointing to the html that is going to be added everytime the addExercise button is clicked, the code is just copy and pasted from the addWorkout page
  const html = `<div class="exercise-container">
        
    <div class="container info-container workout">
        

    <div class="exercise-title">
        <h2 class="info-container-title">
            <input class="addInput exercise-name" type="text" name="exercise-${exerciseNumber}-name"  placeholder="Exercise Name">
        </h2>

        <span class="delete-exercise"><i class="bi bi-x-square-fill"></i></span>
    
    </div>
    

    <div class="set-container">
        <span>Set 1:
            <input class="addInput set" type="number" name="exercise-${exerciseNumber}-set-1-weight"  placeholder="Weight" min="1">LBS
        </span>
        <span>
            <input class="addInput set" type="number" name="exercise-${exerciseNumber}-set-1-reps"  placeholder="Repetitions" min="1">Reps</span>
        <span>
            <input class="addInput set" type="number" name="exercise-${exerciseNumber}-set-1-rpe"  placeholder="Rate Of Percieved Exertion"  min="1" max="10">RPE</span>
        <span>
            <textarea class="addInput set" type="textarea" name="exercise-${exerciseNumber}-set-1-text"  placeholder="Notes..." rows="1"></textarea>
        </span>

        <span><button class="w-minus hidden" type="button"><i class="bi bi-dash-circle-dotted"></i></button></span>

    </div>

    <div class="set-container">
        <span>Set 2:
            <input class="addInput set" type="number" name="exercise-${exerciseNumber}-set-2-weight" placeholder="Weight" min="1">LBS
        </span>
        <span>
            <input class="addInput set" type="number" name="exercise-${exerciseNumber}-set-2-reps"  placeholder="Repetitions" min="1">Reps</span>
        <span>
            <input class="addInput set" type="number" name="exercise-${exerciseNumber}-set-2-rpe"  placeholder="Rate Of Percieved Exertion"  min="1" max="10">RPE</span>
            <span>
            <textarea class="addInput set" type="textarea" name="exercise-${exerciseNumber}-set-1-text"  placeholder="Notes..." rows="1"></textarea>
        </span>

        <span><button class="w-minus hidden" type="button"><i class="bi bi-dash-circle-dotted"></i></button></span>

    </div>

    <div class="set-container">
        <span>Set 3:
            <input class="addInput set" type="number" name="exercise-${exerciseNumber}-set-3-weight"  placeholder="Weight" min="1">LBS
        </span>
        <span>
            <input class="addInput set" type="number" name="exercise-${exerciseNumber}-set-3-reps" placeholder="Repetitions" min="1">Reps</span>
        <span>
            <input class="addInput set" type="number" name="exercise-${exerciseNumber}-set-3-rpe"  placeholder="Rate Of Percieved Exertion"  min="1" max="10">RPE</span>
            <span>
            <textarea class="addInput set" type="textarea" name="exercise-${exerciseNumber}-set-1-text"  placeholder="Notes..." rows="1"></textarea>
        </span>

            <span><button class="w-minus" type="button"><i class="bi bi-dash-circle-dotted"></i></button></span>
    </div>

    
    <div>
        <span class="preview-set">Set #:
            <input class="addInput set" type="number" name="set-4-weight"  placeholder="Weight" disabled>LBS
        </span>
        <span class="preview-set">
            <input class="addInput set" type="number" name="set-4-reps" placeholder="Repetitions" disabled>Reps</span>
        <span class="preview-set">
            <input class="addInput set" type="number" name="set-4-rpe" placeholder="Rate Of Percieved Exertion" disabled>RPE</span>
            <span class="preview-set">
            <textarea class="addInput set" type="textarea" name="set-1-text"  placeholder="Notes..." rows="1" disabled></textarea>
        </span>

            <span><button class="w-plus" type="button"><i class="bi bi-plus-circle-dotted"></i></button></span>

    </div>


</div>

</div>`;

  // grabbing the container that holds all of the exercise containers
  const allExerciseContainer = document.querySelector(
    ".all-exercises-container"
  );

  // inserting the html variable with our boiler plate exercise container code right before the end of the allExerciseContainer,
  allExerciseContainer.insertAdjacentHTML("beforeend", html);
});

// deletes an exercise
document.addEventListener("click", function (event) {
  // using if statement to see if the click matches the button instead of adding the listener to all buttons because exercise containers can be dynamically added so this approach is more dynamic to accomodate that
  if (event.target.matches(".bi.bi-x-square-fill")) {
    const exerciseContainer = event.target.closest(".exercise-container");

    // removes exercise container that is closest to the click event
    exerciseContainer.remove();
  }
});

//  adds a set
document.addEventListener("click", function (event) {
  // checking if click matches the addSet button, again for a more dynamic approach with the add buttons
  if (event.target.matches(".bi.bi-plus-circle-dotted")) {
    const currentExerciseContainer = event.target.closest(".exercise-container");
    const repDivElement = event.target.closest("div");
    const allExerciseContainers = document.querySelectorAll(".exercise-container");

    let exerciseNumber = 0;
    for (let i = 0; i < allExerciseContainers.length; i++) {
      if (allExerciseContainers[i] === currentExerciseContainer) {
        exerciseNumber = i + 1;
        break;
      }
    }

    // counting the number of set containers including the one that is about to be added so we can use it to dynamically name the set numbers when displaying them
    const setNumber = currentExerciseContainer.querySelectorAll(".set-container").length + 1;
      
    const exerciseName = currentExerciseContainer.querySelector('input[name^="exercise-"]').name;

    // variable with html code to be used to add to the document, pertaining to a new set
    const newSetHTML = `
    <div class="set-container">
    <span>Set ${setNumber}:
        <input class="addInput set" type="number" name="exercise-${exerciseNumber}-set-${setNumber}-weight"  placeholder="Weight" min="1">LBS
    </span>
    <span>
        <input class="addInput set" type="number" name="exercise-${exerciseNumber}-set-${setNumber}-reps"  placeholder="Repetitions" min="1">Reps</span>
    <span>
        <input class="addInput set" type="number" name="exercise-${exerciseNumber}-set-${setNumber}-rpe"  placeholder="Rate Of Percieved Exertion"  min="1" max="10">RPE</span>
        <span>
            <textarea class="addInput set" type="textarea" name="exercise-${exerciseNumber}-set-${setNumber}-text"  placeholder="Notes..." rows="1"></textarea>
        </span>

        <span><button class="w-minus" type="button"><i class="bi bi-dash-circle-dotted"></i></button></span>
</div>`;

    // adds new set code before the preview set begins
    repDivElement.insertAdjacentHTML("beforebegin", newSetHTML);

    // updates the minus button after a set is added, puts the minus button at the last set
    const allSets = currentExerciseContainer.querySelectorAll(".set-container");
    const oldLastSet = allSets[allSets.length - 2];
    const minusButton = oldLastSet.querySelector(".w-minus");
    minusButton.classList.toggle("hidden");
  }
});

// removes a set
document.addEventListener("click", function (event) {
  // checking if the click event matches the minus button
  if (event.target.matches(".bi.bi-dash-circle-dotted")) {
    const currentExerciseContainer = event.target.closest(
      ".exercise-container"
    );
    const targetedDeletedElement = event.target.closest(".set-container");
    if (targetedDeletedElement) {
      targetedDeletedElement.remove();
    }

    //    updating the minus button to the last child of the exercise container
    const allSets = currentExerciseContainer.querySelectorAll(".set-container");
    if (allSets.length > 0) {
      const lastSet = allSets[allSets.length - 1];
      const minusButton = lastSet.querySelector(".w-minus");
      minusButton.classList.toggle("hidden");
    }
  }
});


// ------------------------- add workout page -----------------------------

//----------------------------workout page --------------------------------

// ---------------------------  workout page --------------------------------------
