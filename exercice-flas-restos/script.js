window.addEventListener("DOMContentLoaded", function () {
    let form = document.querySelector(.form)
    form.addEventListener("submit", function (event) {
        event.preventDefault()
        fetch("http://127.0.0.1:5000/api/restos")
    })
})