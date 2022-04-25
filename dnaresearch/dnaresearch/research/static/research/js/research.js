document.addEventListener('DOMContentLoaded', () => {
  const exportButton = document.getElementById('export-button');
  const checkboxes = document.querySelectorAll('.research-checkbox');
  const activeCheckboxes = new Set();

  const updateExportButton = () => {
    if (!activeCheckboxes.size) {
      exportButton.classList.add('disabled');
      exportButton.href = '#';
    } else {
      exportButton.classList.remove('disabled');
      exportButton.href = `/research/export/?research_id=${[...activeCheckboxes].join(',')}`;
    }
  };

  checkboxes.forEach(checkbox => {
    checkbox.addEventListener('change', event => {
      const { checked, name } = event.target;

      if (checked) {
        activeCheckboxes.add(name);
      } else {
        activeCheckboxes.delete(name);
      }

      updateExportButton();
    });
  })

  updateExportButton();
});