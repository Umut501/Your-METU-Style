function validate()
	{
		var username = document.forms["form_login"]["user_name"].value;
		var pwd = document.forms["form_login"]["password"].value;
		
		if (username == ""){
			window.alert("Username should be entered!");
			return false;
		}
		else if ( pwd == ""){
			window.alert("Password should be entered!");
			return false;
		}
		else if (username.includes(" ")){
		    window.alert("Username must be entered without any space");
		    return false;
		}
		else if (pwd.includes(" ")){
		    window.alert("Password must be entered without any space");
		    return false;
		}
		return true;
	}