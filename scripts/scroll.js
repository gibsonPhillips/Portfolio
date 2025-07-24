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
