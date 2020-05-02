function changeWidth() {
	
	completed = document.getElementById('completedtasks').value;
	alltasks =  document.getElementById('amountoftasks').value;
	
	completed = parseFloat(completed);
	alltasks = parseFloat(alltasks);
	

	var result = (100*completed)/alltasks;
	
	if(isFinite(result) && completed <= alltasks) {
		
	    document.getElementById('completedprogress').style.width = result + "%";
	    document.getElementById('completedprogress').innerHTML = "%" + result;
		
	}
	
}
