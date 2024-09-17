const bubbles = document.querySelectorAll('.bubble');

// Randomize the delay and duration of each bubble's float animation
bubbles.forEach((bubble) => {
    const randomDelay = Math.random() * 5;  // Random delay (0-5s)
    const randomDuration = 5 + Math.random() * 5;  // Random animation duration (5-10s)

    bubble.style.animationDelay = `${randomDelay}s`;
    bubble.style.animationDuration = `${randomDuration}s`;
});