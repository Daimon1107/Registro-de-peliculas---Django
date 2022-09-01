
console.log('El documento de js se cargo correctamente');

$('nav ul li.btn span').click(function(){
  $('nav ul div.items').toggleClass("show");
  $('nav ul li.btn span').toggleClass("show");
});