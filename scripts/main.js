import { sections } from './config.js';
import { createGrid } from './grid.js';
import { setupKeyboardNavigation, setupScrollingNavigation } from './scroll.js';

// inits the grid creation, keyboard nav, and 
window.addEventListener('DOMContentLoaded', () => {
  sections.forEach(section => createGrid(section.id));

  setupKeyboardNavigation();
  setupScrollingNavigation();

  window.onresize = () => {
    sections.forEach(section => createGrid(section.id));
  };
});
