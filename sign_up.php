<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Material Design for Bootstrap</title>

    <!-- Material Design Icons -->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">

    <!-- Bootstrap core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- Material Design Bootstrap -->
    <link href="css/mdb.css" rel="stylesheet">
    
</head>

<body>
    <!-- Navigation -->
  <nav class="navbar z-depth-2 info-color">
    <div class="container ">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand waves-effect waves-light" href="#">MDBootstrap</a>
      </div>

      <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
        <ul class="nav navbar-nav navbar-right">
          <li><a href="#products" class="waves-effect waves-light">Sign Up <span class="sr-only">(current)</span></a>
          </li>
          <li><a href="#products" class="waves-effect waves-light" data-toggle="modal" data-target="#modalLogin">Log In <span class="sr-only">(current)</span></a>
          </li>
          <!-- <li class="dropdown">
            <a href="#" class="dropdown-toggle waves-effect waves-light" data-toggle="dropdown" role="button" aria-expanded="false">List (click to expand) <span class="caret"></span></a>
            <ul class="dropdown-menu" role="menu">
              <li><a href="http://mdbootstrap.com/product/magic-portfolio-for-video-maker/">Video Maker</a>
              </li>
              <li><a href="http://mdbootstrap.com/material-design-for-bootstrap/">Material Design for Bootstrap</a>
              </li>
              <li><a href="http://mdbootstrap.com/product/magic-portfolio-for-creative-agency">Creative Agency</a>
              </li>
              <li><a href="http://mdbootstrap.com/product/magic-portfolio-photographer">Photographer Portfolio</a>
              </li>
              <li class="divider"></li>
              <li><a href="#footer">Footer</a>
              </li>
            </ul>
          </li> -->
        </ul><!-- 
        <form class="navbar-form navbar-right waves-effect waves-light" role="search">
          <div class="form-group">
            <input type="text" class="form-control" placeholder="Search">
          </div>
        </form> -->
      </div>
    </div>
  </nav>

  <!-- Modal -->
  <div class="modal fade" id="modalLogin" role="dialog">
      <div class="modal-dialog">

          <!-- Modal content-->
          <div class="modal-content">
              <div class="modal-header text-center">
                  <h4><i class="fa fa-user"></i> Login</h4>
              </div>
              <div class="modal-body" style="padding:40px 50px;">
                  <div class="row">
                      <form class="col-md-12">
                          <div class="row">
                              <div class="input-field">
                                  <i class="material-icons prefix">email</i>
                                  <input id="icon_email" type="tel" class="validate">
                                  <label for="icon_email">Your email</label>
                              </div>

                              <div class="input-field">
                                  <i class="material-icons prefix">lock</i>
                                  <input id="password" type="password" class="validate">
                                  <label for="password">Password</label>
                              </div>
                              <div class="text-center">
                                  <button type="button" class="btn btn-primary waves-effect waves-light">Login</button>

                              </div>
                          </div>
                      </form>
                  </div>
              </div>
              <!--Footer-->
              <div class="modal-footer">
                  <button type="submit" class="btn btn-default btn-default pull-left" data-dismiss="modal">X</button>
                  <div class="options">
                  <p>Not a member? <a href="#">Sign Up</a></p>
                  <p>Forgot <a href="#">Password?</a></p>
                  </div>
              </div>
              <!--/.Footer-->
          </div>
          <!-- /.Modal content-->
      </div>
  </div>
  <!-- Modal -->

  <!-- Container -->
  <div class="row">
    <div class="col-md-3"></div>
      <div class="col-md-6">
        <!--Header-->
          <div class="text-center">
              <h2><i class="fa fa-user"></i> Sign Up</h2>
          </div>
        <!--/.Header-->

        <!--Body-->
        <div class="modal-body">
            <div class="row">
                <div class="col-md-12">
                    <!--Form-->
                    <form>
                        <div class="input-field">
                          <i class="material-icons prefix">account_circle</i>
                          <input id="icon_prefix" type="text" class="validate">
                          <label for="icon_prefix">Username</label>
                        </div>

                        <div class="input-field">
                            <i class="material-icons prefix">email</i>
                            <input id="icon_email" type="tel" class="validate">
                            <label for="icon_email">Your email</label>
                        </div>

                        <div class="input-field">
                            <i class="material-icons prefix">lock</i>
                            <input id="password" type="password" class="validate">
                            <label for="password">Password</label>
                        </div>

                        <div class="input-field">
                            <i class="material-icons prefix">lock</i>
                            <input id="password-rep" type="password" class="validate">
                            <label for="password-rep">Repeat password</label>
                        </div>

                        <h4 class="text-center">Packet Offfered:</h4>
                        <div class="col-md-6">
                            <div class="card elegant-color darken-1">
                                <div class="card-content white-text">
                                    <input name="group1" type="radio" id="Free">
                                    <label for="Free"><span class="card-title">Free Plan</span></label>
                                    <p>Lorem ipsum dolor sit amet enim. Etiam ullamcorper. Suspendisse a pellentesque dui, non felis. Maecenas malesuada elit lectus felis, malesuada ultricies. Curabitur et ligula.</p>
                                </div>
                                <div class="card-action">
                                    <a href="#">READ MORE</a>
                                </div>
                            </div>
                        </div>

                        <div class="col-md-6">
                            <div class="card elegant-color darken-1">
                                <div class="card-content white-text">
                                    <input name="group1" type="radio" id="Premium">
                                    <label for="Premium"><span class="card-title" value="Premium">Premium Plan</span></label>
                                    <p>Lorem ipsum dolor sit amet enim. Etiam ullamcorper. Suspendisse a pellentesque dui, non felis. Maecenas malesuada elit lectus felis, malesuada ultricies. Curabitur et ligula.</p>
                                </div>
                                <div class="card-action">
                                    <a href="#">READ MORE</a>
                                </div>
                            </div>
                        </div>

                        <div class="text-center">
                            <button type="button" class="btn btn-primary btn-lg waves-effect waves-light">Sign up</button>
                        </div>

                    </form>
                    <!--/.Form-->
                </div>
            </div>
        </div>
        <!--/.Body-->

        <!--Footer-->
        <div class="modal-footer">
            <div class="options">
            <p>Already have an account? <a href="#" data-toggle="modal" data-target="#modalLogin">Login</a></p>
            </div>
        </div>
        <!--/.Footer-->
      </div>
    <div class="col-md-3"></div>
  </div>


  <div class="row">
    <div class="col-md-3"></div>
      
      <div class="col-md-3"></div>
  </div>
  <!-- Container -->


    <!-- SCRIPTS -->

    <!-- JQuery -->
    <script type="text/javascript" src="js/jquery.min.js"></script>

    <!-- Bootstrap core JavaScript -->
    <script type="text/javascript" src="js/bootstrap.min.js"></script>

    <!-- Material Design Bootstrap -->
    <script type="text/javascript" src="js/mdb.js"></script>


</body>

</html>