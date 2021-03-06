$( function() {
$( ".column" ).sortable({
  connectWith: ".column",
  handle: ".portlet-header",
  cancel: ".portlet-toggle",
  placeholder: "portlet-placeholder ui-corner-all",
  start: function(event,ui){
    const start_status = ui.item[0].getAttribute("cardstatus")
  },
  stop: function(event, ui) {
    var c = ui.item[0] // card
    var p = c.parentElement // card parent
    var data = {} // initialize data to be sent in ajax call

    // check for status change
    if (c.getAttribute("cardstatus") !== status[p.id]){
      c.setAttribute("cardstatus", status[p.id])
      c.setAttribute("order",status[p.id]+c.getAttribute("order").slice(3,9))
      data.cardstatus = status[p.id]
      data.order = c.getAttribute("order")
    }

    // set min and max order values
    var min, max
    try {
      min = Number(c.previousElementSibling.getAttribute("order"))
      if (min === null) throw "No previous sibling card"
    }
    catch(err) {
      console.log(err)
      min = Number(c.getAttribute("cardstatus"))*1000000
    }
    try {
      max = Number(c.nextElementSibling.getAttribute("order"))
      if (max === null) throw "No next sibling card"
    }
    catch(err) {
      console.log(err)
      max = (Number(c.getAttribute("cardstatus"))+1)*1000000-1
    }
    console.log(min)
    console.log(max)
    // check if order is between min and max values
    if ((min >= c.getAttribute("order")) || (max <= c.getAttribute("order"))) {
      var order = assignorder(min,max)
      data.order = order
      c.setAttribute("order", order)
    }
    else console.log("Order does not need to change")
    // check for data for ajax call
    if (Object.keys(data).length != 0) {
      // only updating if data is not empty
      console.log(data)
      cardupdate(c.id,data)
    }
  },
});
// hard coded
var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
const status = {
    backlog_col: '100',
    todo_col: '200',
    inprogress_col: '300',
    review_col: '400',
    done_col: '500',
};


function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function cardupdate(id,data){
  $.ajax({
    type: 'POST',
    url: '/cards/ajax/'+id+'/edit/',
    data: data,
    dataType: 'json',
    success: function(response) {
      if (response.status === 200) {
        console.log(response.message)
      }
    else {
      alert(response.status+': '+response.message)
    }
  },
})
};

function assignorder(min,max){
  return min+1+Math.floor((Math.random()*(max-min-1)))
}

$( ".portlet" )
  .addClass( "ui-widget ui-widget-content ui-helper-clearfix ui-corner-all" )
  .find( ".portlet-header" )
    .addClass( "ui-widget-header ui-corner-all" )
    .prepend( "<span class='ui-icon ui-icon-minusthick portlet-toggle'></span>");

$( ".portlet-toggle" ).on( "click", function() {
  var icon = $( this );
  icon.toggleClass( "ui-icon-minusthick ui-icon-plusthick" );
  icon.closest( ".portlet" ).find( ".portlet-content" ).toggle();
});
} );


  function taskStatusUpdate(el) {
    var style = "text-decoration:none;"
    var done = el.getElementsByTagName("input")[0].checked
    var id = el.getElementsByTagName("input")[0].id.match('[0-9]+')
    if (done) {
      style = "text-decoration:line-through;"
      done = 'True'
    }
    else {
        done = 'False'
    }
    el.getElementsByTagName("label")[0].setAttribute("style",style)

    $.ajax({
      type: 'POST',
      url: '/cards/ajax/task/'+id+'/edit/',
      data: {'done':done},
      dataType: 'json',
      success: function(response) {
        if (response.status === 200) {
          console.log(response.message)
        }
      else {
        alert(response.status+': '+response.message)
      }
    },
   })
  };

// get cards to be placed
var c = $("#card-staging .card");
for (var i = 0; i < c.length; i++) {
  // select corresponding element
  var e = $("#"+c[i].getAttribute("id"));
  if (c[i].getAttribute("cardstatus") === "100") {
    e.appendTo($("#backlog_col"));
  }
  else if (c[i].getAttribute("cardstatus") === "200") {
    e.appendTo($("#todo_col"));
  }
  else if (c[i].getAttribute("cardstatus") === "300") {
    e.appendTo($("#inprogress_col"));
  }
  else if (c[i].getAttribute("cardstatus") === "400") {
    e.appendTo($("#review_col"));
  }
  else if (c[i].getAttribute("cardstatus") === "500") {
    e.appendTo($("#done_col"));
  }
  else {
    console.log("Failed to place:", e);
  }
}

// scripts for modal forms
$(function () {

// create card
  $(".create-card").modalForm({formURL: "/cards/create/"});

// update card
  $(".card-edit-form").each(function() {
    $(this).modalForm({formURL: $(this).data("id")});
  });
});