(function() {
   
  // Initialize Firebase

       
    //Get elements

    const txtEmail = document.getElementById('emailTxt');
    const txtPassword = document.getElementById('passwordTxt');
    const btnLogin = document.getElementById('btnli');
    const btnSignUp = document.getElementById('btns');
    const fpass = document.getElementById('fpass');

 
    btnLogin.addEventListener('click',e => {

        const email = txtEmail.value;
        const pass = txtPassword.value;
        const auth = firebase.auth();

        console.log('hello');


        if(validateEmail(email))
        {

        //Sign in

       
        const promise = auth.signInWithEmailAndPassword(email,pass);
       
        promise.catch(e => window.alert(e.message));




    }

    });

    fpass.addEventListener('click',e => {

        window.alert(emailTxt.value);
        const auth = firebase.auth();
        const emailAddress = emailTxt.value;

        auth.sendPasswordResetEmail(emailAddress).then(function() {
              window.alert('succes');
          }).catch(function(error) {
  
              window.alert('error');
        });


    });

    // Add signup event

    btnSignUp.addEventListener('click',e => {

        const email = txtEmail.value;
        const pass = txtPassword.value;
        const auth = firebase.auth();

        //Sign in
        const promise = auth.createUserWithEmailAndPassword(email,pass);

        promise
        .catch(e => window.alert(e.message));


    });

 
    firebase.auth().onAuthStateChanged(firebaseUser =>{

        if(firebaseUser)
        {
           
          document.location.href = 'index1.html';

            console.log(firebaseUser);
        }

        else
        {
            console.log('not logged in');


        }



    });



}());


function validateEmail(sEmail) {
  var reEmail = /^(?:[\w\!\#\$\%\&\'\*\+\-\/\=\?\^\`\{\|\}\~]+\.)*[\w\!\#\$\%\&\'\*\+\-\/\=\?\^\`\{\|\}\~]+@(?:(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-](?!\.)){0,61}[a-zA-Z0-9]?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9\-](?!$)){0,61}[a-zA-Z0-9]?)|(?:\[(?:(?:[01]?\d{1,2}|2[0-4]\d|25[0-5])\.){3}(?:[01]?\d{1,2}|2[0-4]\d|25[0-5])\]))$/;

  if(!sEmail.match(reEmail)) {
    alert("Invalid email address");
    return false;
  }

  return true;

}
