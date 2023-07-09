function validate()
	{
		var keyword = document.forms["search_form"]["search"].value;
		if (keyword == ""){
			window.alert("At least a character should be entered!");
			return false;
		}
		return true;
	}