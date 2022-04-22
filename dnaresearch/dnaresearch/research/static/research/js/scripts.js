var listName = [];

Array.prototype.remove = function(value) {
  var idx = this.indexOf(value);
  if (idx != -1) {
    return this.splice(idx, 1);
  }
  return false;
}

$('.form-check-input').change(function(e) {
  if (e.target.checked) {
    listName.push(e.target.name);
  } else {
    listName.remove(e.target.name);
  }
  console.log(listName);
});