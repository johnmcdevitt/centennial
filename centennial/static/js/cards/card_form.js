// display color in heading based on type selected
document.getElementById("id_type").setAttribute("onchange", "colorHead(this.value)")

// TODO incorporate API with flask to get data in real-time
function colorHead(type) {
  console.log(type)
}

// title from head moved to hidden input field for submission
function updateTitle(value) {
  $("#id_title")[0].value = value
}

// for priority dropdown update hidden form field and display current choice
function setPriority(priority_choice) {
  // set hidden dropdown
  $("#id_priority")[0].value = priority_choice.getAttribute("value")
  // update visible button
  // this is the selected icon
  var selected = priority_choice.childNodes[0]
  // clone item, do not want to actually move the original with replace
  var clone_selected = selected.cloneNode(true)
  // get the current displayed item in the button
  display = $("#dropdownMenuPriority")[0].childNodes[1]
  // use replace child to update the displayed item with the cloned item
  display.parentNode.replaceChild(clone_selected,display)
}

// set initial values for custom dropdown for edit
$(document).ready(function () {
  // TODO get items with better selector than onclick attribute

  // get value for type on DOM loading
  var initial_type = $("#id_type")[0].value
  var initial_priority = $("#id_priority")[0].value
  var display_type = $("#dropdownMenuType")[0].childNodes[1]
  var display_priority = $("#dropdownMenuPriority")[0].childNodes[1]
  console.log(display_priority,display_type)

  // always set priority incase default is ever changed
  var initial_priority_display = $('a[value='+initial_priority+'][onclick="setPriority(this);"]')[0].childNodes[0]
  console.log(initial_priority_display)
  var clone_initial_priority_display = initial_priority_display.cloneNode(true)
  // use replace child to update the displayed item with the cloned item
  display_priority.parentNode.replaceChild(clone_initial_priority_display,display_priority)

  // only set type if necessary
  if (initial_type === "") {
    console.log("empty")
  }
  else {
    var initial_type_display = $('a[value='+initial_type+'][onclick="setType(this);"]')[0].childNodes[1]
    console.log(initial_type_display)
    var clone_initial_type_display = initial_type_display.cloneNode(true)
    // use replace child to update the displayed item with the cloned item
    display_type.parentNode.replaceChild(clone_initial_type_display,display_type)

  }
});


// for type dropdown update hidden form field and display current choice
function setType(type_choice) {
  // set hidden dropdown
  $("#id_type")[0].value = type_choice.getAttribute("value")
  // update visible button
  // this is the selected icon
  var selected = type_choice.childNodes[1]

  // clone item, do not want to actually move the original with replace
  var clone_selected = selected.cloneNode(true)
  // get the current displayed item in the button
  display = $("#dropdownMenuType")[0].childNodes[1]
  console.log("display", display)
  console.log("selected", selected)
  // use replace child to update the displayed item with the cloned item
  display.parentNode.replaceChild(clone_selected,display)
}