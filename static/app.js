$("form").on('click', "button", (evt)=> {
    // Check for empty fields
    const $fields = $("input").get()
    let missingInputs = $fields.filter(field => field.value === "")
    
    // Prevent form submission if there are any empty fields
    if (missingInputs.length >= 1) {
        evt.preventDefault();
        missingInputs.map(input => {
            input.classList.add("emptyInput")
            input.setAttribute("placeholder", "Fill me out!")
        })
    }
})

// Remove red border after updating value of input
$("form").on("change", "input", (evt) => {
    const input = evt.target
    input.classList.remove("emptyInput")
})