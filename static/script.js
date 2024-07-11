document.getElementById('tweetForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const tweetCount = document.getElementById('tweet_count').value;
    const textQuery = document.getElementById('text_query').value;
    const sinceDate = document.getElementById('since_date').value;
    const untilDate = document.getElementById('until_date').value;

    const response = await fetch('/scrape_tweets', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            tweet_count: tweetCount,
            text_query: textQuery,
            since_date: sinceDate,
            until_date: untilDate,
        }),
    });

    const data = await response.json();
    displayResults(data);
});

function displayResults(data) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '';

    data.forEach(tweet => {
        const tweetDiv = document.createElement('div');
        tweetDiv.classList.add('tweet');

        const tweetText = document.createElement('p');
        tweetText.textContent = tweet.content;

        tweetDiv.appendChild(tweetText);
        resultsDiv.appendChild(tweetDiv);
    });
}
