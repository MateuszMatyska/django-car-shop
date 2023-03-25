function searchingCars() {
    const searching_input = document.getElementById('search-input').value;
    const index = searching_input.indexOf('<')
    if (index < 0) {
        if (searching_input) {
            location.href=`/search_cars/${searching_input}`
        }
    }
}