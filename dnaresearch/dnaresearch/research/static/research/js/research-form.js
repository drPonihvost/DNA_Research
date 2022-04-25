document.addEventListener('DOMContentLoaded', () => {
  const modal = new bootstrap.Modal(document.getElementById('export-modal'));
  const initiatorTextarea = document.getElementById('export-modal-initiator-textarea');
  const executorTextarea = document.getElementById('export-modal-executor-textarea');
  const eventTextarea = document.getElementById('export-modal-event-textarea');
  const form = document.getElementById('research-form');

  document
    .getElementById('export-modal-submit-button')
    .addEventListener('click', () => {
      new QRFormFiller({
        form,
        qrData: [
          {
            qrText: initiatorTextarea.value,
            fields: [
              // undefined, если нужено пропустить элемент
              undefined,
              {
                name: 'initiator_department',
              },
              {
                name: 'initiator_surname'
              },
              {
                name: 'initiator_name'
              },
              {
                name: 'initiator_patronymic'
              },
              {
                name: 'initiator_post',
              },
              {
                name: 'initiator_rank'
              },
            ]
          },
          {
            qrText: executorTextarea.value,
            fields: [
              // undefined, если нужено пропустить элемент
              undefined,
              {
                name: 'executor_department',
              },
              {
                name: 'executor_surname'
              },
              {
                name: 'executor_name'
              },
              {
                name: 'executor_patronymic'
              },
              {
                name: 'executor_post',
              },
              {
                name: 'executor_rank'
              },
            ]
          },
          {
            qrText: eventTextarea.value,
            fields: [
              // undefined, если нужено пропустить элемент
              {
                name: 'event_number',
              },
              {
                name: 'formation_date'
              },
              {
                name: 'incident_date'
              },
              {
                name: 'article'
              },
              {
                name: 'address',
              },
              {
                name: 'plot'
              },
            ]
          },
        ]
      }).fill();

      initiatorTextarea.value = '';
      executorTextarea.value = '';
      eventTextarea.value = '';
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