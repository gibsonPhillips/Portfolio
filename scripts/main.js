import { sections } from './config.js';
import { createGrid } from './grid.js';
import { setupKeyboardNavigation } from './scroll.js';

window.addEventListener('DOMContentLoaded', () => {
  sections.forEach(section => createGrid(section.id));

  setupKeyboardNavigation();

  window.onresize = () => {
    sections.forEach(section => createGrid(section.id));
  };
});
