export const sections = [
    { id: 'section-1', tilesId: 'tiles-1', title: 'Project 1' },
    { id: 'section-2', tilesId: 'tiles-2', title: 'Project 2' },
    { id: 'section-3', tilesId: 'tiles-3', title: 'Project 3' }
  ];
  
  export const sectionStates = {};
  
  sections.forEach(section => {
    sectionStates[section.id] = {
      columns: 0,
      rows: 0,
      toggled: false,
      tilesId: section.tilesId
    };
  });
  