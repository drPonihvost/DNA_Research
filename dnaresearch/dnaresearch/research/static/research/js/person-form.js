document.addEventListener('DOMContentLoaded', () => {
    const modal = new bootstrap.Modal(document.getElementById('export-modal'));
    const personTextarea = document.getElementById('export-modal-person-textarea');
    const form = document.getElementById('person-form');
  
    document
      .getElementById('export-modal-submit-button')
      .addEventListener('click', () => {
        new QRFormFiller({
          form,
          qrData: [
            {
              qrText: personTextarea.value,
              fields: [
                // undefined, если нужено пропустить элемент
                {
                  name: 'surname',
                },
                {
                  name: 'name'
                },
                {
                  name: 'patronymic'
                },
                {
                  name: 'birthday'
                },
                {
                  name: 'birthplace',
                },
                {
                  name: 'gender'
                },
              ]
            }
          ]
        }).fill();
  
        personTextarea.value = '';
        modal.hide();
      });
  
    document
      .getElementById('export-modal-close-button')
      .addEventListener('click', () => {
        modal.hide();
      });
  
    document
      .getElementById('qr-button')
      .addEventListener('click', () => {
        modal.show();
      });
  });