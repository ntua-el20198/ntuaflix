function createListButton(result) {
    const addToListButton = document.createElement('button');
    addToListButton.innerHTML = '<div class="icon">+</div>';
    addToListButton.classList.add('addToListButton', 'empty');
    addToListButton.addEventListener('click', function () {
        toggleAddToList(result.titleID, addToListButton);
    });
    return addToListButton;
}

function toggleAddToList(titleID, button) {
    // Toggle the add to list status and update the button appearance
    if (button.classList.contains('empty')) {
        // If not added, make it added (tick icon)
        button.innerHTML = '<div class="icon">&#10003;</div>';
        button.classList.remove('empty');
        button.classList.add('added');
        // Call the function to handle the add to list operation
        addToWatchlist(titleID);
    } else {
        // If already added, make it not added (plus icon)
        button.innerHTML = '<div class="icon">+</div>';
        button.classList.remove('added');
        button.classList.add('empty');
        // Call the function to handle the remove from list operation
        removeFromWatchlist(titleID);
    }
}

function addToWatchlist(titleID) {
    fetch('/get_user_id')
        .then(response => response.json())
        .then(data => {
            const userID = data;
            console.log('User ID:', userID);

            if (!userID) {
                alert('Please log in to add movies to your watchlist');
                return;
            }

            fetch(`/add_to_list/${titleID}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ userID: userID }),
            })
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function removeFromWatchlist(titleID) {
    fetch('/get_user_id')
        .then(response => response.json())
        .then(data => {
            const userID = data;
            console.log('User ID:', userID);

            if (!userID) {
                alert('Please log in to manage your watchlist');
                return;
            }

            fetch(`/remove_from_list/${titleID}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ userID: userID }),
            })
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        })
        .catch(error => {
            console.error('Error:', error);
        });
}