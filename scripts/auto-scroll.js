const codeBlock = document.getElementById('scrolling-code');

function loopScroll() {
    codeBlock.scrollTo({
        top: codeBlock.scrollHeight,
        behavior: 'smooth'
    });
    console.log("here")

    // Wait for the scroll to bottom to finish, then scroll to top
    setTimeout(() => {
        codeBlock.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }, 3000); // scroll duration

    // loopset
    setTimeout(loopScroll, 600);
}

window.addEventListener('DOMContentLoaded', loopScroll);