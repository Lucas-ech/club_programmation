window.addEventListener('load', function() {
	$("#userlist_input").autocomplete({
		source: '/utilisateurs/getUsersByUsername/',
		select : function(event, ui){
			var div = document.createElement('div');
			var span = document.createElement('span');
			var input = document.createElement('input');

			div.className = 'userlist_user';
			span.innerHTML = ui.item.value.charAt(0).toUpperCase() + ui.item.value.slice(1);
			div.appendChild(span);

			input.type = 'hidden';
			input.name = 'authors';
			input.value = ui.item.value;
			div.appendChild(input);

	    	var button = document.createElement('button');
	    	var i = document.createElement('i');
	    	i.className = 'glyphicon glyphicon-remove-circle';
	    	button.appendChild(i);
			button.addEventListener('click', removeItem, false);
	    	div.appendChild(button);

	    	this.parentNode.insertBefore(div, this.previousSibling);

	    	ui.item.value = '';
	    },
	});

	removeButtons = document.getElementsByClassName('userlist_remove');
	for(var i=0; i < removeButtons.length; i++) {
			console.log(i);
		removeButtons[i].addEventListener('click', removeItem, false);
	}
});

function removeItem(e) {
	e.preventDefault();
	e.target.parentNode.remove();
}