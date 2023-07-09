function validate()
	{
		var username = document.forms["form_register"]["user_name"].value;
		var f_name = document.forms["form_register"]["first_name"].value;
		var l_name = document.forms["form_register"]["last_name"].value;
		var pwd = document.forms["form_register"]["password"].value;
		var pwd2 = document.forms["form_register"]["password2"].value;
		var mail = document.forms["form_register"]["e_mail"].value;
		var phone = document.forms["form_register"]["phone_no"].value;
		var adr = document.forms["form_register"]["address"].value;
		if (username == "" || f_name == "" || l_name == "" || pwd == "" || pwd2 == "" || mail == "" || phone == "" || adr == "")
		{
			window.alert("All boxes should be filled!");
			return false;
		}
		else if (username.includes(" ") || f_name.includes(" ") || l_name.includes(" ") || pwd.includes(" ") ||
		pwd2.includes(" ") || mail.includes(" ") || phone.includes(" ") || adr.includes(" "))
		{
		    window.alert("Information must be entered without any space");
		    return false;
		}
		else if (pwd != pwd2)
		{
		    window.alert("Passwords don't match");
		    return false
		}
		return true;
	}