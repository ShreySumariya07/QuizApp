/*document.querySelector('.img-btn').addEventListener('click', function()
	{
		document.querySelector('.cont').classList.toggle('s-signup')
	}
);*/
// OR //
document.querySelector('.img-btn').addEventListener("click", myfunction);
function myfunction() {
	document.querySelector('.cont').classList.toggle('s-signup')
}

function myalertsignup() {
	alert("Sign Up Successful");
}

function myalertlogin() {
	alert("Login Successful");
}

/*

document.getElementById("student").onclick = function() { 
	var e = document.getElementById("student1");

	if(e.style.display == 'block')
		document.getElementById("student1").style.display = "none";
	else
        e.style.display = 'block';  

} 
document.getElementById("teacher").onclick = function() { 
	var e = document.getElementById("teacher1");

	if(e.style.display == 'block')
		document.getElementById("teacher1").style.display = "none";
	else
        e.style.display = 'block';  

} 
 


function toggle_visibility(teacher1) {
	var e = document.getElementById(teacher1);
	if(e.style.display == 'block')
	   e.style.display = 'none';
	else
	   e.style.display = 'block';
}
$("#teacher").click(function(){
	$("#teacher1").show();
  });

function toggle_visibility(student1) {
	var e = document.getElementById(student1);
	if(e.style.display == 'block')
	   e.style.display = 'none';
	else
	   e.style.display = 'block';
}
*/


 $(document).ready(function(){
	$("#teacher").click(function(){
	  $("#teacher1").hide();
	});
	$("#teacher").click(function(){
	  $("#student1").show();
	});
  });

  $(document).ready(function(){
	$("#student").click(function(){
	  $("#student1").hide();
	});
	$("#student").click(function(){
	  $("#teacher1").show();
	});
  });