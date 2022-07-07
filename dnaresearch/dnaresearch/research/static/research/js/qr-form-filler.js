class QRFormFiller {
  constructor({ form, qrData = [] }) {
    if (!form) {
      throw 'Пустая форма!';
    }

    this.form = form;
    this.qrData = qrData;
    this.parseResult = {};
  }

  getFormSetter = type => {
    return {
      text: this.valueSetter,
      textarea: this.valueSetter,
      radio: this.radioSetter
    }[type] || (() => { });
  }

  valueSetter = (index, element) => {
    this.form.elements[index].value = this.parseResult[element.name];
  }

  radioSetter = (index, element) => {
    if (element.value === this.parseResult[element.name]) {
      this.form.elements[index].checked = true;
    }
  }

  parseQRText = text => {
    return text.split('*');
  }

  parseQRData() {
    const result = this.qrData.reduce(
      (accumulator, { qrText, fields = [] }) => {
        if (!qrText) {
          return accumulator;
        }

        const entities = this.parseQRText(qrText);

        entities.forEach((entity, index) => {
          const field = fields[index];

          if (field) {
            accumulator[field.name] = entity;
          }
        });

        return accumulator;
      },
      {}
    );

    this.parseResult = result;
  }

  fill() {
    this.parseQRData();

    Array.from(this.form.elements).forEach((element, index) => {
      if (element.name in this.parseResult) {
        const setter = this.getFormSetter(element.type);

        setter(index, element)
      }
    });
  }
}

window.QRFormFiller = QRFormFiller;