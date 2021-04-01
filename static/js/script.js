$(document).ready(function () {
    $('.sidenav').sidenav();
    $('.parallax').parallax();
    $('.carousel').carousel();
    $('.modal').modal();
    $('select').formSelect();
   // $('#ingredients').val('');
   // M.textareaAutoResize($('#ingredients'));
   // $('#method').val('');
   // M.textareaAutoResize($('#method'));
   // $('#notes').val('');
   // M.textareaAutoResize($('#notes'));
   // M.updateTextFields();
});

// fetch("https://congen-temperature-converter-v1.p.rapidapi.com/fahrenheit?to=celsius&value=104&decimal=2", {
// 	"method": "GET",
// 	"headers": {
// 		"content-type": "application/json",
// 		"x-rapidapi-key": "SIGN-UP-FOR-KEY",
// 		"x-rapidapi-host": "congen-temperature-converter-v1.p.rapidapi.com"
// 	}
// })
// .then(response => {
// 	console.log(response);
// })
// .catch(err => {
// 	console.error(err);
// });
// //
// //
// var unirest = require("unirest");

// var req = unirest("GET", "https://food-unit-of-measurement-converter.p.rapidapi.com/convert");

// req.query({
// 	"unit": "<REQUIRED>",
// 	"ingredient": "<REQUIRED>",
// 	"value": "<REQUIRED>"
// });

// req.headers({
// 	"x-rapidapi-key": "88071a1f27msh218df85fe41f780p10e406jsn4741329a20c7",
// 	"x-rapidapi-host": "food-unit-of-measurement-converter.p.rapidapi.com",
// 	"useQueryString": true
// });


// req.end(function (res) {
// 	if (res.error) throw new Error(res.error);

// 	console.log(res.body);
// });
// //