function validateTextbox() {
	var box=document.getElementById('name');
	var box2=document.getElementById('topic');
	var box3=document.getElementById('no_of_ques');
	var box4=document.getElementById('marks_per_ques');
	var box5=document.getElementById('total_marks');
	var box6=document.getElementById('author');
	if(box.value.length == "" || box2.value == "" || box3.value == "" || box4.value == "" || box5.value == "" || box5.value == "")
	{
		alert("Element Empty");
	    return false;
	}
	else
	{
		alert("Quiz Created");
	}
}