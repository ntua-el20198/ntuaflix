async function displayMovieResults(movie, movieContainer) {

    // Clear previous movie
    movieContainer.innerHTML = '';

    const titleContainer = document.createElement('div');
    titleContainer.classList.add('movieTitleContainer');
    const titleElement = document.createElement('h2'); // Using h2 for title
    titleElement.textContent = movie.originalTitle;
    titleContainer.appendChild(titleElement);

    const bigContainerElement = document.createElement('div');
    bigContainerElement.classList.add('bigContainer');

    const containerElement = document.createElement('div');
    containerElement.classList.add('mediumContainer');

    const posterSrc = movie.titlePoster ? movie.titlePoster : '/static/images/default.jpg';
    const posterElement = document.createElement('img');
    posterElement.src = posterSrc.replace('{width_variable}', 'w500');
    posterElement.classList.add('row__poster2');

    bigContainerElement.appendChild(posterElement);

    const smallContainerElement = document.createElement('div');
    smallContainerElement.classList.add('smallContainer');
    // Create a div for movie information
    const movieInfoElement = document.createElement('div');
    movieInfoElement.classList.add('movieInfo2');

    const typeElement = document.createElement('p');
    typeElement.textContent = `Type: ${movie.type}`;
    movieInfoElement.appendChild(typeElement);

    const startYearElement = document.createElement('p');
    startYearElement.textContent = `Start Year: ${movie.startYear}`;
    movieInfoElement.appendChild(startYearElement);

    const genresElement = document.createElement('p');
    genresElement.textContent = `Genres: ${movie.genres.join(', ')}`;
    movieInfoElement.appendChild(genresElement);

    smallContainerElement.appendChild(movieInfoElement);

    // Ensure createListButton is defined
    const ratingContainer = document.createElement('div');
    ratingContainer.classList.add('ratingContainer');

    // ratingButtonContainer.insertBefore(starRating, ratingButtonContainer.firstChild);
    const ratingElement = document.createElement('h3');
    ratingElement.textContent = `${movie.rating ? movie.rating.avRating : 'N/A'} (${movie.rating ? movie.rating.numVotes : '0'} votes)`;

    // Create a container for the buttons
    const buttonsContainer = document.createElement('div');
    buttonsContainer.classList.add('buttonsContainer');

    async function createContent() {
        const likeButton = await createLikeButton(movie);
        const listButton = await createListButton(movie);

        buttonsContainer.appendChild(listButton);
        buttonsContainer.appendChild(likeButton);

        const yourRatingContainer = document.createElement('div');
        yourRatingContainer.classList.add('yourRatingContainer')
        const starRating = createStarRating();
        yourRatingContainer.appendChild(starRating)
        const commentBox = createCommentBox();
        yourRatingContainer.appendChild(commentBox);

        ratingContainer.appendChild(ratingElement);

        ratingContainer.appendChild(buttonsContainer);

        smallContainerElement.appendChild(ratingContainer);

        containerElement.appendChild(smallContainerElement);

        containerElement.appendChild(yourRatingContainer);

        bigContainerElement.appendChild(containerElement);
    }
    createContent();
    movieContainer.appendChild(titleContainer);
    //movieContainer.appendChild(containerElement);
    movieContainer.appendChild(bigContainerElement);


    console.log('listButton type:', typeof listButton, listButton);
    console.log('likeButton type:', typeof likeButton, likeButton);

    function createStarRating() {
        const starRatingContainer = document.createElement('div');
        starRatingContainer.className = 'star-rating';

        for (let i = 10; i >= 1; i--) {
            const starInput = document.createElement('input');
            starInput.type = 'radio';
            starInput.id = `star${i}`;
            starInput.name = 'rating';
            starInput.value = i;

            starInput.setAttribute('title', i);

            const starLabel = document.createElement('label');
            starLabel.htmlFor = `star${i}`;
            starLabel.title = `${i} stars`;
            starLabel.textContent = '★';

            starRatingContainer.appendChild(starInput);
            starRatingContainer.appendChild(starLabel);
        }

        return starRatingContainer;
    }

    function createCommentBox() {
        // Create the container for the comment box
        const commentBoxContainer = document.createElement('div');
        commentBoxContainer.classList.add('comment-box');

        // Create the form element
        const formElement = document.createElement('form');
        formElement.id = 'commentForm';

        // Create the textarea element
        const textareaElement = document.createElement('textarea');
        textareaElement.id = 'commentInput';
        textareaElement.placeholder = 'Add your comment here...';

        // Create the submit button
        const submitButton = document.createElement('button');
        submitButton.type = 'submit';
        submitButton.textContent = 'Submit';

        submitButton.addEventListener('click', function (event) {
            event.preventDefault(); // Prevent the default form submission behavior
            submitForm(); // Call your submitForm function when the button is clicked
        });


        // Append textarea and submit button to the form
        formElement.appendChild(textareaElement);
        formElement.appendChild(submitButton);

        // Append the form to the comment box container
        commentBoxContainer.appendChild(formElement);

        return commentBoxContainer;
    }

    function getSelectedRating() {
        const selectedRatingInput = document.querySelector('input[name="rating"]:checked');
        
        if (selectedRatingInput) {
            const titleAttribute = selectedRatingInput.getAttribute('title');
            if (titleAttribute !== null) {
                return parseInt(titleAttribute, 10);  // Return the stars as a string
            }
        } else {
            return '0';  // Return a default value when no rating is selected
        }
    }

    function getComment() {
        return document.getElementById('commentInput').value.trim();
    }

    function submitForm() {
        const titleID = movie.titleID;
        const rating = getSelectedRating();
        const comment = getComment();

        // Send an asynchronous request to your backend
        fetch(`/ntuaflix_api/rating/${titleID}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                rating: rating,
                comment: comment,
            }),
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                console.log('Rating added successfully:', data.message);
            })
            .catch(error => {
                console.error('Error adding rating:', error.message);
            });
    }


}