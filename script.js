document.getElementById('input-form').addEventListener('submit', function(event) {
  event.preventDefault();

  const userInput = {
    'AGE': document.getElementById('age').value,
    'Interest': document.getElementById('interest').value,
    'Bạn đi với': document.getElementById('companions').value,
    'Visiting time': document.getElementById('visiting-time').value,
    'sex': document.getElementById('sex').value,
    'Desired amount': document.getElementById('desired-amount').value
  };

  fetch('/recommend', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(userInput)
  })
    .then(response => response.json())
    .then(data => {
      const outputContainer = document.getElementById('output');
      outputContainer.innerHTML = '';

      const heading = document.createElement('h2');
      heading.textContent = 'Recommended Places:';
      outputContainer.appendChild(heading);

      const placesList = document.createElement('ul');
      data.top_recommended_places.forEach(place => {
        const listItem = document.createElement('li');
        listItem.textContent = place;
        placesList.appendChild(listItem);
      });
      outputContainer.appendChild(placesList);
    })
    .catch(error => {
      console.error('Error:', error);
    });
});
