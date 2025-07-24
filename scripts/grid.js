import { sectionStates } from './config.js';
import { handleOnClick } from './animation.js';

export function createTile(index, sectionId) {
  const tile = document.createElement("div");
  tile.classList.add("tile");

  const state = sectionStates[sectionId];
  tile.style.opacity = state.toggled ? 0 : 1;

  tile.onclick = () => handleOnClick(index, sectionId);

  return tile;
}

export function createTiles(quantity, sectionId) {
  const state = sectionStates[sectionId];
  const tilesWrapper = document.getElementById(state.tilesId);

  Array.from({ length: quantity }).forEach((_, index) => {
    tilesWrapper.appendChild(createTile(index, sectionId));
  });
}

export function createGrid(sectionId) {
  const state = sectionStates[sectionId];
  const tilesWrapper = document.getElementById(state.tilesId);
  tilesWrapper.innerHTML = "";

  const size = document.body.clientWidth > 800 ? 100 : 50;

  state.columns = Math.floor(document.body.clientWidth / size);
  state.rows = Math.floor(document.body.clientHeight / size);

  tilesWrapper.style.setProperty("--columns", state.columns);
  tilesWrapper.style.setProperty("--rows", state.rows);

  createTiles(state.columns * state.rows, sectionId);
}
