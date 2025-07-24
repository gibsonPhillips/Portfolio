import { sectionStates } from './config.js';

export function toggle(sectionId) {
  const state = sectionStates[sectionId];
  state.toggled = !state.toggled;

  const section = document.getElementById(sectionId);
  section.classList.toggle("toggled");
}

export function handleOnClick(index, sectionId) {
  toggle(sectionId);

  const state = sectionStates[sectionId];
  const tilesWrapper = document.getElementById(state.tilesId);

  anime({
    targets: tilesWrapper.querySelectorAll(".tile"),
    opacity: state.toggled ? 0 : 1,
    delay: anime.stagger(50, {
      grid: [state.columns, state.rows],
      from: index
    })
  });
}
