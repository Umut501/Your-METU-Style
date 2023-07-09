def print_forms(title, massage):
    print("Content-type: text/html")
    print("")
    print("""
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{}</title>
    <link rel="stylesheet" href="style.css">

    </head>
    <body class="bg">

    <ul>
      <li style="background-color:rgb(223, 223, 223)"><a style="color:red; font-family:Papyrus,Fantasy">YMS</a></li>
      <li style="float:right"><a href="manager_login.py">LogOut</a></li>
        <li class="dropdown">
            <a href="javascript:void(0)" class="dropbtn">PRODUCTS</a>
            <div class="dropdown-content">
              <a href="manager_product.py">MANAGE PRODUCTS</a>
              <a href="manager_display.py">DISPLAY PRODUCTS</a>
            </div>
          </li>
        <li>
          <a href="#">CUSTOMIZATION APPROVAL</a>
        </li>
      </ul>


  <div class="container">
    <div class="font bgf Add-New-Product" >

    <form novalidate autocomplete="off" #form="ngForm" (submit)="onSubmit(form)" action= "manager_insert.py">
      <div class="form-group">
        <label class="label">Product Name</label><br>
        <input required [class.invalid]="productName.invalid && productName.touched" class="form-control form-control-lg "
        placeholder="Enter Product Name" name="productName" #productName="ngModel" [(ngModel)]= "service.formData.productName">
    </div>     <br>

    <div class="form-group">
        <label  >Product Description</label><br>
        <input required [class.invalid]="productDescription.invalid && productDescription.touched" class="form-control form-control-lg "
        placeholder="Product Description" name="productDescription" #productDescription="ngModel" [(ngModel)]= "service.formData.productDescription">
    </div> <br>

    <div class="form-group">
        <label >Product Quantity</label><br>
        <input required [class.invalid]="productQuantity.invalid && productQuantity.touched" class="form-control form-control-lg "
        placeholder="Product Quantity" name="productQuantity" #productQuantity="ngModel" [(ngModel)]= "service.formData.productQuantity">
    </div> <br>

    <div class="form-group">
        <label >Product Type</label><br>
        <input required [class.invalid]="productType.invalid && productType.touched" class="form-control form-control-lg "
        placeholder="Product Type" name="productType" #productType="ngModel" [(ngModel)]= "service.formData.productType">
    </div> <br>

    <div class="form-group">
        <label >Product Color</label><br>
        <input required [class.invalid]="productColor.invalid && productColor.touched" class="form-control form-control-lg"
        placeholder="Product Color" name="productColor" #productColor="ngModel" [(ngModel)]= "service.formData.productColor">
    </div> <br>

    <div class="form-group">
        <label >Product Size</label><br>
        <input required [class.invalid]="productSize.invalid && productSize.touched" class="form-control form-control-lg "
        placeholder="Product Size" name="productSize" #productSize="ngModel" [(ngModel)]= "service.formData.productSize">
    </div> <br>

    <div class="form-group">
        <label >Product Price</label><br>
        <input required [class.invalid]="productPrice.invalid && productPrice.touched" class="form-control form-control-lg"
        placeholder="Product Price" name="productPrice" #productPrice="ngModel" [(ngModel)]= "service.formData.productPrice">
    </div>
    <br>
    <div class="form-group">
      <label >Product Link</label><br>
      <input required [class.invalid]="product_image_file.invalid && product_image_file.touched" class="form-control form-control-lg"
      placeholder="Product Image Link" name="product_image_file" #product_image_file="ngModel" [(ngModel)]= "service.formData.product_image_file">
  </div>
  <br>
    <div class="form-group">
        <button class="btn btn-info btn-lg fcolor btn-block" type="submit" [disabled]="form.invalid">SUBMIT</button>
    </div>

    </form><br><br></div>

    <div class="font bgf update">


      <form novalidate autocomplete="off" #form="ngForm" (submit)="onSubmit(form)" action= "manager_update.py">
      
        <div class="form-group">
          <label class="label">Product ID</label><br>
          <input required [class.invalid]="productid.invalid && productid.touched" class="form-control form-control-lg "
          placeholder="Enter Product ID" name="productid" #productid="ngModel" [(ngModel)]= "service.formData.productid">
      </div> <br>

      <div class="form-group">
          <label  >Product Quantity</label><br>
          <input required [class.invalid]="productQuantity.invalid && productQuantity.touched" class="form-control form-control-lg "
          placeholder="Enter Product Quantity" name="productQuantity" #productQuantity="ngModel" [(ngModel)]= "service.formData.productQuantity">
      </div> <br>
      <div class="form-group">
        <button class="btn btn-info btn-lg fcolor btn-block" type="submit" [disabled]="form.invalid">UPDATE</button>
    </div>

    </form><br>
  </div>
  <div class="font bgf delete">
    <form novalidate autocomplete="off" #form="ngForm" (submit)="onSubmit(form)"  action= "manager_delete.py">
      <div class="form-group">
        <label class="label">Product ID</label><br>
        <input required [class.invalid]="productid.invalid && productid.touched" class="form-control form-control-lg "
        placeholder="Enter Product ID" name="productid" #productid="ngModel" [(ngModel)]= "service.formData.productid">
    </div> <br>
    <div class="form-group">
      <button class="btn btn-info btn-lg fcolor btn-block" type="submit" [disabled]="form.invalid">DELETE</button>
  </div>
  </form><br>
    </div>
    </div>
    {}
    </body>
    </html>""".format(title, massage))


def print_invalid_manager_form():
    print("Content-type: text/html")
    print("")
    print("""<html><head><title>LogIn</title>
    <script src = "manager_login.js"></script>
    <link rel="stylesheet" type="text/css" href="manager_login.css"></head><body>
    <ul>
    <li style="background-color:rgb(223, 223, 223)"><a style="color:red; font-family:Papyrus,Fantasy" href="manager.py">YMS</a></li>
    </ul>""")

    print("""
    <h2></h2>
    <div>
    <h2 style="color:black; text-align: center">LogIn</h2>
    <form name = "manager_login" method="post" action= "manager.py" onsubmit="return validate();">
    <label for="e_mail">E-mail:</label><br>
    <input type="text" id="e_mail" name="e_mail">
    <label for="password">Password:</label><br>
    <input type="password" id="password" name="password">
    <p><input type="submit" value="LogIn" class="button button1"></p>
    </form>
    </div>""")

    print("""<p style="text-align: center">Your e_mail or password is invalid!!!</p>""")
    print("</body></html>")


def print_all_ptoducts():
    print("Content-type: text/html")
    print("")
    print("""<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{}</title>
    <link rel="stylesheet" href="style.css">

    </head>
    <body class="bg">

    <ul>
      <li style="background-color:rgb(223, 223, 223)"><a style="color:red; font-family:Papyrus,Fantasy">YMS</a></li>
      <li style="float:right"><a href="manager_login.py">LogOut</a></li>
        <li class="dropdown">
            <a href="javascript:void(0)" class="dropbtn">PRODUCTS</a>
            <div class="dropdown-content">
              <a href="manager_product.py">MANAGE PRODUCTS</a>
              <a href="manager_display.py">DISPLAY PRODUCTS</a>
            </div>
          </li>
        <li>
          <a href="#">CUSTOMIZATION APPROVAL</a>
        </li>
      </ul>""")
