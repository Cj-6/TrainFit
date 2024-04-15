
// ---------------------- add workout page -----------------------------------



// adds a new container for an exercise 
const addExerciseBtn = document.querySelector('.d-flex.justify-content-center.align-items-center');
addExerciseBtn.addEventListener('click', function() {
   
    
    const html = `<div class="exercise-container">
        
    <div class="container info-container">
        

    <div class="exercise-title">
        <h2 class="info-container-title">
            <input class="addInput exercise" type="text" name="exerciseName"  placeholder="Exercise Name">
        </h2>

        <span class="delete-exercise"><i class="bi bi-x-square-fill"></i></span>
    
    </div>
    <hr>

    <div class="set-container">
        <span>Set 1:
            <input class="addInput set" type="number" name="set-1-weight"  placeholder="Weight">LBS
        </span>
        <span>
            <input class="addInput set" type="number" name="set-1-reps"  placeholder="Repetitions">Reps</span>
        <span>
            <input class="addInput set" type="number" name="set-1-rpe"  placeholder="Rate Of Percieved Exertion">RPE</span>
        <span>
            <textarea class="addInput set" type="textarea" name="set-1-text"  placeholder="Notes..." rows="1"></textarea>
        </span>

        <span><button class="w-minus" type="button"><i class="bi bi-dash-circle-dotted"></i></button></span>

    </div>

    <div class="set-container">
        <span>Set 2:
            <input class="addInput set" type="number" name="set-2-weight" placeholder="Weight">LBS
        </span>
        <span>
            <input class="addInput set" type="number" name="set-2-reps"  placeholder="Repetitions">Reps</span>
        <span>
            <input class="addInput set" type="number" name="set-2-rpe"  placeholder="Rate Of Percieved Exertion">RPE</span>
            <span>
            <textarea class="addInput set" type="textarea" name="set-1-text"  placeholder="Notes..." rows="1"></textarea>
        </span>

        <span><button class="w-minus" type="button"><i class="bi bi-dash-circle-dotted"></i></button></span>

    </div>

    <div class="set-container">
        <span>Set 3:
            <input class="addInput set" type="number" name="set-3-weight"  placeholder="Weight">LBS
        </span>
        <span>
            <input class="addInput set" type="number" name="set-3-reps" placeholder="Repetitions">Reps</span>
        <span>
            <input class="addInput set" type="number" name="set-3-rpe"  placeholder="Rate Of Percieved Exertion">RPE</span>
            <span>
            <textarea class="addInput set" type="textarea" name="set-1-text"  placeholder="Notes..." rows="1"></textarea>
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
            <textarea class="addInput set" type="textarea" name="set-1-text"  placeholder="Notes..." rows="1"></textarea>
        </span>

            <span><button class="w-plus" type="button"><i class="bi bi-plus-circle-dotted"></i></button></span>

    </div>


</div>

</div>
    `;
    const exerciseContainer = document.querySelector('.exercise-container');

    exerciseContainer.insertAdjacentHTML('beforeend', html);
});

// deletes an exercise
document.addEventListener('click', function(event) {
    if(event.target.matches('.bi.bi-x-square-fill')) {
        const exerciseContainer = event.target.closest('.exercise-container');

        if(exerciseContainer){
            exerciseContainer.remove();
        }
    }
});

//  adds a set
document.addEventListener('click', function(event){
    if(event.target.matches('.bi.bi-plus-circle-dotted')){
        const currentExerciseContainer = event.target.closest('.exercise-container');
        const repDivElement = event.target.closest('div');
        
        const setNumber = currentExerciseContainer.querySelectorAll('.set-container').length + 1;
    const newSetHTML = `
    <div class="set-container">
    <span>Set ${setNumber}:
        <input class="addInput set" type="number" name="set-${setNumber}-weight"  placeholder="Weight">LBS
    </span>
    <span>
        <input class="addInput set" type="number" name="set-${setNumber}-reps"  placeholder="Repetitions">Reps</span>
    <span>
        <input class="addInput set" type="number" name="set-${setNumber}-rpe"  placeholder="Rate Of Percieved Exertion">RPE</span>
        <span>
            <textarea class="addInput set" type="textarea" name="set-${setNumber}-text"  placeholder="Notes..." rows="1"></textarea>
        </span>

        <span><button class="w-minus" type="button"><i class="bi bi-dash-circle-dotted"></i></button></span>
</div>`;
    
    repDivElement.insertAdjacentHTML('beforebegin', newSetHTML);

    }
});

// removes a set
document.addEventListener('click', function(event){
    if(event.target.matches('.bi.bi-dash-circle-dotted')){
        const targetedDeletedElement = event.target.closest('.set-container');
        if(targetedDeletedElement){
            targetedDeletedElement.remove();
        }
    }
});


// ------------------------- add workout page -----------------------------

