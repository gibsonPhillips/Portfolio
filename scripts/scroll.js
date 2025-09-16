import { sections } from './config.js';

const inferredSections = document.querySelectorAll(".section");

function calculateCurrentSection() {
  let minDistance = Infinity;
  let index = 0;

  inferredSections.forEach((section, i) => {
    const distance = Math.abs(section.getBoundingClientRect().top);
    if (distance < minDistance) {
      minDistance = distance;
      index = i;
    }
  });

  return index;
}


// navigate sections with arrows
export function setupKeyboardNavigation() {
  document.addEventListener('keydown', (e) => {
    const currentSection = calculateCurrentSection();

    if (e.key === 'ArrowDown' && currentSection < sections.length - 1) {
      e.preventDefault();
      document.getElementById(sections[currentSection + 1].id).scrollIntoView({ behavior: 'smooth' });
    } else if (e.key === 'ArrowUp' && currentSection > 0) {
      e.preventDefault();
      document.getElementById(sections[currentSection - 1].id).scrollIntoView({ behavior: 'smooth' });
    }
  });
}


// make scrolling with mouse just navigate through sections just like with arrows
let scrollLocked = false;
let cooldownTime = 1000;
export function setupScrollingNavigation() {
  document.addEventListener('wheel', (e) => {
    
    // handles input overflow for smooth nav
    if (scrollLocked) {
      e.preventDefault();
      return;
    }

    const currentSection = calculateCurrentSection();

    // console.log(`e.deltaY ${e.deltaY} scrollLocked: ${scrollLocked}`)

    if (e.deltaY > 0 && currentSection < sections.length - 1) {
      // scrollign down I believe

      scrollLocked = true;
      e.preventDefault();
      document.getElementById(sections[currentSection + 1].id).scrollIntoView({ behavior: 'smooth' });
    } else if (e.deltaY < 0 && currentSection > 0) {
      // scrolling up

      scrollLocked = true;
      e.preventDefault();
      document.getElementById(sections[currentSection - 1].id).scrollIntoView({ behavior: 'smooth' });
    }

    setTimeout(() => scrollLocked = false, cooldownTime); 
  }, { passive: false });
}
