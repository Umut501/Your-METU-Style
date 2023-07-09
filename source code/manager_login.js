function validate()
	{
		var email = document.forms["manager_login"]["e_mail"].value;
		var pwd = document.forms["manager_login"]["password"].value;

		if (email == "")
		{
			window.alert("Email should be entered!");
			return false;
		}

		else if ( pwd == "")
		{
			window.alert("Password should be entered!");
			return false;
		}
		else if (email.includes(" "))
		{
		    window.alert("Email must be entered without any space");
		    return false;
		}
		else if (pwd.includes(" "))
		{
		    window.alert("Password must be entered without any space");
		    return false;
		}
	    return true;
	}