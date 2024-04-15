// for addWorkout page, adds a new container for an exercise 
const addExerciseBtn = document.querySelector('.d-flex.justify-content-center.align-items-center');
addExerciseBtn.addEventListener('click', function() {
   
    
    const html = `<div class="exercise-container">
        
    <div class="container info-container">
        

    <div class="exercise-title">
        <h2 class="info-container-title">
            <input class="addInput exercise" type="text" name="exerciseName" required placeholder="Exercise Name">
        </h2>

        <span><i class="bi bi-x-square-fill"></i></span>
    
    </div>
    <hr>

    <div>
        <span>Set 1:
            <input class="addInput set" type="number" name="set-1-weight" required placeholder="Weight">LBS
        </span>
        <span>
            <input class="addInput set" type="number" name="set-1-reps" required placeholder="Repetitions">Reps</span>
        <span>
            <input class="addInput set" type="number" name="set-1-rpe" required placeholder="Rate Of Percieved Exertion">RPE</span>

            <span><button class="w-minus"></span><i class="bi bi-dash-circle-dotted"></i></button></span>
    </div>

    <div>
        <span>Set 2:
            <input class="addInput set" type="number" name="set-2-weight" required placeholder="Weight">LBS
        </span>
        <span>
            <input class="addInput set" type="number" name="set-2-reps" required placeholder="Repetitions">Reps</span>
        <span>
            <input class="addInput set" type="number" name="set-2-rpe" required placeholder="Rate Of Percieved Exertion">RPE</span>

            <span><button class="w-minus"><i class="bi bi-dash-circle-dotted"></i></button></span>
    </div>

    <div>
        <span>Set 3:
            <input class="addInput set" type="number" name="set-3-weight" required placeholder="Weight">LBS
        </span>
        <span>
            <input class="addInput set" type="number" name="set-3-reps" required placeholder="Repetitions">Reps</span>
        <span>
            <input class="addInput set" type="number" name="set-3-rpe" required placeholder="Rate Of Percieved Exertion">RPE</span>

            <span><button class="w-minus"><i class="bi bi-dash-circle-dotted"></i></button></span>
    </div>

    
    <div>
        <span class="preview-set">Set 4:
            <input class="addInput set" type="number" name="set-4-weight" required placeholder="Weight" disabled>LBS
        </span>
        <span class="preview-set">
            <input class="addInput set" type="number" name="set-4-reps" required placeholder="Repetitions" disabled>Reps</span>
        <span class="preview-set">
            <input class="addInput set" type="number" name="set-4-rpe" required placeholder="Rate Of Percieved Exertion" disabled>RPE</span>

            <span><button class="w-minus"><i class="bi bi-plus-circle-dotted"></i></button></span>

    </div>


</div>

</div>
    `;
    const exerciseContainer = document.querySelector('.exercise-container');

    exerciseContainer.insertAdjacentHTML('beforeend', html);
});

// for addWorkout page, deletes an exercise




